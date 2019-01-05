"""
NOTES :-
Master Clustering Module Iteration - 1
Clustering Technique under Implementation is [Unknown Algo Based on "Unsupervised clustering algorithm for N-dimensional
data" Author :- "Erwin B. Montgomery Jr.a,b,∗, He Huanga, Amir Assadic,d]"
Author:- Ankit Yadav [15SCSE101296]
Cyber-Shield
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
# Control panel
no_of_dim = 4
# Sample Data Points in 4 D
X = [[1,5,6,2],[1,2,1,3],[12,13,14,13],[22,23,21,24]]

# Dimension Values extractor Function
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

ax = plt.axes(projection='3d')
zdata = dimension_Dict['dimension-3']
xdata = dimension_Dict['dimension-2']
ydata = dimension_Dict['dimension-1']
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
plt.show()