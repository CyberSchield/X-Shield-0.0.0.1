from Threat_Detection_Neural_Net import Final_Params as params
from Threat_Detection_Neural_Net import Main_Forward_propagation_Function
from Threat_Detection_Neural_Net import max_func
import numpy as np

def predict(parameters, x):

    A2, cache = Main_Forward_propagation_Function(x, parameters)
    return max_func(A2)
# testing the predict func
print(predict(params,np.array([[23,23,43]])))