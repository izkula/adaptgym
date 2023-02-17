"""Policies for agents.
This can be used to control sphero agents. 
Can be used as input to SpecifyMultiagents wrapper."""

import numpy as np
from scipy.spatial.transform import Rotation as R

def random(time_step, physics, agent, action_spec, step_number=0, scale=1):
    del time_step
    action = scale*np.random.uniform(low=action_spec.minimum,
                               high=action_spec.maximum,
                               size=action_spec.shape)
    return action

# Pass it into specified policies for each agent
def still(time_step,  physics,agent, action_spec, step_number, scale=1):
    action = np.zeros(action_spec.shape)
    return action

def jump_periodic(time_step, physics, agent, action_spec, step_number=0, scale=1, period=150):
    pos = time_step.observation['absolute_position_'+agent]
    ori = time_step.observation['absolute_orientation_'+agent]
    # vel = time_step.observation[agent+'/sensors_velocimeter']
    a = 0.1
    w = 2*np.pi/period
    # action = np.array([0, 0, np.sin(2 * np.pi / period * step_number) * scale * a])
    if np.mod(step_number, period) == 0:
        action = np.array([0, 0, scale])
    else:
        action = np.array([0, 0, 0])
    # action  = np.array([0, 0, 10])

    return action

def circle_periodic(time_step, physics, agent, action_spec, step_number=0, scale=1):
    # if agent == "ball1":
    #     # ball1_pos = time_step.observation['absolute_position_ball1']
    #     # ball1_ori = time_step.observation['absolute_orientation_ball1']
    #     # ball1_vel = time_step.observation['ball1/sensors_velocimeter']
    #     # action = np.array([scale*0.1, 0.75])
    #     action = np.array([scale*0.5, 0.5])
    # elif agent == "ball2":
    #     action = np.array([scale*0.3, 0.75])
    # elif agent == "ball3":
    #     # action = np.array([scale*0.4, 0.75])
    #     action = np.array([scale*0.5, 0.5])
    # elif agent == "ball4":
    #     action = np.array([scale*0.5, 0.5])
    # elif agent == "ball5":
    #     action = np.array([scale*0.3, 0.75])
    # else:
    #     action = np.zeros(action_spec.shape)
    action = np.array([scale * 0.5, 0.5])
    return action

def line_periodic(time_step,  physics,agent, action_spec, step_number, scale=1, period=100):
    pos = time_step.observation['absolute_position_'+agent]
    ori = time_step.observation['absolute_orientation_'+agent]
    # vel = time_step.observation[agent+'/sensors_velocimeter']

    action = np.array([-np.sin(2 * np.pi / period * step_number) * scale, 0])

    return action

def line(time_step, physics, agent, action_spec, step_number, scale=1):
    pos = time_step.observation['absolute_position_'+agent]
    ori = time_step.observation['absolute_orientation_'+agent]
    a = 1
    action = np.array([-scale * a, 0])
    return action

def line_periodic_teleport(time_step, physics, agent, action_spec, step_number, walker, period_line=100, period_tp=10, scale=1, dist=10):
    pos = time_step.observation['absolute_position_'+agent]
    ori = time_step.observation['absolute_orientation_'+agent]
    quaternion = time_step.observation['absolute_quaternion_'+agent]
    maze_size = time_step.observation['maze_size']
    if step_number % period_tp == 0 and step_number > 0:
        z_angle_abs = np.arctan2(
            2 * (quaternion[0] * quaternion[3] + quaternion[1] * quaternion[2]),
            1 - 2 * (quaternion[2] ** 2 + quaternion[3] ** 2))

        init_quat =  physics.bind(walker._mjcf_root.find('body', 'head_body')).quat
        init_z_angle = np.arctan2(
            2 * (init_quat[0] * init_quat[3] + init_quat[1] * init_quat[2]),
            1 - 2 * (init_quat[2] ** 2 + init_quat[3] ** 2))
        z_angle = z_angle_abs - init_z_angle
        dir_ = R.from_rotvec([0,0,z_angle]).apply([1,0,0])
        new_pos = pos - dir_ * dist ## set back
        new_pos[:2] = np.clip(new_pos[:2],[-maze_size[0], -maze_size[1]],[maze_size[0], maze_size[1]])
        walker.set_pose(physics, position=new_pos)
        # walker.set_velocity(physics, velocity=np.zeros(3), angular_velocity=np.zeros(3))
        # walker.shift_pose()
    action = np.array([-np.sin(2 * np.pi / period_line * step_number) * scale, 0])
    return action

