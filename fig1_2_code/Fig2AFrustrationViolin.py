import boolean_smil
import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np

from scipy import stats

plt.style.use("ggplot")



networks=[["NoTeams","Adj","SteadyStates"]]
FrustData=[["NoTeams", "FrustDist"]]

d=0.3


adj2=nteams.nteam_net(2,[5,5], [[d,d],[d,d]])[0]

adj3=nteams.nteam_net(3,[5,5,5],[[d,d,d],[d,d,d],[d,d,d]])[0]

adj4=nteams.nteam_net(4,[5,5,5,5],[[d,d,d,d],[d,d,d,d],[d,d,d,d],[d,d,d,d]])[0]

adj5=nteams.nteam_net(5,[5,5,5,5,5],[[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]])[0]

adj6=nteams.nteam_net(6,[5,5,5,5,5,5],[[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d]])[0]

adj7=nteams.nteam_net(7,[5,5,5,5,5,5,5],[[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d]])[0]


steadys2=boolean_smil.steady_states(adj2,10000)
networks.append([2,adj2,steadys2])

steadys3=boolean_smil.steady_states(adj3,10000)
networks.append([3,adj3,steadys3])

steadys4=boolean_smil.steady_states(adj4,10000)
networks.append([4,adj4,steadys4])

steadys5=boolean_smil.steady_states(adj5,10000)
networks.append([5,adj5,steadys5])

steadys6=boolean_smil.steady_states(adj6,10000)
networks.append([6,adj6,steadys6])

steadys7=boolean_smil.steady_states(adj7,10000)
networks.append([7,adj7,steadys7])

frust2=frustration.ensemble_frustration(steadys2,adj2)
frust3=frustration.ensemble_frustration(steadys3,adj3)
frust4=frustration.ensemble_frustration(steadys4,adj4)
frust5=frustration.ensemble_frustration(steadys5,adj5)
frust6=frustration.ensemble_frustration(steadys6,adj6)
frust7=frustration.ensemble_frustration(steadys7,adj7)


FrustData.append([2,frust2])
FrustData.append([3,frust3])
FrustData.append([4,frust4])
FrustData.append([5,frust5])
FrustData.append([6,frust6])
FrustData.append([7,frust7])




'''import csv
with open('data/Figure2/Fig2A/Networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure2/Fig2A/FrustDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FrustData)
'''




pos=[1,2,3,4,5,6]
data=[frust2,frust3,frust4,frust5,frust6,frust7]
label=["Two Teams", "Three Teams", "Four Teams", "Five Teams", "Six Teams","Seven Teams"]

'''pos=[1,2]
data=[frust2,frust3]
label=["Two Teams", "Three Teams"]

'''


plt.figure()
ax=plt.subplot(111)
plt.violinplot(data,pos)
ax.set_xticks(pos)
ax.set_xticklabels(label)
plt.ylabel("Frustration")

plt.title("Frustration Distributions")
plt.show()

#--------------- t test to establish that the frustration distribution are different

'''p_valt2_3=stats.ttest_ind(frust2,frust3)[-1]
print(np.round( p_valt2_3, 4))

plt.show()'''