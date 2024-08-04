import nteams
import matplotlib.pyplot as plt 
import numpy as np
import boolean_smil
import frustration
import matplotlib.cm as cm
from scipy.stats.stats import pearsonr
plt.style.use("ggplot")

numsim=50
d=0.5

frust2=[]
freq2=[]

frust3=[]
freq3=[]

frust4=[]
freq4=[]

frust5=[]
freq5=[]

frust6=[]
freq6=[]

frust7=[]
freq7=[]

import csv
FigData2=[["NTeams","Adj","Frustration","Frequency"]]
FigData3=[["NTeams","Adj","Frustration","Frequency"]]
FigData4=[["NTeams","Adj","Frustration","Frequency"]]
FigData5=[["NTeams","Adj","Frustration","Frequency"]]
FigData6=[["NTeams","Adj","Frustration","Frequency"]]
FigData7=[["NTeams","Adj","Frustration","Frequency"]]




def frust_freq(ssf,adj):
    nsteady=0
    for i in range(len(ssf[1])):
        nsteady+=ssf[1][i]
    freq=[]
    for i in range(len(ssf[1])):
        freq.append(ssf[1][i]/nsteady)

    frust=frustration.ensemble_frustration(ssf[0],adj)
    return(freq,frust)

for i in range(0,numsim):
    adj=nteams.nteam_net(2,[5,5],[[d,d],[d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    
    data=frust_freq(ssf,adj)
    frust2+=data[1]
    freq2+=data[0] 
    FigData2.append([2,adj,data[1],data[0]])
print("done")

'''with open('data/Figure2/Fig2S1C/den5/TwoTeamFrustFreqData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData2)
'''


for i in range(0,numsim):
    adj=nteams.nteam_net(3,[5,5,5],[[d,d,d],[d,d,d],[d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)

    data=frust_freq(ssf,adj)
    frust3+=data[1]
    freq3+=data[0]

    FigData3.append([3,adj,data[1],data[0]])
print("done")


'''with open('data/Figure2/Fig2S1C/den5/ThreeTeamFrustFreqData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData3)
'''







for i in range(0,numsim):
    adj=nteams.nteam_net(4,[5,5,5,5],[[d,d,d,d],[d,d,d,d],[d,d,d,d],[d,d,d,d]])[0]

    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    
    data=frust_freq(ssf,adj)
    frust4+=data[1]
    freq4+=data[0]
    FigData4.append([4,adj,data[1],data[0]])

print("done")


'''with open('data/Figure2/Fig2S1C/den5/FourTeamFrustFreqData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData4)
'''




for i in range(0,numsim):
    adj=nteams.nteam_net(5,[5,5,5,5,5],[[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)

    data=frust_freq(ssf,adj)
    frust5+=data[1]
    freq5+=data[0]
    FigData5.append([5,adj,data[1],data[0]])

print("done")


'''with open('data/Figure2/Fig2S1C/den5/FiveTeamFrustFreqData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData5)
'''




for i in range(0,numsim):
    adj=nteams.nteam_net(6,[5,5,5,5,5,5],[[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)

    data=frust_freq(ssf,adj)
    frust6+=data[1]
    freq6+=data[0]
    FigData6.append([6,adj,data[1],data[0]])

print("done")


'''with open('data/Figure2/Fig2S1C/den5/SixTeamFrustFreqData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData6)
'''








for i in range(0,numsim):
    adj=nteams.nteam_net(7,[5,5,5,5,5,5,5],[[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)

    data=frust_freq(ssf,adj)
    frust7+=data[1]
    freq7+=data[0]
    FigData7.append([7,adj,data[1],data[0]])

print("done")

'''with open('data/Figure2/Fig2S1C/den5/SevenTeamFrustFreqData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData7)
'''


'''for i in range(0,numsim):
    adj=nteams.nteam_net(8,[5,5,5,5,5,5,5,5],[[d,d,d,d,d,d,d,d],[d,d,d,d,d,d,d,d],[d,d,d,d,d,d,d,d],[d,d,d,d,d,d,d,d],[d,d,d,d,d,d,d,d],[d,d,d,d,d,d,d,d],[d,d,d,d,d,d,d,d],[d,d,d,d,d,d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,1000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)

    data=frust_freq(ssf,adj)
    frust8+=data[1]
    freq8+=data[0]

    print("done")
'''




data=[[freq2,frust2],[freq3,frust3],[freq4,frust4],[freq5,frust5],[freq6,frust6],[freq7,frust7]]

for i in range(len(data)):
    plt.scatter(np.log(data[i][0]),data[i][1],alpha=0.5,label="{}_teams_corr {}".format(i+2,round(pearsonr(np.log(data[i][0]),data[i][1])[0],3)))

plt.legend()
plt.xlabel("Frequency(log scale)")
plt.ylabel("Frustration")
plt.title("Frustration vs Frequency (Density={})".format(d))
plt.show()
