
import numpy as np
import pandas as pd
from ML_Module_Clustering.Multi_dimension_clustering_Algo import cluster_generation as MDCA
from ML_Module_Clustering.Multi_dimension_clustering_Algo import cluster_visualize as MDVA
from ML_Module_Detection.Threat_Detection_Neural_Net import Train_NN_Model as NTMA

# Data Sepration Function
def X_Y_segregator(dic1):
    X_inp = []
    Y_inp = []
    for i in dic1:
        for j in dic1[i]['Data_points']:
            X_inp.append(j)
            Y_inp.append(i)
    return X_inp,Y_inp


# Data connecton here
data = pd.read_csv("../Data_Set/CSV_Format/Cyber-Kali_Linux-data.csv")  # Conecting to the CSV File
df = pd.DataFrame(data)
X_data = []
for i in range(1,45):
    X_data.append(list(df.values[i]))

print(X_data) # DEBUG FUNCTION TO check the procesed data<-----------------------


X_data = [[233,231,234],[653,231,323],[342,323,122],[232,323,122],[323,221,323]] #<-------BACKUP DATA FOR TESTING ONLY

## Processing the Data points with the clustering algorithms
no_of_dims = len(X_data[1])

cluster_data, outliers, no_of_clusters= MDCA(no_of_dims,X_data)

########################
print(cluster_data)    #
print(outliers)        ################ Debug code for reading and analysis only<------------
print(no_of_clusters)  #
########################

## Visualization code un-comment to activate

MDVA(no_of_dims,cluster_data,outliers,no_of_clusters,['Reds'],1,X_data)
##------------------------------------------------------------

## Labeling the processed clusters

def cluster_labler(Y,labels):
    for i in range(len(labels)):
        for j in range(len(Y)):
            if(Y[j] == 'cluster-'+str(i+1)):
                Y[j] = labels[i]
    return Y
##--------------------------------



## Training the Neural Net Algorithm


############## Processing the Data ########################################
X ,Y = X_Y_segregator(cluster_data)
print(Y)

X = np.asarray(X)
labels = ['very_safe','safe','low_level_threat','medium_threat','risky_threat','high_risk_threat'] #Update as analysed
Y = np.asarray(cluster_labler(Y,labels))

##################Processing the data before feeding to N N Model##########

Layers_Dimensions = np.asarray([X.shape[0],5,5,Y.shape[0]])

#########
print(X)#
print(Y)################ Debug Code only
#########

#########################################################################################
X = np.asarray(np.asarray([[2.5,4.5,3.0,1.0,5.3,2.3,5.1,4.0,7.0,5.4,2.3]]))# Source Data#
Y = np.asarray(np.asarray([[1,2,2,3,3,2,5,5,3,5,4]])) # Source known result             ######## Debug Code
#########################################################################################
learning_rate = 0.0085
no_of_iterations = 30
Resultant_weights = NTMA(X, Y, Layers_Dimensions, learning_rate, no_of_iterations)

#debug code
print(Resultant_weights)#<-----------------------------------------------------------
