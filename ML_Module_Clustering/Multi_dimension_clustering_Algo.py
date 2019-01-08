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
import matplotlib.patches as mpatches
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib as mpl
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
def plot_cluster(dimension_Dict,label,color):
    mpl.rcParams['legend.fontsize'] = 10
    ax = plt.axes(projection='3d')
    zdata = dimension_Dict['dimension-3']
    xdata = dimension_Dict['dimension-2']
    ydata = dimension_Dict['dimension-1']
    ax.scatter3D(xdata, ydata, zdata, c=zdata,label = label, cmap= color);
    ax.legend()
    plt.show()
plot_cluster(dimension_Dict,'Data_Plot','Blues')
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
    lis3 = []
    lis4 = []
    lis5 = []
    lis6 = []
    empdic = {}
    for i in point_metadata.keys():
        lis1.append(i)
        lis2.append(point_metadata[i]['Neighbour Count'])
        lis3.append(point_metadata[i]['Points'])
        lis4.append(point_metadata[i]['Centroid'])
        lis5.append(point_metadata[i]['value'])
        lis6.append(point_metadata[i]['Clustered'])
    for l in range(len(lis1)):
        for j in range(len(lis2)):
            if lis2[l] > lis2[j]:  #swapping values
                tmp = lis2[l]
                tmp2 = lis1[l]
                tmp3 = lis3[l]
                tmp4 = lis4[l]
                tmp5 = lis5[l]
                tmp6 = lis6[l]
                lis2[l] = lis2[j]
                lis1[l] = lis1[j]
                lis3[l] = lis3[j]
                lis4[l] = lis4[j]
                lis5[l] = lis5[j]
                lis6[l] = lis6[j]
                lis2[j] = tmp
                lis1[j] = tmp2
                lis3[j] = tmp3
                lis4[j] = tmp4
                lis5[j] = tmp5
                lis6[j] = tmp6

    for a in range(len(lis1)):
        empdic[lis1[a]] = {}
        empdic[lis1[a]]['Neighbour Count'] = lis2[a]
        empdic[lis1[a]]['Points'] = lis3[a]
        empdic[lis1[a]]['Centroid'] = lis4[a]
        empdic[lis1[a]]['value'] = lis5[a]
        empdic[lis1[a]]['Clustered'] = lis6[a]
    return empdic,lis2,lis4
# 3. Z Score calculator function
def ZScore(point_Value,cluster_metadata_list):
    neighbour_count_list = np.array(cluster_metadata_list)
    n = len(cluster_metadata_list)
    sum1 = np.sum(neighbour_count_list)
    mean_of_data = sum1/n
    sum_of_square = np.sum(np.power((neighbour_count_list - mean_of_data),2))
    variance = sum_of_square/(n-1)
    std  = math.sqrt(variance)
    Z = (point_Value - mean_of_data)/std
    return Z

# 4. Centroid Calculator
def centroid_calc(no_of_dims,list_val):
    dims = ext_dim(no_of_dims,list_val)
    centroid = []
    for i in range(no_of_dim):
        centroid.append(sum(dims['dimension-' + str(i+1)])/len(dims['dimension-' + str(i+1)]))
    return centroid
def neighbour_Density_calculator(no_of_dim,X,radius_increment_val):
    point_metadata = {}
    max_radius = 0
    Non_cut_off_condition = True
    # initialising an empty dictionary with keys
    for i in range(len(X)):
        point_metadata['point-' + str(i)] = {}
        point_metadata['point-' + str(i)]['value'] = X[i]
        point_metadata['point-' + str(i)]['Neighbour Count'] = 0
        point_metadata['point-' + str(i)]['Points'] = []
        point_metadata['point-' + str(i)]['Centroid'] = X[i]
        point_metadata['point-' + str(i)]['Clustered'] = False
    while(Non_cut_off_condition):
        for i in range(len(X)):
            val = 0
            for a in X:
                if X[i] == a: # Prevent calculating Euclidean distance for same points
                    continue
                if Euclidean_Distance_Calc(no_of_dim,X[i],a) < max_radius :
                    val = val + 1
                    point_metadata['point-' + str(i)]['Neighbour Count'] = val
                    point_metadata['point-' + str(i)]['Points'].append(a)
                    print( Euclidean_Distance_Calc(no_of_dim,X[i],a),'|',max_radius,val) #<-------------------------------------

        for k in range(len(X)):
            if (point_metadata['point-' + str(k)]['Neighbour Count']/len(X))*100 > 10 :
                Non_cut_off_condition = False
            else:
                max_radius = max_radius + radius_increment_val
    return sort_cluster_density(point_metadata)

