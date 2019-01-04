'''
NOTES:-
Neural Network Model Iteration -1
Threat Detection Model
To Analyse Computer Log Data for Threat Detection
Author :- Ankit yadav
Cyber-Shield
'''

# Importing Packages

import numpy as np
import sklearn as skl

## Neural Network Model ---------------------------------------

# Configuration of neural Network Architecture

def Neural_network_Architecture(input_size_x,Hidden_Layer_size,output_layer_size_y):
    x_size = input_size_x.shape[0]                                                    ## Pulling in the input data size values
    y_size = output_layer_size_y.shape[1]                                             ## pulling the values for the label dimension
    return (x_size,Hidden_Layer_size,y_size)