def reset_position(time_step, physics, agent, action_spec, step_number, walker, reset_position_freq, start_pos=[0., 0.], step_disappear=None):
    pos = time_step.observation['absolute_position_'+agent]
    maze_size = time_step.observation['maze_size']
    if reset_position_freq > 0:
        # if np.mod(step_number, reset_position_freq) == 0:
        #     print(f'JUMPING {agent} to: {start_pos} at step {step_number}')
        #
        #     new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
        #     new_pos[:2] = np.clip(new_pos[:2],[-maze_size[0], -maze_size[1]],[maze_size[0], maze_size[1]])
        #     walker.set_pose(physics, position=new_pos)

        if step_disappear is not None and step_number == step_disappear:
            new_pos = np.array([-maze_size[0], -maze_size[1], pos[2]])
            walker.set_pose(physics, position=new_pos)

        if step_disappear is None or step_number < step_disappear:
            if np.mod(step_number, reset_position_freq) == 0:
                print(f'JUMPING {agent} to: {start_pos} at step {step_number}')

                new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
                new_pos[:2] = np.clip(new_pos[:2], [-maze_size[0], -maze_size[1]], [maze_size[0], maze_size[1]])
                walker.set_pose(physics, position=new_pos)

    action = np.array([0., 0.])
    return action

def hardcode_trajectory(time_step, physics, agent, action_spec, step_number, walker, reset_position_freq, start_pos=[0., 0.]):
    pos = time_step.observation['absolute_position_'+agent]
    maze_size = time_step.observation['maze_size']

    # xs = np.arange(1, 10, 0.1)
    # ys = np.arange(1, 5, 0.1)
    xs = np.arange(1, 10, 0.1)
    ys = np.arange(1, 5, 0.1)


    # new_pos = np.array([np.mod(step_number, 10)/2, np.mod(step_number, 10)/2, 0.3])
    # new_pos = np.array([xs[np.mod(step_number, len(xs))], ys[np.mod(step_number, len(ys))], 0.3])
    new_pos = np.array([3*np.sin(step_number/50), 3*np.cos(step_number/40), 0.3])
    new_pos[:2] = np.clip(new_pos[:2],[-maze_size[0], -maze_size[1]],[maze_size[0], maze_size[1]])
    walker.set_pose(physics, position=new_pos)

    action = np.array([0., 0.])
    return action

def object_appear(time_step, physics, agent, action_spec, step_number, walker, step_appear, step_disappear, start_pos=[0., 0.], reset_position_freq=0):
    pos = time_step.observation['absolute_position_'+agent]
    ori = time_step.observation['absolute_orientation_'+agent]
    quaternion = time_step.observation['absolute_quaternion_'+agent]
    maze_size = time_step.observation['maze_size']

    if step_disappear is not None:
        assert(step_disappear >= step_appear)

    if step_number == step_appear:
        new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
        new_pos[:2] = np.clip(new_pos[:2],[-maze_size[0], -maze_size[1]],[maze_size[0], maze_size[1]])
        walker.set_pose(physics, position=new_pos)
    if step_disappear is not None:
        if step_number == step_disappear:
            new_pos = np.array([-maze_size[0], -maze_size[1], pos[2]])
            walker.set_pose(physics, position=new_pos)

    # Deal with resetting environment appropriately
    if time_step.first():
        print(f'$$$$$$$$$$$$$$$>>>>>>>>>>>>>>> FIRST TIME STEP global_step={step_number}')
        if step_number < step_appear:
            pass
        elif step_number >= step_appear and step_disappear is None:
            new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
            new_pos[:2] = np.clip(new_pos[:2], [-maze_size[0], -maze_size[1]], [maze_size[0], maze_size[1]])
            walker.set_pose(physics, position=new_pos)
        elif step_number >= step_appear and step_number < step_disappear:
            new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
            new_pos[:2] = np.clip(new_pos[:2], [-maze_size[0], -maze_size[1]], [maze_size[0], maze_size[1]])
            walker.set_pose(physics, position=new_pos)
        elif step_number >= step_disappear:
            new_pos = np.array([-maze_size[0], -maze_size[1], pos[2]])
            walker.set_pose(physics, position=new_pos)
        else:
            raise(f'Error in object_appear(): step_number {step_number}, step_appear {step_appear}, step_disappear {step_disappear}')

    if reset_position_freq > 0:
        if step_number > step_appear:
            if step_disappear is None or step_number < step_disappear:
                if np.mod(step_number, reset_position_freq) == 0:
                    print(f'JUMPING {agent} to: {start_pos} at step {step_number}')

                    new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
                    new_pos[:2] = np.clip(new_pos[:2], [-maze_size[0], -maze_size[1]], [maze_size[0], maze_size[1]])
                    walker.set_pose(physics, position=new_pos)



    action = np.array([0., 0.])
    return action

