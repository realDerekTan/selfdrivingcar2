import os
import tensorflow as tf
from rl_model import RlModel

batch_update_frequency = 10
max_epoch_runtime_sec = 30
per_iter_epsilon_reduction = 0.003
min_epsilon = 0.1
batch_size = 32

replay_memory_size = 50
weights_path = os.path.join(os.getcwd(), '/pretrain_model_weights.h5')
train_conv_layers = 'false'
airsim_path = 'C:\\Derek\\TKS\\AirSim\\AD_Cookbook_AirSim\\'
data_dir = os.path.join(os.getcwd(), 'Share')
experiment_name = 'local_run'

train_cmd = 'python distributed_agent.py'
train_cmd += ' batch_update_frequency={0}'.format(batch_update_frequency)
train_cmd += ' max_epoch_runtime_sec={0}'.format(max_epoch_runtime_sec)
train_cmd += ' per_iter_epsilon_reduction={0}'.format(per_iter_epsilon_reduction)
train_cmd += ' min_epsilon={0}'.format(min_epsilon)
train_cmd += ' batch_size={0}'.format(batch_size)
train_cmd += ' replay_memory_size={0}'.format(replay_memory_size)
train_cmd += ' weights_path={0}'.format(weights_path)
train_cmd += ' train_conv_layers={0}'.format(train_conv_layers)
train_cmd += ' airsim_path={0}'.format(airsim_path)
train_cmd += ' data_dir={0}'.format(data_dir)
train_cmd += ' experiment_name={0}'.format(experiment_name)
train_cmd += ' local_run=true'

TRAINING_BATCH_FILE = 'Share/scripts_downpour/app/train.bat'

if not tf.gfile.Exists(TRAINING_BATCH_FILE):
	tf.gfile.MakeDirs(TRAINING_BATCH_FILE)

with open(os.path.join(os.getcwd(), 'Share\\scripts_downpour\\app\\train.bat'), 'w') as f:
	f.write(train_cmd)
