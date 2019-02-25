# selfdrivingcar2
In this project, I use reinforcement learning to train a self driving car in AirSim. This model's framework is based off of the cookbook made on AirSim. 

# Navigation
** rl_model.py ** The raw model for reinforcement learning. The machine learning and CNN portion of the project is located in this file.

** trainRLmodel.py ** This is the script you need to run if you want to train the model.

** airsim_client.py ** This file includes many of the commands we use in distributed_agent.py so we can connect our results to the AirSim client.

** distributed_agent.py ** This file converts the results of our decision-making neural net into executable commands in the AirSim environment.

** Generator.py ** This file is used to generate additional data for our model to train upon.

** pretrain_model_weights.h5 ** Usually, this model would take days to train. Using preloaded weights for our model, the training converges after a couple of hours. 
