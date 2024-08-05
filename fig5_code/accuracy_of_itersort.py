'''calculating accuracy of algorithm over a wide range of arrays'''

import numpy as np
import pandas as pd
import os

import algorithm as alg
from algorithm import make_dir
import create_matrix as cm

# enter range of densities
density_array= [0.3, 0.7, 1] 
density_array= [np.round(i,2) for i in density_array] 

# enter team arrays
team_array_types= [np.array([10,10]), np.array([10,8]), np.array([10,6]),np.array([10,4]) ,np.array([10,2]), np.array([10])] 

# enter directory to store information
wd= os.getcwd() #change it as required

store_adj= {}

for iterant in range(len(team_array_types)):
    team_array= team_array_types[iterant]

    dir_to_store= wd+ "\\data_storage\\store_iter_data_team_size_"+str(team_array)+"\\"
    make_dir(dir_to_store)
    os.chdir(dir_to_store)

    for density in density_array:
        density_matrix= np.ones(shape= (team_array.size, team_array.size)) * density
        df= pd.DataFrame(columns=["sl no","ground truth", "prediction", "true positive", "false positive", "false negative", "eigenvector"])
        df["sl no"]= np.arange(0,1000)
        array_confusion=[]
        for i in range(1000):
            Adj, array_ranges= cm.generate_n_team_matrix_sparse(team_array= team_array, density_matrix= density_matrix)
            array_team_nodes= array_ranges[:-1]
            array_team_nodes=[list(i) for i in array_team_nodes]
            array_pred=alg.iteratively_perform_sort(Adj)
            array_pred= [i for i in array_pred if len(i)!=0]

            true_positive= [i for i in array_team_nodes if i in array_pred]
            false_positive=[i for i in array_pred if i not in array_team_nodes]
            false_negative=[i for i in array_team_nodes if i not in array_pred]

            df["ground truth"][i]= str(array_team_nodes)
            df["prediction"][i]= str(array_pred)
            df["true positive"][i]= str(true_positive)
            df["false positive"][i]= str(false_positive)
            df["false negative"][i]= str(false_negative)
            df["eigenvector"][i]= str(np.linalg.eig(Adj)[1].T[0])
    
            array_confusion.append([len(false_negative), len(false_positive), len(true_positive)])

        np.save("data_itersort_"+str(density), np.array(array_confusion))   
        df.to_csv("data_itersort_"+str(density)+".csv")
    os.chdir(wd)