"""
NOTES :-
Master Clustering Module Iteration - 1
Clustering Technique under Implementation is [Unknown Algo Based on "Unsupervised clustering algorithm for N-dimensional
data" Author :- "Erwin B. Montgomery Jr.a,b,∗, He Huanga, Amir Assadic,d]"
Author:- Ankit Yadav [15SCSE101296]
Cyber-Shield
"""
#-------------------------------------------------------Random Data Generation Code------------------------------
import random
value_range = 400
sample_size = 1000
X=[]
for i in range (sample_size):
    X.append(random.sample(range(value_range), 4))
print(X)
#-------------------------------------------------------Random Data Generation Code -----------------------------
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# Control panel
no_of_dim = 4
# Sample Data Points in 4 D
#X = [[25,15,10,12],[21,12,8,13],[12,13,14,13],[22,23,21,24],[19,18,20,11],[11,15,19,24],[16,13,17,15],[16.4,13.2,17.2,2,15.1]]
# Dimension Values extraction Function
def ext_dim(no_of_dim,X):
    dim_dict = {}
    temp_lis = []
    for i in range(no_of_dim):
        for j in range(len(X)):
            temp_lis.append(X[j][i])
        dim_dict['dimension-' + str(i+1)] = temp_lis[:]
        del temp_lis[:]  # Emptying the list again
    return dim_dict

dimension_Dict = ext_dim(no_of_dim,X) # Segeregating the multi dimension values


# Debug Code:---------------------------------------------------------------------------------------
print(dimension_Dict)
# --------------------------------------------------------------------------------------------------

# Graph plotting and analysis tool
def plot_cluster(dimension_Dict):
    ax = plt.axes(projection='3d')
    zdata = dimension_Dict['dimension-3']
    xdata = dimension_Dict['dimension-2']
    ydata = dimension_Dict['dimension-1']
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
    plt.show()
plot_cluster(dimension_Dict)
# Step 1 Calculating the Euclidean Distance or no of neighbours

# helper functions
# 1. Euclidean distance calculation function
def Euclidean_Distance_Calc(no_of_dim,pt1,pt2):
    sum = 0
    for i in range(no_of_dim):
        sum = sum + pow((pt1[i] - pt2[i]),2)
    return math.sqrt(sum)
# 2. Cluster density Sorter
def sort_cluster_density(point_metadata):
    lis1 = []
    lis2 = []
    empdic = {}
    for i in point_metadata.keys():
        lis1.append(i)
        lis2.append(point_metadata[i]['Neighbour Count'])
    for l in range(len(lis1)):
        for j in range(len(lis2)):
            if lis2[l] > lis2[j]:  #swapping values
                tmp = lis2[l]
                tmp2 = lis1[l]
                lis2[l] = lis2[j]
                lis1[l] = lis1[j]
                lis2[j] = tmp
                lis1[j] = tmp2

    for a in range(len(lis1)):
        empdic[lis1[a]] = {}
        empdic[lis1[a]]['Neighbour Count'] = lis2[a]
    return empdic
# 3. Z Score calculator function
def ZScore():
    pass


def neighbour_Density_calculator(no_of_dim,X,radius_increment_val):
    point_metadata = {}
    max_radius = 0
    Non_cut_off_condition = True
    # initialising an empty dictionary with keys
    for i in range(len(X)):
        point_metadata['point-' + str(i)] = {}
        point_metadata['point-' + str(i)]['Neighbour Count'] = 0
    while(Non_cut_off_condition):
        for i in range(len(X)):
            val = 0
            for a in X:
                if X[i] == a: # Prevent calculating Euclidean distance for same points
                    continue
                if Euclidean_Distance_Calc(no_of_dim,X[i],a) < max_radius :
                    val = val + 1
                    point_metadata['point-' + str(i)]['Neighbour Count'] = val
                    print( Euclidean_Distance_Calc(no_of_dim,X[i],a),'|',max_radius,val) #<-------------------------------------

        for k in range(len(X)):
            if (point_metadata['point-' + str(k)]['Neighbour Count']/len(X))*100 > 10 :
                Non_cut_off_condition = False
            else:
                max_radius = max_radius + radius_increment_val
                #print(max_radius)#<-------------------------------------------------------------Remove
    return sort_cluster_density(point_metadata)

## Testing the code <-------------------------------Remove------------------------
a = neighbour_Density_calculator(no_of_dim,X,.1)

print(a) #<----------------------------

