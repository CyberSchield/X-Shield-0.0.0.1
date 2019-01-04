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

def Neural_network_Architecture(input_size_x,Hidden_Layer_size,Hidden_Layer_No,output_layer_size_y):
    x_size = input_size_x.shape[0]                                                    ## Pulling in the input data size values
    y_size = output_layer_size_y.shape[1]                                             ## pulling the values for the label dimension
    return (x_size,Hidden_Layer_size,Hidden_Layer_No,y_size)


# Initialising the input parameters

def Initilize_params(x_size,Hidden_Layer_size,Hidden_layer_No,y_size):
    Wx = np.random.randn(Hidden_Layer_size,x_size,Hidden_layer_No)*0.01 # Initialising the weight matrix for the data
    Bx = np.zeros((Hidden_Layer_size,1,Hidden_layer_No)) # initialising the bias matrix for the data

    Wy = np.random.randn(y_size,Hidden_Layer_size)*0.01 # initialising the weight matrix of label portion
    By = np.zeros((y_size,1))

    ## Checking the dimension of the matrix raises error for some anamalyous behaviour

    assert (Wx.shape == (Hidden_Layer_size, x_size,Hidden_layer_No))
    assert (Bx.shape == (Hidden_Layer_size, 1,Hidden_layer_No))
    assert (Wy.shape == (y_size, Hidden_Layer_size))
    assert (By.shape == (y_size, 1))

    parameters = {"Wx": Wx, "bx": Bx, "Wy": Wy, "by": By}
    return parameters

c = Initilize_params(2,4,3,3)
print(c)