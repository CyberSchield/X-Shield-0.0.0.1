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

# Neural Network Model ---------------------------------------
# ---------------Neural Network Architecture---------------------
# Configuration of neural Network Architecture
X = Input_Data # Source Data
Y = Labels_of_Input_Data # Source known result
Layers_Dimensions = [X.shape[1],3,4,Y.shape[1]]  #First value is input and last is output and the middle values are hidden layers
Layer_Order = ['S','R','R','R','L']
# -------------------------------------------------

# Initialising the input parameters

def Initilize_params(Layers_Dimensions):

    # Initialize the hidden layer matrix values
    np.random.seed(3)  # to control the random values selection
    parameters_Hidden_Layer = {}
    L = len(Layers_Dimensions)
    for i in range(1, L):
        parameters_Hidden_Layer['Wx' + str(i)] = np.random.randn(Layers_Dimensions[i], Layers_Dimensions[i-1])*0.01
        parameters_Hidden_Layer['Bx' + str(i)] = np.zeros((Layers_Dimensions[i], 1))

        # analysing the dimensions and giving error of wrong dimension matrix
        assert (parameters_Hidden_Layer['Wx' + str(i)].shape == (parameters_Hidden_Layer[i]),parameters_Hidden_Layer[i-1])
        assert (parameters_Hidden_Layer['Bx' + str(i)].shape == (parameters_Hidden_Layer[i]),1)

    ## Checking the dimension of the matrix raises error for some anamalyous behaviour
    parameters = parameters_Hidden_Layer
    return parameters
# Forward Propagation Function

# A-> Activation from prev layer,W-> Weight from prev layer,
# b-> bias from prev layer
def Linear_forward_prop(A,W,b):
    Z = np.dot(W,A) + b
    # checking the dimensions values
    assert (Z.shape == (W.shape[0],A.shape[1]))
    cache = (A,W,b)    # stroting values for backward propagation
    return Z,cache

## Creating the Sigmoid Helper Function
def sigmoid(z):
    s = 1/(1+np.exp(-z))
    return s,z
## Creating Relu Helper Function
def Relu(z):
    r = z * (z > 0)
    return (r,z)

def dRelu(z,activation_cache):
    dr = 1. * (z > 0)
    return activation_cache*dr,z

def dsigmoid(z,activation_cache):
    return activation_cache*(sigmoid(z)[0]*(1 - sigmoid(z)[0]))

def max_func(z):
    return np.floor(z/max(z))

def Linear_Activation_forward(A_prev, W , b , activation): ## activation = 1[Sigmoid] , 2[Relu]

    if activation == 1:
        Z,linear_cache = Linear_forward_prop(A_prev, W , b)
        A,activation_cache = sigmoid(Z)

    elif activation == 2:
        Z,linear_cache = Linear_forward_prop(A_prev,W,b)
        A, activation_cache = Relu(Z)
    elif activation == 0:
        Z, linear_cache = Linear_forward_prop(A_prev, W, b)
        A, activation_cache = max_func(Z)

    # Checking the matrix dimensions
        assert (A.shape == (W.shape[0], A_prev.shape[1]))
        cache = (linear_cache, activation_cache)

        return  A, cache
# Main consolidated forward propagation function
def Main_Forward_propagation_Function(X,parameters):
    activation = 0
    caches = []
    A = X
    L = len(parameters) // 2
    for i in range(1,L):
        if Layer_Order[i] == 'S':
            activation = 1
        elif Layer_Order[i] == 'R':
            activation = 2
        A_prev = A
        A, cache = Linear_Activation_forward(A_prev, parameters['W' + str(i)], parameters['b' + str(i)], activation)
        caches.append(cache)

        # implementing the final result layer

    AL, cache = Linear_Activation_forward(A, parameters['W'+str(L)], parameters['b'+str(L)],0)
    caches.append(cache)

    # Checking the dimension of result matrix
    assert (AL.shape == (1, X.shape[1]))
    return AL, caches

###-------------Defining the Cost Function-------------###

def compute_cost(AL,Y):  # Y is the input

    m = Y.shape[1]

    # Compute loss from aL and y.

    cost = -1 / m * np.sum(Y * np.log(AL) + (1 - Y) * (np.log(1 - AL)))  # Cost Function
    cost = np.squeeze(cost)
    # Checking the cost shape
    assert (cost.shape == ())

    return cost

# Backward Propagation Function

def linear_backward(dZ, cache):

    A_prev, W, b = cache
    m = A_prev.shape[1]

    dW = 1 / m * (np.dot(dZ, A_prev.T))
    db = 1 / m * np.sum(dZ, axis=1, keepdims=True)
    dA_prev = np.dot(W.T, dZ)

## Checking the structure
    assert (dA_prev.shape == A_prev.shape)
    assert (dW.shape == W.shape)
    assert (db.shape == b.shape)

    return dA_prev, dW, db


def linear_activation_backward(dA, cache, activation):

    linear_cache, activation_cache = cache

    if activation == 1:

        dZ = dRelu(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)

    elif activation == 2:

        dZ = dsigmoid(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)

    return dA_prev, dW, db




