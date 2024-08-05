import numpy as np
import matplotlib.pyplot as plt
import os

from algorithm import make_dir
# mlt.style.use("ggplot")


density_array= [0.3, 0.7, 1] 
density_array= [np.round(i,2) for i in density_array]

team_array_types= [np.array([10,10]), np.array([10,8]), np.array([10,6]),np.array([10,4]) ,np.array([10,2]), np.array([10])]

colors= ["blue", "red", "green", "pink", "yellow", "cyan", "grey"]
for iterant in range(len(team_array_types)):
    team_array= team_array_types[iterant]
    third_team_size= 5- iterant
    wd= os.getcwd()
    dir_to_store= wd+ "\\data_storage\\store_iter_data_team_size_"+str(team_array)+"\\"
    make_dir(dir_to_store)
    os.chdir(dir_to_store)
    print(team_array, dir_to_store)
    precision=[]
    recall_array=[]

    for density in density_array:
        os.chdir(dir_to_store)
        array= np.load("data_itersort_"+str(density)+".npy")

        fn_array=[sum(array[:,0][100*i:100*(i+1)]) for i in range(0,10)]
        fp_array=[sum(array[:,1][100*i:100*(i+1)]) for i in range(0,10)]
        tp_array=[sum(array[:,2][100*i:100*(i+1)]) for i in range(0,10)]
        precision_array=[tp_array[i]/(tp_array[i]+fn_array[i]) for i in range(0,10)]
        print(precision_array)
        os.chdir(wd)

        for i in range(0,10):
            plt.scatter(density, precision_array[i], color=colors[iterant], alpha=0.4)
        precision.append(np.mean(precision_array))
    plt.plot(density_array, precision, label= team_array, color=colors[iterant])
    os.chdir(wd)
plt.legend()
plt.xlabel("density")
plt.ylabel("recall")
plt.ylim(0.0, 1.05)
plt.title("varied density and third team size reduction effect on accuracy")
plt.show()
    



    