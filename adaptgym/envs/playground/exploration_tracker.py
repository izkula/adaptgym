"""
HOOK_NAMES = ('initialize_episode_mjcf',
              'after_compile',
              'initialize_episode',
              'before_step',
              'before_substep',
              'after_substep',
              'after_step')
"""
import math
from datetime import datetime

from bidict import bidict
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation
from PIL import Image

from scipy import sparse

import glob
import os
import getpass
from pathlib import Path


class ExplorationTracker:
    def __init__(self,
                 env_name: str,
                 run_id: int,
                 walkers,
                 primary_agent_id,
                 attention_threshold=3, #minimum time in seconds required for counting attention time
                 target_name: str = 'target/',
                 params: dict = None
                 ):

        self.env_name = env_name
        self.run_id = run_id
        self.walkers = walkers
        self.primary_agent_id = primary_agent_id
        self.target_name = target_name

        self.attention_threshold = attention_threshold

        self.total_step = 0
        self.episode_step = 0
        self.which_episode = 0
        self.first_csv_write = True

        self.geom_id = bidict()
        self.collision_tracker = None
        self.attention_tracker = None  ## tracks total time in seconds spent looking at different objects, each attention segment thresholded by attention_threshold
        self.attention_start = None
        self.episode_data = None

        self.fov = np.deg2rad(self.walkers[self.primary_agent_id]._mjcf_root.find('camera', 'egocentric').fovy)

        if params:
            self.logger = params['logger']
            self.grid_density = params['grid_density']
            self.episode_length = params['episode_length']
            self.env_raw_output_file_name = params['env_raw_output_file_name']
            self.record_every_k_timesteps = params['record_every_k_timesteps']
            self.episodes_for_summary_metrics = params['episodes_for_summary_metrics']
            self.logdir = params['logdir']
            self.flush_data_every = params['flush_logger_every']

        else:
            self.logger = None
            self.grid_density = 20
            self.episode_length = None
            self.env_raw_output_file_name = f'log_{datetime.now().strftime("%Y%m%d%H%M%S")}.csv'
            self.record_every_k_timesteps = 20
            self.episodes_for_summary_metrics = 20
            self.logdir = Path(f'/home/{getpass.getuser()}/logs/')
            self.flush_data_every = 2000
            # self.logdir = Path(f'/home/{getpass.getuser()}/gendreamer/logs/')

        # self.flush_data_every = 2000 # Number of steps for flushing data (relevant in nonepisodic instances)
        # self.flush_data_every = 2000 # Number of steps for flushing data (relevant in nonepisodic instances)


        print(f'Logging exploration information to {self.logdir / self.env_raw_output_file_name}')

    def after_step(self, physics, random_state):
        self.episode_step += 1
        self.total_step += 1

        primary_agent_name = self.walkers[self.primary_agent_id].mjcf_model.model
        # primary_agent_in_contact = {v: False for v in self.geom_id}
        # primary_agent_in_contact['wall'] = False
        for contact in physics.data.contact:
            if contact.geom1 == self.geom_id[f'{primary_agent_name}/shell']:
                contact_with_primary_agent = True
                other_geom_id = contact.geom2
            elif contact.geom2 == self.geom_id[f'{primary_agent_name}/shell']:
                contact_with_primary_agent = True
                other_geom_id = contact.geom1
            else:
                contact_with_primary_agent = False
                other_geom_id = None

            if contact_with_primary_agent:
                # Is what primary agent collided with in set of 'important' geom_ids?
                if other_geom_id in self.wall_geom_ids:
                    self.collision_tracker['wall'] += 1
                elif other_geom_id in self.geom_id.values():
                    self.collision_tracker[self.geom_id.inverse[other_geom_id]] += 1
            else:
                if contact.geom1 in self.wall_geom_ids:
                    if contact.geom2 in self.geom_id.values():
                        cname = f"{self.geom_id.inverse[contact.geom2]}_wall"
                        self.collision_tracker[cname] += 1
                elif contact.geom2 in self.wall_geom_ids:
                    if contact.geom1 in self.geom_id.values():
                        cname = f"{self.geom_id.inverse[contact.geom1]}_wall"
                        self.collision_tracker[cname] += 1
                else:
                    if contact.geom1 in self.geom_id.values() and contact.geom2 in self.geom_id.values():
                        cname = f"{self.geom_id.inverse[contact.geom1]}_{self.geom_id.inverse[contact.geom2]}"
                        self.collision_tracker[cname] += 1
        # for geom_id in primary_agent_in_contact:
        #     if not primary_agent_in_contact[geom_id]:
        #         self.collision_tracker[geom_id].append(0)

        for walker in self.walkers:
            if walker == self.primary_agent_id:
                continue
            ##
            name = f'{self.walkers[walker].mjcf_model.model}/shell'
            quaternion = physics.bind(self.walkers[self.primary_agent_id].root_body).xquat
            z_angle_abs = np.arctan2(
                2 * (quaternion[0] * quaternion[3] + quaternion[1] * quaternion[2]),
                1 - 2 * (quaternion[2] ** 2 + quaternion[3] ** 2))
            init_quat = physics.bind(self.walkers[self.primary_agent_id]._mjcf_root.find('body', 'head_body')).quat
            init_z_angle = np.arctan2(
                2 * (init_quat[0] * init_quat[3] + init_quat[1] * init_quat[2]),
                1 - 2 * (init_quat[2] ** 2 + init_quat[3] ** 2))
            camera_z_angle = z_angle_abs - init_z_angle

            dir_ =  physics.bind(self.walkers[walker].root_body).xpos - physics.bind(self.walkers[self.primary_agent_id].root_body).xpos
            agent_z_angle = np.arctan2(dir_[1],dir_[0])

            in_view = agent_z_angle > camera_z_angle - self.fov / 2 and agent_z_angle < camera_z_angle + self.fov / 2

            if in_view:
                # if self.attention_start[walker] is None:
                self.attention_tracker[name] += 1
            # else:
            #     self.attention_tracker[name] += 0

            # else:
            #     if self.attention_start[walker] is not None:# and physics.time() - self.attention_start[walker] > self.attention_threshold: #only count when looking at the object for long time
            #         self.attention_tracker[walker] += (physics.time() - self.attention_start[walker])
            #
            #     self.attention_start[walker] = None


        if self.episode_step % self.record_every_k_timesteps == 0:

            row = {}
            row['episode'] = self.which_episode
            row['step'] = self.episode_step
            row['total_step'] =  self.total_step

            for walker in self.walkers:
                bound_walker = physics.bind(self.walkers[walker].root_body)
                walker_name = self.walkers[walker].mjcf_model.model

                row[f'{walker_name}_xloc'] = bound_walker.xpos[0]
                row[f'{walker_name}_yloc'] = bound_walker.xpos[1]
                row[f'{walker_name}_zloc'] = bound_walker.xpos[2]

                row[f'{walker_name}_xvel'] = bound_walker.cvel[3]
                row[f'{walker_name}_yvel'] = bound_walker.cvel[4]
                row[f'{walker_name}_zvel'] = bound_walker.cvel[5]

                if walker == self.primary_agent_id:
                    # To capture others, it would be [f'ball{walker}/egocentric']
                    cam_xmat = physics.named.data.cam_xmat[f'{walker_name}/egocentric']
                    cam_xmat = np.array(cam_xmat).reshape((3, 3))
                    r = Rotation.from_matrix(cam_xmat)
                    orientation = r.as_euler("ZYX")[0]
                    row[f'{walker_name}_orientation'] = orientation
                    try:
                        row[f'{walker_name}_steer_velocity'] = \
                            physics.named.data.actuator_velocity[f'{walker_name}/steer']
                        row[f'{walker_name}_roll_velocity'] = \
                            physics.named.data.actuator_velocity[f'{walker_name}/roll']
                    except:
                        pass

            target_xpos = physics.named.data.xpos[f'{self.target_name}/']
            row[f'target_xloc'] = target_xpos[0]
            row[f'target_yloc'] = target_xpos[1]
            row[f'target_zloc'] = target_xpos[2]

            for c in self.collision_tracker:
                row[f'collisions_{c}'] = self.collision_tracker[c]

            for c in self.attention_tracker:
                row[f'attention_{c}'] = self.attention_tracker[c]
            self.episode_data.append(row)

            # Reset collision tracker
            self.collision_tracker = {geom: 0 for geom in self.geom_id}
            for geom1 in self.geom_id:
                for geom2 in self.geom_id:
                    self.collision_tracker[f"{geom1}_{geom2}"] = 0
            for geom1 in self.geom_id:
                self.collision_tracker[f"{geom1}_wall"] = 0

            self.collision_tracker['wall'] = 0
            self.attention_tracker = {f'{self.walkers[name].mjcf_model.model}/shell': 0 for name in self.walkers if
                                      name != self.primary_agent_id}

        if self.total_step % self.flush_data_every == 0:
            self.flush_data(physics, random_state, increment_episode=False)

    def flush_data(self, physics, random_state, increment_episode=False):
        # print('flush_data executing in exploration tracker')

        if self.episode_data:
            ### TODO: Add in episode timestamp here?
            df = pd.DataFrame(self.episode_data, columns=self.episode_data[0].keys())

            # Add timestamp so can match to replay buffer episodes. This timestamp will be later in time.
            timestamp = datetime.now().strftime('%Y%m%dT%H%M%S')
            df['timestamp'] = timestamp

            df.to_csv(self.logdir / self.env_raw_output_file_name, mode='a', header=self.first_csv_write, float_format='%.4f')
            self.first_csv_write = False

        if increment_episode:
            self.episode_step = 0
            self.which_episode += 1

        for walker in self.walkers:
            walker_name = self.walkers[walker].mjcf_model.model
            geom_name = f'{walker_name}/shell'
            # if geom_name in self.geom_id.keys():
            try:
                self.geom_id[geom_name] = physics.named.model.geom_bodyid.axes.row.names.index(geom_name)
            except:
                pass

        self.geom_id[f'{self.target_name}/geom'] = physics.named.model.geom_bodyid.axes.row.names.index(f'{self.target_name}/geom')
        self.collision_tracker = {geom: 0 for geom in self.geom_id}
        for geom1 in self.geom_id:
            for geom2 in self.geom_id:
                self.collision_tracker[f"{geom1}_{geom2}"] = 0
        for geom1 in self.geom_id:
            self.collision_tracker[f"{geom1}_wall"] = 0
        self.episode_data = []

        self.attention_tracker = {f'{self.walkers[name].mjcf_model.model}/shell': 0 for name in self.walkers if name != self.primary_agent_id}
        self.attention_start = {f'{self.walkers[name].mjcf_model.model}/shell': None for name in self.walkers if name != self.primary_agent_id}
        self.wall_geom_ids = np.where(['wall' in x for x in physics.named.model.geom_bodyid.axes.row.names])[0]
        self.collision_tracker['wall'] = 0


    def initialize_episode(self, physics, random_state):

        print('initialize_episode hook executing in exploration tracker')

        self.flush_data(physics, random_state, increment_episode=True)