# Cluster formation and centroid calculation
def cluster_generation(no_of_dim,X):
    Initial_cluster_no = 0
    outliers = []
    cluster_list = {}
    point_metadata, cluster_metadata__list , label_metadata = neighbour_Density_calculator(no_of_dim, X, .1)
    #Initial_centroid = cluster_metadata__list[0]
    for i in point_metadata.keys():
        Initial_cluster_no +=1
        cluster_list['cluster-' + str(Initial_cluster_no)] = {}
        cluster_list['cluster-' + str(Initial_cluster_no)]['Data_points'] = []
        cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid'] = point_metadata[i]['value']
        for j in point_metadata.keys():
            if(point_metadata[i]['Clustered'] == True):
                ttp = cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid']
                ppt = point_metadata[j]['value']
                ptp = point_metadata[j]['Centroid']
                if(Euclidean_Distance_Calc(no_of_dim,ttp,ppt) < Euclidean_Distance_Calc(no_of_dim,ptp,ppt)):
                    cluster_list['cluster-' + str(Initial_cluster_no)]['Data_points'].append(point_metadata[j]['value'])
                    cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid'] = centroid_calc(no_of_dim,cluster_list['cluster-' + str(Initial_cluster_no)]['Data_points'])
                    point_metadata[j]['Clustered'] = True
                    point_metadata[j]['Centroid'] = cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid']
            else:
                if point_metadata[j]['value'] in point_metadata[i]['Points']:
                    cluster_list['cluster-' + str(Initial_cluster_no)]['Data_points'].append(point_metadata[j]['value'])
                    cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid'] = centroid_calc(no_of_dim,cluster_list['cluster-' + str(Initial_cluster_no)]['Data_points'])
                    point_metadata[j]['Clustered'] = True
                    point_metadata[j]['Centroid'] = cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid']
                elif ZScore(point_metadata[j]['Neighbour Count'], cluster_metadata__list) < ZScore(point_metadata[i]['Neighbour Count'], cluster_metadata__list):
                    cluster_list['cluster-' + str(Initial_cluster_no)]['Data_points'].append(point_metadata[j]['value'])
                    cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid'] = centroid_calc(no_of_dim,cluster_list['cluster-' + str(Initial_cluster_no)]['Data_points'])
                    point_metadata[j]['Clustered'] = True
                    point_metadata[j]['Centroid'] = cluster_list['cluster-' + str(Initial_cluster_no)]['Centroid']
        if not cluster_list['cluster-' + str(Initial_cluster_no)]:
            del cluster_list['cluster-' + str(Initial_cluster_no)]
            Initial_cluster_no -= 1

    for i in point_metadata.keys():
        if(point_metadata[i]['Clustered'] == False):
            outliers.append(point_metadata[i]['value'])
    return cluster_list,outliers,Initial_cluster_no

# Visualising the clusters function

def cluster_visualize(no_of_dim,cluster_list,outliers,no_of_cluster,color_list): # Fix the colour schemes for the code
    #color = ["Blues","Greens","Reds"]
    for i in range(no_of_cluster):
        dimension_Dict = ext_dim(no_of_dim, cluster_list['cluster-'+str(i+1)]['Data_points'])
        plot_cluster(dimension_Dict, "Cluster - " + str(i+1), "Greens")

    dimension_Dict1 = ext_dim(no_of_dim, outliers)
    plot_cluster(dimension_Dict1, "Outliers", "Blues")








## Testing the code <-------------------------------Remove------------------------
a,b ,c= cluster_generation(no_of_dim,X)
print(a)
print(b)
print("No of Clusters =" + str(c))
cluster_visualize(no_of_dim,a,b,c,['Reds'])

