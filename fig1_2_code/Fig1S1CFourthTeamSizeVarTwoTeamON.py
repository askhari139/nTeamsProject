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

doublepos_percent=[]
doublepos_percent_error=[]

networks=[["FourthTeamSize","Network"]]
TwoOnFrac=[["FractionTwoOn","FourthTeamSize"]]

FigData=[["MeanFracTwoOn","Std","FourthTeamSize"]]



for i in range(1,25):
    teamsize.append(i)

    doublepos_count=[]
    for j in range(0,50):
        adj=nteams.nteam_net(4,[5,5,5,i],[[den,den,den,den],[den,den,den,den],[den,den,den,den],[den,den,den,den]])[0]
        networks.append([i,adj])
        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)
        data=fsc.nteam_on_hybrid_dist(4,[0,5,10,15,15+i],ssf,adj)[2]
        doublepos_count.append(data)

        TwoOnFrac.append([data,i])
        #print("Aye aye captain")

    doublepos_percent.append(np.mean(doublepos_count))
    doublepos_percent_error.append(np.std(doublepos_count))
    FigData.append([np.mean(doublepos_count),np.std(doublepos_count),i])
    print(i, np.mean(doublepos_count))

'''import csv
with open('data/Figure1/Fig1S1C/Networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1S1C/TwoTeamOnDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(TwoOnFrac)

with open('data/Figure1/Fig1S1C/FinalFig1S1C.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''

plt.title("Fourth team of varying size")

plt.errorbar(teamsize,doublepos_percent,doublepos_percent_error,capsize=4, color="r", marker="o")
plt.xlabel("Teamsize")
plt.ylabel("Frequency of Double Positive States")
plt.show()
