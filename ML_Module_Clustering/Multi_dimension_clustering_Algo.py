"""
NOTES :-
Master Clustering Module Iteration - 1
Clustering Technique under Implementation is [Unknown Algo Based on "Unsupervised clustering algorithm for N-dimensional
data" Author :- "Erwin B. Montgomery Jr.a,b,∗, He Huanga, Amir Assadic,d]"
Author:- Ankit Yadav [15SCSE101296]
Cyber-Shield
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# Control panel
no_of_dim = 4
# Sample Data Points in 4 D
X = [[25,15,10,12],[21,12,8,13],[12,13,14,13],[22,23,21,24],[19,18,20,11],[11,15,19,24],[16,13,17,15]]

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

# Step 1 Calculating the Euclidean Distance or no of neighbours

# helper functions
# 1. Euclidean distance calculation function
def Euclidean_Distance_Calc(no_of_dim,pt1,pt2):
    sum = 0
    for i in range(no_of_dim):
        sum = sum + pow((pt1[i] - pt2[i]),2)
    return math.sqrt(sum)


def neighbour_Density_calculator(no_of_dim,X,radius_increment_val):
    point_metadata = {{}}
    max_radius = 0
    Non_cut_off_condition = True

    while(Non_cut_off_condition):
        for i in range(len(X)):
            for a in X - X[i]:
                val = 0
                point_metadata['point-' + str(i)]['Values'] = X[i]
                if Euclidean_Distance_Calc(no_of_dim,X[i],a) < max_radius :
                    point_metadata['point-' + str(i)]['Neighbour Count'] = val + 1
        for k in range(len(X)):
            if (point_metadata['point-' + str(i)]['Neighbour Count']/len(X))*100 > 10 :
                Non_cut_off_condition = False
                break
            else:
                max_radius + radius_increment_val
                Non_cut_off_condition = True
    return point_metadata





# Graph plooting and analysis tool
def plot_cluster(dimension_Dict):
    ax = plt.axes(projection='3d')
    zdata = dimension_Dict['dimension-3']
    xdata = dimension_Dict['dimension-2']
    ydata = dimension_Dict['dimension-1']
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
    plt.show()
plot_cluster(dimension_Dict)

