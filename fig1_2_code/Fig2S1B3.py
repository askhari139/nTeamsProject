import boolean_smil
import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
plt.style.use("ggplot")


path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/2_3_teams/figure1_24/mean_var"

#100 networks mean frustration vs var for 2 teams for 3 teams 
import csv

FigData2=[["NTeams","Adj","Mean","Var"]]
FigData3=[["NTeams","Adj","Mean","Var"]]
FigData4=[["NTeams","Adj","Mean","Var"]]
FigData5=[["NTeams","Adj","Mean","Var"]]
FigData6=[["NTeams","Adj","Mean","Var"]]
FigData7=[["NTeams","Adj","Mean","Var"]]

mean2=[]
var2=[]


mean3=[]
var3=[]


mean4=[]
var4=[]


mean5=[]
var5=[]


mean6=[]
var6=[]


mean7=[]
var7=[]

numsim=50
d=0.7

for i in range(0,numsim):
    adj=nteams.nteam_net(2,[5,5],[[d,d],[d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean2.append(np.mean(frust_dist))
    var2.append(np.var(frust_dist))

    FigData2.append([2,adj,mean2,var2])
print("done2teams")

'''with open('data/Figure2/Fig2S1B/den7/TwoTeamFrustMeanVarData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData2)
'''

for i in range(0,numsim):
    adj=nteams.nteam_net(3,[5,5,5],[[d,d,d],[d,d,d],[d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean3.append(np.mean(frust_dist))
    var3.append(np.var(frust_dist))
    FigData3.append([3,adj,mean3,var3])
print("done3teams")

'''with open('data/Figure2/Fig2S1B/den7/ThreeTeamFrustMeanVarData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData3)
'''

for i in range(0,numsim):
    adj=nteams.nteam_net(4,[5,5,5,5],[[d,d,d,d],[d,d,d,d],[d,d,d,d],[d,d,d,d]])[0]

    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean4.append(np.mean(frust_dist))
    var4.append(np.var(frust_dist))
    FigData4.append([4,adj,mean4,var4])
print("done4team")

'''with open('data/Figure2/Fig2S1B/den7/FourTeamFrustMeanVarData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData4)
'''


for i in range(0,numsim):
    adj=nteams.nteam_net(5,[5,5,5,5,5],[[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean5.append(np.mean(frust_dist))
    var5.append(np.var(frust_dist))
    FigData5.append([5,adj,mean5,var5])
print("done5team")

'''with open('data/Figure2/Fig2S1B/den7/FiveTeamFrustMeanVarData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData5)
'''


for i in range(0,numsim):
    adj=nteams.nteam_net(6,[5,5,5,5,5,5],[[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d]])[0]

    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean6.append(np.mean(frust_dist))
    var6.append(np.var(frust_dist))
    FigData2.append([6,adj,mean6,var6])
print("done6team")

'''with open('data/Figure2/Fig2S1B/den7/SixTeamFrustMeanVarData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData6)
'''

for i in range(0,numsim):
    adj=nteams.nteam_net(7,[5,5,5,5,5,5,5],[[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d]])[0]

    steadys=boolean_smil.steady_states(adj,10000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean7.append(np.mean(frust_dist))
    var7.append(np.var(frust_dist))
    FigData2.append([7,adj,mean7,var7])
print("done7team")


'''with open('data/Figure2/Fig2S1B/den7/SevenTeamFrustMeanVarData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData7)
'''


plt.scatter(mean2,var2 , marker="o", label="Two Teams", color="b", alpha=0.7)
plt.scatter(mean3,var3 , marker="o", label="Three Teams", color="r", alpha=0.7)
plt.scatter(mean4,var4 , marker="o", label="Four Teams" , alpha=0.7)
plt.scatter(mean5,var5 , marker="o", label="Five Teams", alpha=0.7)
plt.scatter(mean6,var6 , marker="o", label="Six Teams",  alpha=0.7)
plt.scatter(mean7,var7 , marker="o", label="Seven Teams",  alpha=0.7)




plt.xlabel("Mean")
plt.ylabel("Variance")
plt.legend()
plt.title("Mean vs Variance of Frustration (Density={}) ".format(d))
plt.show()


#The following plot plots the bimodality coefficients 



'''
for i in range(0,numsim):
    adj=nteams.nteam_net(2,[5,5],[[d,d],[d,d]])[0]
    steadys=boolean_smil.steady_states(adj,1000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean2.append(np.mean(frust_dist))
    var2.append(np.var(frust_dist))
    bimod2.append(frustration.biomdality(frust_dist))
    print("done")

for i in range(0,numsim):
    adj=nteams.nteam_net(3,[5,5,5],[[d,d,d],[d,d,d],[d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,1000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean3.append(np.mean(frust_dist))
    var3.append(np.var(frust_dist))
    bimod3.append(frustration.biomdality(frust_dist))

    print("done")

for i in range(0,numsim):
    adj=nteams.nteam_net(4,[5,5,5,5],[[d,d,d,d],[d,d,d,d],[d,d,d,d],[d,d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,1000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean4.append(np.mean(frust_dist))
    var4.append(np.var(frust_dist))
    bimod4.append(frustration.biomdality(frust_dist))
    
    print("done")


for i in range(0,numsim):
    adj=nteams.nteam_net(5,[5,5,5,5,5],[[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]])[0]
    steadys=boolean_smil.steady_states(adj,1000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean5.append(np.mean(frust_dist))
    var5.append(np.var(frust_dist))
    bimod5.append(frustration.biomdality(frust_dist))

    print("done")


for i in range(0,numsim):
    adj=nteams.nteam_net(6,[5,5,5,5,5,5],[[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d]])[0]

    steadys=boolean_smil.steady_states(adj,1000)
    frust_dist=frustration.ensemble_frustration(steadys,adj)
    mean6.append(np.mean(frust_dist))
    var6.append(np.var(frust_dist))
    bimod6.append(frustration.biomdality(frust_dist))

    print("done")


plt.hist(bimod2,label="Two Teams", alpha=0.6)
plt.hist(bimod3,label="Three Teams", alpha=0.6)
plt.hist(bimod4,label="Four Teams", alpha=0.6)
plt.hist(bimod5,label="Five Teams", alpha=0.6)
plt.hist(bimod6,label="Six Teams", alpha=0.6)

plt.title("Bimodality Coefficients of Frustration Distribution")
plt.xlabel("Bimodality Coefficient")
plt.ylabel("Frequency")
plt.legend()
plt.show()
'''
