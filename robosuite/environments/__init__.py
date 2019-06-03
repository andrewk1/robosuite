import sys
sys.path.append('.')
sys.path.append('./roboturk_sim2real')
sys.path.append('./roboturk_sim2real/models')
sys.path.append('./roboturk_sim2real/options')

from .base import REGISTERED_ENVS, MujocoEnv
from .roboturk_sim2real import *

ALL_ENVS = REGISTERED_ENVS.keys()
