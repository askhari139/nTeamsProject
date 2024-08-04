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

hybrid_percent=[]
hybrid_percent_error=[]


networks=[["FourthTeamSize","Network"]]
HybFrac=[["FractionHybrid","FourthTeamSize"]]

FigData=[["MeanFracHybrid","Std","FourthTeamSize"]]

for i in range(1,25):
    teamsize.append(i)

    hybrid_count=[]
    for j in range(0,50):
        adj=nteams.nteam_net(4,[5,5,5,i],[[den,den,den,den],[den,den,den,den],[den,den,den,den],[den,den,den,den]])[0]
        networks.append([i,adj])
        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)

        data=fsc.nteam_on_hybrid_dist(4,[0,5,10,15,15+i],ssf,adj)[-1]
        hybrid_count.append(data)
        
        HybFrac.append([data,i])
        #print("Aye aye captain")

    hybrid_percent.append(np.mean(hybrid_count))
    hybrid_percent_error.append(np.std(hybrid_count))
    FigData.append([np.mean(hybrid_count),np.std(hybrid_count),i])
    print(i, np.mean(hybrid_count))


'''import csv
with open('data/Figure1/Fig1S1D/Networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1S1D/HybDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(HybFrac)

with open('data/Figure1/Fig1S1D/FinalFig1S1D.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''

plt.title("Fourth team of varying size")

plt.errorbar(teamsize,hybrid_percent,hybrid_percent_error,capsize=4, color="r", marker="o")
plt.xlabel("Teamsize")
plt.ylabel("Frequency of Hybrid States")
plt.show()