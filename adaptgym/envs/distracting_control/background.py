# coding=utf-8
# Copyright 2021 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""A wrapper for dm_control environments which applies color distractions."""
import os

from PIL import Image
import collections
from dm_control.rl import control
import numpy as np

from dm_control.mujoco.wrapper import mjbindings

import scipy.ndimage

DAVIS17_TRAINING_VIDEOS = [
    'bear', 'bmx-bumps', 'boat', 'boxing-fisheye', 'breakdance-flare', 'bus',
    'car-turn', 'cat-girl', 'classic-car', 'color-run', 'crossing',
    'dance-jump', 'dancing', 'disc-jockey', 'dog-agility', 'dog-gooses',
    'dogs-scale', 'drift-turn', 'drone', 'elephant', 'flamingo', 'hike',
    'hockey', 'horsejump-low', 'kid-football', 'kite-walk', 'koala',
    'lady-running', 'lindy-hop', 'longboard', 'lucia', 'mallard-fly',
    'mallard-water', 'miami-surf', 'motocross-bumps', 'motorbike', 'night-race',
    'paragliding', 'planes-water', 'rallye', 'rhino', 'rollerblade',
    'schoolgirls', 'scooter-board', 'scooter-gray', 'sheep', 'skate-park',
    'snowboard', 'soccerball', 'stroller', 'stunt', 'surf', 'swing', 'tennis',
    'tractor-sand', 'train', 'tuk-tuk', 'upside-down', 'varanus-cage', 'walking'
]
DAVIS17_VALIDATION_VIDEOS = [
    'bike-packing', 'blackswan', 'bmx-trees', 'breakdance', 'camel',
    'car-roundabout', 'car-shadow', 'cows', 'dance-twirl', 'dog', 'dogs-jump',
    'drift-chicane', 'drift-straight', 'goat', 'gold-fish', 'horsejump-high',
    'india', 'judo', 'kite-surf', 'lab-coat', 'libby', 'loading', 'mbike-trick',
    'motocross-jump', 'paragliding-launch', 'parkour', 'pigs', 'scooter-black',
    'shooting', 'soapbox'
]
SKY_TEXTURE_INDEX = 0
Texture = collections.namedtuple('Texture', ('size', 'address', 'textures'))


def imread(filename):
  img = Image.open(filename)
  img_np = np.asarray(img)
  return img_np


def size_and_flatten(image, ref_height, ref_width):
  # Resize image if necessary and flatten the result.
  image_height, image_width = image.shape[:2]

  if image_height != ref_height or image_width != ref_width:
    image = scipy.ndimage.zoom(image, (ref_height / image_height, ref_width / image_width, 1),
                               order=1).astype(np.uint8)
  return np.reshape(image, [-1])


def blend_to_background(alpha, image, background):
  if alpha == 1.0:
    return image
  elif alpha == 0.0:
    return background
  else:
    return (alpha * image.astype(np.float32)
            + (1. - alpha) * background.astype(np.float32)).astype(np.uint8)


