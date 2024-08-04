import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np

import boolean_smil
import state_classification as fsc

plt.style.use("ggplot")


den=0.3

teamsize=[]

OneOn_percent=[]
OneOn_percent_error=[]

networks=[["Network","ThirdTeamSize"]]
OneOnFrac=[["FractionOneOn","ThirdTeamSize"]]

FigData=[["MeanFracOneOn","Std","TeamSize"]]
for i in range(1,25):
    teamsize.append(i)

    OneOn_count=[]
    for j in range(0,50):
        adj=nteams.nteam_net(3,[5,5,i],[[den,den,den],[den,den,den],[den,den,den]])[0]
        networks.append([adj,i])
        
        steadys=boolean_smil.steady_states(adj,10000)
        networks.append([adj,i,steadys])
        ssf=boolean_smil.steady_state_frequency(steadys,adj)
        data=fsc.states_classification_ssf(3,[0,5,10,10+i],ssf,adj)[-1]
        
        
        OneOn_count.append(data)
        OneOnFrac.append([data,i])
        #print("Aye aye captain")

    OneOn_percent.append(np.mean(OneOn_count))
    OneOn_percent_error.append(np.std(OneOn_count))
    FigData.append([np.mean(OneOn_count),np.std(OneOn_count),i])
    print(i, np.mean(OneOn_count))


'''import csv
with open('data/Figure1/Fig1B/NetworkThirdTeam.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/OneTeamOnDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(OneOnFrac)

with open('data/Figure1/Fig1B/FinalFig1B.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''

plt.title("Third team of varying size")

plt.errorbar(teamsize,OneOn_percent,OneOn_percent_error,marker="o",capsize=4)
plt.xlabel("Teamsize")
plt.ylabel("Frequency of States with One Team On")
plt.show()
