import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
import datetime
import boolean_smil
import state_classification as fsc
from scipy import stats 

plt.style.use("ggplot")


den=0.3

teamsize=[]
mean_frust=[]
pure_percent=[]
frust_error=[]
mean_frust_error=[]


networks=[["Size","Adj"]]
FigData=[["MeanFrust","Std","ThirdTeamSize"]]
FrustDist=[["FrustDist","ThirdTeamSize"]]

frust_distributions=[]

for i in range(1,25):
    teamsize.append(i)
    for j in range(0,50):

    
        adj=nteams.nteam_net(3,[5,5,i],[[den,den,den],[den,den,den],[den,den,den]])[0]
        networks.append([i,adj])

        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)

        data= frustration.ensemble_frustration(steadys,adj)
        frust_distributions.append(data)
        FrustDist.append([data,i])

    mean_frust.append(np.mean(data))
    mean_frust_error.append(np.std(data))
    FigData.append([mean_frust,mean_frust_error,i])
    print(i)



'''import csv
with open('data/Figure2/Fig2D/Networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure2/Fig2D/FrustSizeVar.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FrustDist)

with open('data/Figure2/Fig2D/FinalFig2DFrustSizeVar.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''





plt.plot(teamsize,mean_frust, marker="o")
plt.errorbar(teamsize,mean_frust,mean_frust_error,capsize=4,color="r")
plt.xlabel("Teamsize")
plt.ylabel("Frustration")
plt.title("Third team of varying size")



plt.show()


