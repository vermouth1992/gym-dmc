from dm_control import suite
from gym.envs import register
from gym.envs.registration import EnvSpec
from gym.wrappers import TimeLimit


def make_env(flatten_obs=True, from_pixels=False, frame_skip=1, episode_frames=1000, **kwargs):
    assert episode_frames % frame_skip == 0
    max_episode_steps = episode_frames // frame_skip

    from gym_dmc.dmc_env import DMCEnv
    env = DMCEnv(from_pixels=from_pixels, frame_skip=frame_skip, **kwargs)

    # This spec object gets picked up by the gym.EnvSpecs constructor
    # used in gym.registration.EnvSpec.make, L:93 to generate the spec

    if from_pixels:
        from gym_dmc.wrappers import ObservationByKey
        env = ObservationByKey(env, "pixels")
    elif flatten_obs:
        from gym_dmc.wrappers import FlattenObservation
        env = FlattenObservation(env)

    env = TimeLimit(env, max_episode_steps=max_episode_steps)
    return env


for domain_name, task_name in suite.ALL_TASKS:
    ID = f'{domain_name.capitalize()}-{task_name}-v1'
    register(id=ID,
             entry_point='gym_dmc:make_env',
             kwargs=dict(
                 domain_name=domain_name,
                 task_name=task_name,
                 channels_first=True,
                 width=84,
                 height=84,
                 frame_skip=1),
             )

DMC_IS_REGISTERED = True
