from adaptgym.envs.distracting_control import suite


def test_ddmc_walker():
  domain = 'walker'
  task = 'walk'
  dynamic = False
  num_videos = 3
  randomize_background = 0
  shuffle_background = 0
  do_color_change = 0
  ground_plane_alpha = 0.1
  background_dataset_videos = [ 'boat', 'bmx-bumps', 'flamingo' ]
  continuous_video_frames = True
  do_just_background = True
  difficulty = 'easy'
  specify_background = '0,0,1e6;1,1e6,2e6;0,2e6,1e9'  # ABA

  env = suite.load(domain, task, difficulty=difficulty,
                         pixels_only=False, do_just_background=do_just_background,
                         do_color_change=do_color_change,
                         background_dataset_videos=background_dataset_videos,
                         background_kwargs=dict(num_videos=num_videos,
                                                dynamic=dynamic,
                                                randomize_background=randomize_background,
                                                shuffle_buffer_size=shuffle_background * 500,
                                                seed=1,
                                                ground_plane_alpha=ground_plane_alpha,
                                                continuous_video_frames=continuous_video_frames,
                                                specify_background=specify_background,
                                                ))
  assert 1 == 1
