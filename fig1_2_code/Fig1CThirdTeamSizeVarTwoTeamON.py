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

dopos_percent=[]
dopos_percent_error=[]


networks=[["ThirdTeamSize","Network"]]
TwoOnFrac=[["FractionTwoOn","ThirdTeamSize"]]

FigData=[["MeanFracTwoOn","Std","TeamSize"]]


for i in range(1,25):
    teamsize.append(i)

    dopos_count=[]

    for j in range(0,50):
        adj=nteams.nteam_net(3,[5,5,i],[[den,den,den],[den,den,den],[den,den,den]])[0]
        networks.append([i,adj])
        
        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)

        data=fsc.nteam_on_hybrid_dist(3,[0,5,10,1+i],ssf,adj)[2]

        dopos_count.append(data)
        TwoOnFrac.append([data,i])
        
        print("Aye aye captain")

    dopos_percent.append(np.mean(dopos_count))
    dopos_percent_error.append(np.std(dopos_count))
    FigData.append([np.mean(dopos_count),np.std(dopos_count),i])

    print(i, np.mean(dopos_count))


'''import csv
with open('data/Figure1/Fig1C/NetworkThirdTeam.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1C/TwoTeamOnDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(TwoOnFrac)

with open('data/Figure1/Fig1C/FinalFig1C.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''
plt.title("Third team of varying size")
plt.plot(teamsize,dopos_percent, marker="o", label="Double Positive")
plt.errorbar(teamsize,dopos_percent,dopos_percent_error,capsize=4)


plt.legend()
plt.xlabel("Teamsize")
plt.ylabel("Frequency of Double Positive States")
plt.show()