class DistractingBackgroundEnv(control.Environment):
  """Environment wrapper for background visual distraction.

  **NOTE**: This wrapper should be applied BEFORE the pixel wrapper to make sure
  the background image changes are applied before rendering occurs.

  Args:
    specify_background: a string with format 'vid_id,start_step,endstep;next_vid_id,start_step,end_step'

  """

  def __init__(self,
               env,
               dataset_path=None,
               dataset_videos=None,
               video_alpha=1.0,
               ground_plane_alpha=1.0,
               num_videos=None,
               dynamic=False,
               seed=None,
               shuffle_buffer_size=None,
               randomize_background=1,
               continuous_video_frames=False,
               specify_background=None,
               divide_step_count_by=1,
               ):

    if not 0 <= video_alpha <= 1:
      raise ValueError('`video_alpha` must be in the range [0, 1]')

    self._env = env
    self._video_alpha = video_alpha
    self._ground_plane_alpha = ground_plane_alpha
    self._random_state = np.random.RandomState(seed=seed)
    self._dynamic = dynamic
    self._shuffle_buffer_size = shuffle_buffer_size
    self._background = None
    self._current_img_index = 0
    self._randomize_background = randomize_background
    self._continuous_video_frames = continuous_video_frames
    self._divide_step_count_by = divide_step_count_by

    self.step_counter = 0
    self.ep_counter = 0
    if specify_background == 'None':
      specify_background = None
    self.specify_background = specify_background

    if specify_background is not None:
      self.specify_background = []
      for val in specify_background.split(';'):
        # self.specify_background.append([int(float(x)) for x in val.split(',')])
        self.specify_background.append([x for x in val.split(',')])

    if not dataset_path or num_videos == 0:
      # Allow running the wrapper without backgrounds to still set the ground
      # plane alpha value.
      self._video_paths = []
    else:
      # Use all videos if no specific ones were passed.
      if not dataset_videos:
        dataset_videos = sorted(os.listdir(dataset_path))
      # Replace video placeholders 'train'/'val' with the list of videos.
      elif dataset_videos in ['train', 'training']:
        dataset_videos = DAVIS17_TRAINING_VIDEOS
      elif dataset_videos in ['val', 'validation']:
        dataset_videos = DAVIS17_VALIDATION_VIDEOS
      # Get complete paths for all videos.
      video_paths = [
          os.path.join(dataset_path, subdir) for subdir in dataset_videos
      ]

      # Optionally use only the first num_paths many paths.
      if num_videos is not None and not num_videos == 'All':
        if num_videos > len(video_paths) or num_videos < 0:
          raise ValueError(f'`num_bakground_paths` is {num_videos} but '
                           'should not be larger than the number of available '
                           f'background paths ({len(video_paths)}) and at '
                           'least 0.')
        video_paths = video_paths[:num_videos]

      self._video_paths = video_paths

  def reset(self):
    """Reset the background state."""
    time_step = self._env.reset()
    self._reset_background()
    self.ep_counter += 1
    return time_step

  def _reset_background(self):
    # Make grid semi-transparent.
    if self._ground_plane_alpha is not None:
      self._env.physics.named.model.mat_rgba['grid',
                                             'a'] = self._ground_plane_alpha

    # For some reason the height of the skybox is set to 4800 by default,
    # which does not work with new textures.
    self._env.physics.model.tex_height[SKY_TEXTURE_INDEX] = 800

    # Set the sky texture reference.
    sky_height = self._env.physics.model.tex_height[SKY_TEXTURE_INDEX]
    sky_width = self._env.physics.model.tex_width[SKY_TEXTURE_INDEX]
    sky_size = sky_height * sky_width * 3
    sky_address = self._env.physics.model.tex_adr[SKY_TEXTURE_INDEX]

    sky_texture = self._env.physics.model.tex_rgb[sky_address:sky_address +
                                                  sky_size].astype(np.float32)

    if self._video_paths:

      if self._shuffle_buffer_size:
        print('--> Shuffling background!')
        # Shuffle images from all videos together to get background frames.
        file_names = [
            os.path.join(path, fn)
            for path in self._video_paths
            for fn in os.listdir(path)
        ]
        self._random_state.shuffle(file_names)
        # Load only the first n images for performance reasons.
        file_names = file_names[:self._shuffle_buffer_size]
        images = [imread(fn) for fn in file_names]

        # Pick a random starting point and stepping direction.
        self._current_img_index = self._random_state.choice(len(images))
        self._step_direction = self._random_state.choice([-1, 1])
      else:
        if self.specify_background is None:
          # Randomly pick a video and load all images.
          video_path = self._random_state.choice(self._video_paths)
        else:
          vid_id = 0 #default
          for id, start_step, end_step in self.specify_background:
            start_step = int(float(start_step)/self._divide_step_count_by)
            end_step = int(float(end_step)/self._divide_step_count_by)
            if '&' in id:
              if self.step_counter >= start_step and self.step_counter < end_step:
                ids = id.split(':')[0]
                ratio = int(float(id.split(':')[1]))
                id0 = int(float(ids.split('&')[0]))
                id1 = int(float(ids.split('&')[1]))
                if np.mod(self.ep_counter, ratio) == 0:
                  vid_id = id0
                else:
                  vid_id = id1
            else:
              if self.step_counter >= start_step and self.step_counter < end_step:
                vid_id = int(float(id))
          video_path = self._video_paths[vid_id]
        file_names = os.listdir(video_path)


        # The above listdir operation loads files in an arbitrary order.
        # This is potentially a bug! I added a parameter to flag if frames should be
        # put into sequential order, which allows for smooth playing of video. I believe
        # setting this to "True" is in line with the intent of the paper.
        #
        # From the paper:
        # > In the dynamic setting, the video plays forwards or backwards until the last
        # > or first frame is reached at which point the playing direction  is reversed.
        # > This way, the background motion is always smooth and without “cuts”.

        if self._continuous_video_frames:
            file_names.sort()

        if self._randomize_background:
            if not self._dynamic:
              # Randomly pick a single static frame.
              file_names = [self._random_state.choice(file_names)]
            images = [imread(os.path.join(video_path, fn)) for fn in file_names]

            # Pick a random starting point and stepping direction.
            self._current_img_index = self._random_state.choice(len(images))
            self._step_direction = self._random_state.choice([-1, 1])
        else:
          if not self._dynamic:  # Select a static frame
              file_names = [file_names[0]]
          images = [imread(os.path.join(video_path, fn)) for fn in file_names]
          self._current_img_index = 0
          self._step_direction = 1

      # Prepare images in the texture format by resizing and flattening.

      # Generate image textures.
      texturized_images = []
      for image in images:
        image_flattened = size_and_flatten(image, sky_height, sky_width)
        new_texture = blend_to_background(self._video_alpha, image_flattened,
                                          sky_texture)
        texturized_images.append(new_texture)

    else:

      self._current_img_index = 0
      texturized_images = [sky_texture]

    self._background = Texture(sky_size, sky_address, texturized_images)
    self._apply()

  def step(self, action):
    time_step = self._env.step(action)

    if time_step.first():
      self._reset_background()
      return time_step

    if self._dynamic and self._video_paths:
      # Move forward / backward in the image sequence by updating the index.
      self._current_img_index += self._step_direction

      # Start moving forward if we are past the start of the images.
      if self._current_img_index <= 0:
        self._current_img_index = 0
        self._step_direction = abs(self._step_direction)
      # Start moving backwards if we are past the end of the images.
      if self._current_img_index >= len(self._background.textures):
        self._current_img_index = len(self._background.textures) - 1
        self._step_direction = -abs(self._step_direction)

      self._apply()

    self.step_counter += 1

    return time_step

  def _apply(self):
    """Apply the background texture to the physics."""

    if self._background:
      start = self._background.address
      end = self._background.address + self._background.size
      texture = self._background.textures[self._current_img_index]

      self._env.physics.model.tex_rgb[start:end] = texture
      # Upload the new texture to the GPU. Note: we need to make sure that the
      # OpenGL context belonging to this Physics instance is the current one.
      with self._env.physics.contexts.gl.make_current() as ctx:
        ctx.call(
            mjbindings.mjlib.mjr_uploadTexture,
            self._env.physics.model.ptr,
            self._env.physics.contexts.mujoco.ptr,
            SKY_TEXTURE_INDEX,
        )

  # Forward property and method calls to self._env.
  def __getattr__(self, attr):
    if hasattr(self._env, attr):
      return getattr(self._env, attr)
    raise AttributeError("'{}' object has no attribute '{}'".format(
        type(self).__name__, attr))