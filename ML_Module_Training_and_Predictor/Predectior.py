from ML_Module_Detection import Threat_Detection_Neural_Net
import numpy as np

def predict(parameters, x):

    A2, cache = Threat_Detection_Neural_Net.Main_Forward_propagation_Function(x, parameters)
    return Threat_Detection_Neural_Net.max_func(A2)
# testing the predict func # debugging

Prediction_Result = predict(Threat_Detection_Neural_Net.load_obj('Trained_NN_data'),np.array([[23,23,43]]))

#print(predict(Threat_Detection_Neural_Net.Final_Params,np.array([[23,23,43]])))

print(Prediction_Result)

print(Threat_Detection_Neural_Net.load_obj('Trained_NN_data'))