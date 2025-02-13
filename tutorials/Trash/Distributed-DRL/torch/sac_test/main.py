import ray

from configparser import ConfigParser
from argparse import ArgumentParser

# from run_algorithm import run_apex, run_dppo, run_a3c, run_impala
import run
from utils.utils import Dict
parser = ArgumentParser('parameters')

parser.add_argument("--env_name", type=str, default = 'CartPole-v1', help = 'environment to adjust (default : CartPole-v1)')
parser.add_argument("--algo", type=str, default = 'apex', help = 'algorithm to adjust (default : a3c)')
parser.add_argument('--epochs', type=int, default=100000, help='number of epochs, (default: 5000)')
parser.add_argument('--num_actors', type=int, default=3, help='number of actors, (default: 3)')
parser.add_argument('--test_repeat', type=int, default=10, help='test repeat for mean performance, (default: 10)')
parser.add_argument('--test_sleep', type=int, default=3, help='test sleep time when training, (default: 3)')
parser.add_argument("--use_cuda", type=bool, default = True, help = 'cuda usage(default : True)')
parser.add_argument('--tensorboard', type=bool, default=True, help='use_tensorboard, (default: False)')
args = parser.parse_args()

##Algorithm config parser
parser = ConfigParser()
parser.read('config.ini')
agent_args = Dict(parser, args.algo) 

#ray init
ray.init()
if args.algo == 'apex' :
    run.run(args, agent_args)
