import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
import boolean_smil
import state_classification as fsc
import datetime

plt.style.use("ggplot")

#density_varying_0_1
den=0.3
third_team=1

networks=[["Density","Adj"]]
FigData=[["MeanFracOneOn","Std","ThirdTeamDensity"]]
OneOnFrac=[["FractionOneOn","ThirdTeamDensity"]]


density=[]
pure_percent_error=[]
pure_percent=[]

for i in np.linspace(0,1,20):

    density.append(i)
    
    pure_count=[]
    for j in range(0,50):    
        adj=nteams.nteam_net(3,[5,5,third_team],[[den,den,i],[den,den,i],[i,i,i]])[0]
        networks.append([i,adj])

        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)
        data=fsc.states_classification_ssf(3,[0,5,10,10+third_team],ssf,adj)[-1]

        pure_count.append(data)
        OneOnFrac.append([data,i])
    
    print(i,np.mean(pure_count),datetime.datetime.now())

    
    pure_percent.append(np.mean(pure_count))
    pure_percent_error.append(np.std(pure_count))
    
    FigData.append([np.mean(pure_count),np.std(pure_count),i])



'''import csv
with open('data/Figure1/Fig1E/NetworkThirdTeam.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1E/OneTeamOnDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(OneOnFrac)

with open('data/Figure1/Fig1E/FinalFig1C.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''

plt.title("Effect of a third team of size {}".format(third_team))

plt.errorbar(density,pure_percent,pure_percent_error,capsize=4,marker="o",color="r")
plt.xlabel("Density")
plt.ylabel("Fequency of States with One Team On")
plt.show()
