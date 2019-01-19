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
import json
import pickle
import codecs
import time
# import sklearn as skl
import matplotlib.pyplot as plt

Input_Data = np.asarray([[2.5,4.5,3.0,1.0,5.3,2.3,5.1,4.0,7.0,5.4,2.3]])
Test_Input = np.asarray([[2.2,3.5]])
Labels_of_Input_Data = np.asarray([[1,2,2,3,3,2,5,5,3,5,4]])

# Processing the Data


# Neural Network Model ---------------------------------------
# ---------------Neural Network Architecture---------------------
# Configuration of neural Network Architecture
learning_rate = Learning_Rate = .0004 # edit it as needed
num_iterations = no_of_Iteration = 3000 # edit to control the iteration count for the system
X = np.asarray(Input_Data) # Source Data
Y = np.asarray(Labels_of_Input_Data) # Source known result
Layers_Dimensions = np.asarray([X.shape[0],3,3,Y.shape[0]])  #First value is input and last is output and the middle values are hidden layers
Layer_Order = ['R','R','R','R','L']
# -------------------------------------------------

# Initialising the input parameters

def Initilize_params(Layers_Dimensions):

    # Initialize the hidden layer matrix values
    np.random.seed(3)  # to control the random values selection
    parameters_Hidden_Layer = {}
    L = len(Layers_Dimensions)
    for i in range(1, L):
        parameters_Hidden_Layer['W' + str(i)] = np.random.randn(Layers_Dimensions[i], Layers_Dimensions[i-1])*0.01
        parameters_Hidden_Layer['b' + str(i)] = np.zeros((Layers_Dimensions[i], 1))

        # analysing the dimensions and giving error of wrong dimension matrix
        assert parameters_Hidden_Layer['W' + str(i)].shape == (Layers_Dimensions[i],Layers_Dimensions[i-1])
        assert parameters_Hidden_Layer['b' + str(i)].shape == (Layers_Dimensions[i],1)

    ## Checking the dimension of the matrix raises error for some anamalyous behaviour
    parameters = parameters_Hidden_Layer
    return parameters
# Forward Propagation Function

# A-> Activation from prev layer,W-> Weight from prev layer,
# b-> bias from prev layer
def Linear_forward_prop(A,W,b):
    Z = np.dot(W,A) + b
    # checking the dimensions values
    #assert Z.shape[0] == (W.shape[0],A.shape[1])
    cache = (A,W,b)    # storing values for backward propagation
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
    dr = 1.0* (z > 0)  ## Relu issue[Check]
    #print(activation_cache * dr)                                         # REMOVE THESE AFTER DEBUG
    return dr

def dsigmoid(z,activation_cache):
    #print((activation_cache)*(sigmoid(z)[0]*(1 - sigmoid(z)[0])).shape)   # REMOVE THEIS AFTER DEBUG
    return sigmoid(z)[0]*(1 - sigmoid(z)[0])

def max_func(z):
    return np.floor(z/max(z))

#Function for storing and fetching file

def save_obj(obj, name):
    with open('./' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('./' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

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
    assert A.shape == (W.shape[0], A_prev.shape[1])
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

    AL, cache = Linear_Activation_forward(A, parameters['W'+str(L)], parameters['b'+str(L)],2)
    caches.append(cache)

    # Checking the dimension of result matrix
    assert AL.shape == (1, X.shape[1])
    return AL, caches

###-------------Defining the Cost Function-------------###

def compute_cost(AL,Y):  # Y is the input

    m = Y.shape[1]

    # Compute loss from aL and y.

    cost = -1 / m * np.sum(Y * np.log(AL) + (1 - Y) * (np.log(1 - AL)))  # Cost Function
    cost = np.squeeze(cost)
    # Checking the cost shape
    assert cost.shape == ()
    return cost

# Backward Propagation Function

def linear_backward(dZ, cache):

    A_prev, W, b = cache
    m = A_prev.shape[1]

    dW = 1 / m * (np.dot(dZ, A_prev.T))
    db = 1 / m * np.sum(dZ, axis=1, keepdims=True)
    dA_prev = np.dot(W.T, dZ)


## Checking the structure
    assert dA_prev.shape == A_prev.shape
    assert dW.shape == W.shape
    assert db.shape == b.shape

    return dA_prev, dW, db

# Linear Activation backward

def linear_activation_backward(dA, cache, activation):

    linear_cache, activation_cache = cache
    if activation == 2:

        dZ = dRelu(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)

    elif activation == 1:

        dZ = dsigmoid(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)

    return dA_prev, dW, db

# Main Linear Backward Model

def L_model_backward(AL, Y, caches):

    grads = {}
    L = len(caches)  # the number of layers
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)  # shaping Y as the  same shape as AL

    # Initializing the backpropagation


    dAL = -(np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))



    current_cache = caches[L - 1]
    grads["dA" + str(L - 1)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(dAL,current_cache,2)

    # Loop from l=L-2 to l=0
    for l in reversed(range(L - 1)):
        if Layer_Order[l] == 'S':
            activation = 1
        elif Layer_Order[l] == 'R':
            activation = 2
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads["dA" + str(L - 1)], current_cache, activation)
        grads["dA" + str(l)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp
        print('loop completed sucessfully ----->' + str(l))


    return grads

# Updating Parameters Helper Function

def update_parameters(parameters, grads, learning_rate):

    L = len(parameters) // 2  # number of layers in the neural network

    for l in range(1, L):
        parameters["W" + str(l )] = parameters['W' + str(l)] - learning_rate * (grads['dW' + str(l)])
        parameters["b" + str(l )] = parameters['b' + str(l)] - learning_rate * (grads['db' + str(l)])
    return parameters


## Training the NN Model Function

def Train_NN_Model(X, Y, Layers_Dimensions, learning_rate = 0.0075, num_iterations = 3000):
    np.random.seed(1)
    costs = []  # keep track of cost

    parameters = Initilize_params(Layers_Dimensions)

    # Loop (gradient descent)
    for i in range(0, num_iterations):


        AL, caches = Main_Forward_propagation_Function(X, parameters)

        # Compute cost.

        cost = compute_cost(AL, Y)

        # Backward propagation.

        grads = L_model_backward(AL, Y, caches)


        # Update parameters.

        parameters = update_parameters(parameters, grads, learning_rate)
    ## Storing the Trained N N Model

    #processing the dictionary and serializing it


    try:
        save_obj(parameters,'Trained_NN_data')
    except():
        print("Logs Cannot be generated")
    else:
        print("Logs Generated successfully")




    ##------------Debuger Code-------------------------------------------
    print('=================================================') #
    print(cost)                                                # Problem of division by zero and inf comming with real data check this part
    print('=================================================') #

    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()
    #---------------------Debug Code------------------------------#
    return parameters

# Calling the training module

#Final_Params = Train_NN_Model(X, Y, Layers_Dimensions, 0.0075, 30)           ## Debugger function
#print(Final_Params)




##--------------------------------------------------------------------