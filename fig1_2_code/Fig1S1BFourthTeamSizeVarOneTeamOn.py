import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
import datetime
import boolean_smil
import state_classification as fsc

plt.style.use("ggplot")

#Vary the size of the 4th team and calculate the number of one team on states

den=0.3

teamsize=[]

pure_percent=[]
pure_percent_error=[]

networks=[["FourthTeamSize","Network"]]
OneOnFrac=[["FractionOneOn","FourthTeamSize"]]

FigData=[["MeanFracOneOn","Std","TeamSize"]]

for i in range(1,25):
    teamsize.append(i)

    pure_count=[]
    for j in range(0,50):
        adj=nteams.nteam_net(4,[5,5,5,i],[[den,den,den,den],[den,den,den,den],[den,den,den,den],[den,den,den,den]])[0]
        networks.append([i,adj])
        
        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)

        data=fsc.states_classification_ssf(4,[0,5,10,15,15+i],ssf,adj)[-1]
        pure_count.append(data)
        OneOnFrac.append([data,i])
        #print("Aye aye captain")

    pure_percent.append(np.mean(pure_count))
    pure_percent_error.append(np.std(pure_count))
    FigData.append([np.mean(pure_count),np.std(pure_count),i])
    print(i, np.mean(pure_count))

'''import csv
with open('data/Figure1/Fig1S1B/NetworkThirdTeam.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1S1B/OneTeamOnDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(OneOnFrac)

with open('data/Figure1/Fig1S1B/FinalFig1S1B.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''


plt.title("Fourth team of varying size")
plt.plot(teamsize,pure_percent, marker="o")
plt.errorbar(teamsize,pure_percent,pure_percent_error,capsize=4, color="r")
plt.xlabel("Teamsize")
plt.ylabel("Frequency of States with One Team On")
plt.show()