import matplotlib.pyplot as plt
np.random.seed(1)
def color_change(time_step,  physics,agent, action_spec, step_number, walker, rgb, period=10, do_random=0):
    # if step_number > 0:
    if step_number >= 0:
        if (step_number % period) == 0 and (step_number // period) % 2 == 1:
            if do_random:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = np.random.rand(3)
            else:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = rgb
        elif (step_number % period) == 0 and (step_number // period) % 2 == 0:
            if do_random:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = np.random.rand(3)
            else:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = walker._mjcf_root.find('texture', 'body').rgb1

    action = np.zeros(action_spec.shape)
    return action

def object_appear_and_color_change(time_step, physics, agent, action_spec, step_number, walker, step_appear, step_disappear, start_pos=[0., 0.], rgb=None, period=10, do_random=0):
    pos = time_step.observation['absolute_position_'+agent]
    ori = time_step.observation['absolute_orientation_'+agent]
    quaternion = time_step.observation['absolute_quaternion_'+agent]
    maze_size = time_step.observation['maze_size']
    if step_number == step_appear:
        new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
        new_pos[:2] = np.clip(new_pos[:2],[-maze_size[0], -maze_size[1]],[maze_size[0], maze_size[1]])
        walker.set_pose(physics, position=new_pos)
    if step_disappear is not None:
        if step_number == step_disappear:
            new_pos = np.array([-maze_size[0], -maze_size[1], pos[2]])
            walker.set_pose(physics, position=new_pos)
    if step_number >= 0:
        if (step_number % period) == 0 and (step_number // period) % 2 == 1:
            if do_random:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = np.random.rand(3)
            else:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = rgb
        elif (step_number % period) == 0 and (step_number // period) % 2 == 0:
            if do_random:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = np.random.rand(3)
            else:
                physics.named.model.geom_rgba[agent + '/shell'][:3] = walker._mjcf_root.find('texture', 'body').rgb1

    action = np.array([0., 0.])
    return action

def object_appear_and_color_change_collision(time_step, physics, agent, action_spec, step_number, walker, step_appear, step_disappear,
                                             start_pos=[0., 0.], do_random=0, primary_agent='agent0', last_collision_step=None,
                                             other_agents_to_change=None):
    pos = time_step.observation['absolute_position_'+agent]
    ori = time_step.observation['absolute_orientation_'+agent]
    quaternion = time_step.observation['absolute_quaternion_'+agent]
    maze_size = time_step.observation['maze_size']
    if step_number == step_appear:
        new_pos = np.array([start_pos[0], start_pos[1], pos[2]])
        new_pos[:2] = np.clip(new_pos[:2],[-maze_size[0], -maze_size[1]],[maze_size[0], maze_size[1]])
        walker.set_pose(physics, position=new_pos)
    if step_disappear is not None:
        if step_number == step_disappear:
            new_pos = np.array([-maze_size[0], -maze_size[1], pos[2]])
            walker.set_pose(physics, position=new_pos)


    contact_with_primary_agent = False
    for contact in physics.data.contact:
        if contact.geom1 == physics.named.model.geom_bodyid.axes.row.names.index(f'{primary_agent}/shell'):
            contact_with_primary_agent = True
            other_geom_id = contact.geom2
        elif contact.geom2 == physics.named.model.geom_bodyid.axes.row.names.index(f'{primary_agent}/shell'):
            contact_with_primary_agent = True
            other_geom_id = contact.geom1
        else:
            contact_with_primary_agent = False
            other_geom_id = None


    if contact_with_primary_agent:
        if other_geom_id == physics.named.model.geom_bodyid.axes.row.names.index(f'{agent}/shell'):
            if (step_number - last_collision_step[0]) > 2: # A form of debouncing
                physics.named.model.geom_rgba[agent + '/shell'][:3] = np.random.rand(3)
                if other_agents_to_change is not None:
                    for ii in other_agents_to_change:
                        physics.named.model.geom_rgba[ii + '/shell'][:3] = np.random.rand(3)

            last_collision_step[0] = step_number

    action = np.array([0., 0.])
    return action


def color_change_multi(time_step,  physics,agent, action_spec, step_number, walker, rgbs, period=10):
    ncolors = len(rgbs)
    if step_number >= 0:
        if (step_number % period) == 0:
            i = (step_number // period) % ncolors
            physics.named.model.geom_rgba[agent + '/shell'][:3] = rgbs[i]

    action = np.zeros(action_spec.shape)
    return action

def color_change_collision(time_step,  physics,agent, action_spec, step_number, walker, primary_agent, rgb=None, last_collision_step=None, period=2, do_random=0):
    """
    last_collision_step: must be an object that is passed by reference
    :return:
    """
    contact_with_primary_agent = False
    for contact in physics.data.contact:
        if contact.geom1 == physics.named.model.geom_bodyid.axes.row.names.index(f'{primary_agent}/shell'):
            contact_with_primary_agent = True
            other_geom_id = contact.geom2
        elif contact.geom2 == physics.named.model.geom_bodyid.axes.row.names.index(f'{primary_agent}/shell'):
            contact_with_primary_agent = True
            other_geom_id = contact.geom1
        else:
            contact_with_primary_agent = False
            other_geom_id = None


    if contact_with_primary_agent:
        if other_geom_id == physics.named.model.geom_bodyid.axes.row.names.index(f'{agent}/shell'):
            if (step_number - last_collision_step[0]) > 2: # A form of debouncing
                physics.named.model.geom_rgba[agent + '/shell'][:3] = np.random.rand(3)
            last_collision_step[0] = step_number

    action = np.zeros(action_spec.shape)
    return action


def ball_target(time_step,  physics, agent, action_spec, step_number):
    """Specify """
    pos = time_step.observation[f'absolute_position_{agent}']
    ori = time_step.observation[f'absolute_orientation_{agent}']
    vel = time_step.observation[f'{agent}/sensors_velocimeter']

    ### Okay