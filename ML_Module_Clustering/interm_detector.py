from ML_Module_Clustering.Multi_dimension_clustering_Algo import cluster_generation as clust_generate
from ML_Module_Clustering.Multi_dimension_clustering_Algo import load_obj as load
from ML_Module_Clustering.Multi_dimension_clustering_Algo import save_obj as save
from ML_Module_Clustering.Multi_dimension_clustering_Algo import no_of_dim as n
from ML_Module_Clustering.Multi_dimension_clustering_Algo import X as x
import random
def predictor(test_val):
    X = []
    flag = 0
    value_range = 400
    X.append(random.sample(range(value_range), 4))
    print(X)
    test_val = X[0]

    cluster_list, outliers, cluster_count = clust_generate(n, x)
    save(cluster_list, 'Trained_clustering_data.pkl')
    save(outliers, 'Trained_clustering_outliers')
    save(cluster_count, 'Trined_clustering_no_of_clusters')

    cluster_list1 = load('Trained_cLustering_data')
    for i in range(5):
        print(i)
        dis1 = cluster_list['cluster-' + str(i + 1)]['Centroid'][0] - test_val[0]
        dis2 = cluster_list['cluster-' + str(i + 1)]['Centroid'][1] - test_val[1]
        dis3 = cluster_list['cluster-' + str(i + 1)]['Centroid'][2] - test_val[2]
        dis4 = cluster_list['cluster-' + str(i + 1)]['Centroid'][3] - test_val[3]
        print(dis1)
        print(dis2)
        print(dis3)
        print(dis4)
        val = abs(dis1) + abs(dis2) + abs(dis3) + abs(dis4)
        print(val)
        if dis1 in range(-50,50) and dis2 in range(-50,50) and dis3 in range(-50,50) and dis4 in range(-50,50):
            flag = 0
            return 'cluster-' + str(i+1)
        else:
            if(abs(val) < 200):
                flag = 0
                return 'cluster-' + str(i + 1)
            else:
                flag = 1

    if flag == 1:
        print('not found')
        return 'not_found'



