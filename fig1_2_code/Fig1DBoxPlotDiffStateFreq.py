import seaborn as sns
import matplotlib.pyplot as plt
import nteams 
import boolean_smil
import state_classification as fsc
import numpy as np 
import csv
plt.style.use("ggplot")


numsim=50


#Figure 1D- box plots of various states seen in different teams

d=0.3


two_team=[]
two_team_transpose=[]
fig,axs=plt.subplots(2,3,sharey=True)
plt.tick_params(left=False)

networks=[["NoTeams","Network"]]
States=[]
for i in range(0,numsim):
    adj=nteams.nteam_net(2,[5,5],[[d,d],[d,d]])[0]
    networks.append([2,adj])

    steadys=boolean_smil.steady_states(adj,10000)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    state_pos=fsc.nteam_on_hybrid_dist(2,[0,5,10],ssf,adj)[1:-1]
    two_team.append(state_pos)
    
n1=len(two_team)
n2=len(two_team[0])


labels=["{}_on".format(i+1) for i in range(0,n2)]


States.append(labels)

for i in two_team:
    print(i)
    States.append(i)

two_team=np.matrix(two_team)



'''

with open('data/Figure1/Fig1D/2Teams/networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1D/2Teams/TwoTeamStates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(States)
'''


axs[0, 0].boxplot(two_team, labels=labels)
axs[0, 0].set_xlabel("Number of Teams on")
axs[0, 0].set_ylabel("Frequency")
axs[0, 0].set_title("Two Teams")

print(labels)











networks=[["NoTeams","Network"]]
States=[]

three_team=[]
for i in range(0,numsim):
    adj=nteams.nteam_net(3,[5,5,5],[[d,d,d],[d,d,d],[d,d,d]])[0]
    networks.append([3,adj])
    
    steadys=boolean_smil.steady_states(adj,10000)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    state_pos=fsc.nteam_on_hybrid_dist(3,[0,5,10,15],ssf,adj)[1:-1]
    three_team.append(state_pos)
    
n1=len(three_team)
n2=len(three_team[0])

labels=["{}_on".format(i+1) for i in range(0,n2)]

States.append(labels)

for i in three_team:
    print(i)
    States.append(i)

three_team=np.matrix(three_team)

'''with open('data/Figure1/Fig1D/3Teams/networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1D/3Teams/TwoTeamStates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(States)
'''


axs[0, 1].boxplot(three_team, labels=labels)
axs[0, 1].set_xlabel("Number of Teams on")
axs[0, 1].set_ylabel("Frequency")
axs[0, 1].set_title("Three Teams")


print(labels)











networks=[["NoTeams","Network"]]
States=[]

four_team=[]

for i in range(0,numsim):
    adj=nteams.nteam_net(4,[5,5,5,5],[[d,d,d,d],[d,d,d,d],[d,d,d,d],[d,d,d,d]])[0]
    networks.append([4,adj])
    steadys=boolean_smil.steady_states(adj,10000)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    state_pos=fsc.nteam_on_hybrid_dist(4,[0,5,10,15,20],ssf,adj)[1:-1]
    four_team.append(state_pos)
    
n1=len(four_team)
n2=len(four_team[0])

labels=["{}_on".format(i+1) for i in range(0,n2)]

States.append(labels)

for i in four_team:
    print(i)
    States.append(i)

four_team=np.matrix(four_team)








'''with open('data/Figure1/Fig1D/4Teams/networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1D/4Teams/TwoTeamStates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(States)
'''


axs[0, 2].boxplot(four_team, labels=labels)
axs[0, 2].set_xlabel("Number of Teams on")
axs[0, 2].set_ylabel("Frequency")
axs[0, 2].set_title("Four Teams")

print(labels)








networks=[["NoTeams","Network"]]
States=[]

five_team=[]
for i in range(0,numsim):
    adj=nteams.nteam_net(5,[5,5,5,5,5],[[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d],[d,d,d,d,d]])[0]
    networks.append([5,adj])
    steadys=boolean_smil.steady_states(adj,10000)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    state_pos=fsc.nteam_on_hybrid_dist(5,[0,5,10,15,20,25],ssf,adj)[1:-1]
    five_team.append(state_pos)
    
n1=len(five_team)
n2=len(five_team[0])

labels=["{}_on".format(i+1) for i in range(0,n2)]

States.append(labels)

for i in five_team:
    print(i)
    States.append(i)

'''with open('data/Figure1/Fig1D/5Teams/networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1D/5Teams/TwoTeamStates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(States)
'''
five_team=np.matrix(five_team)




axs[1, 0].boxplot(five_team, labels=labels)
axs[1, 0].set_xlabel("Number of Teams on")
axs[1, 0].set_ylabel("Frequency")
axs[1, 0].set_title("Five Teams")

print(labels)






networks=[["NoTeams","Network"]]
States=[]

six_team=[]
for i in range(0,numsim):
    adj=nteams.nteam_net(6,[5,5,5,5,5,5],[[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d],[d,d,d,d,d,d]])[0]
    networks.append([6,adj])
    steadys=boolean_smil.steady_states(adj,10000)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    state_pos=fsc.nteam_on_hybrid_dist(6,[0,5,10,15,20,25,30],ssf,adj)[1:-1]
    six_team.append(state_pos)
    
n1=len(six_team)
n2=len(six_team[0])


labels=["{}_on".format(i+1) for i in range(0,n2)]

States.append(labels)

for i in six_team:
    print(i)
    States.append(i)

'''with open('data/Figure1/Fig1D/6Teams/networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1D/6Teams/TwoTeamStates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(States)
'''

six_team=np.matrix(six_team)




axs[1, 1].boxplot(six_team, labels=labels)
axs[1, 1].set_xlabel("Number of Teams on")
axs[1, 1].set_ylabel("Frequency")
axs[1, 1].set_title("Six Teams")

print(labels)






networks=[["NoTeams","Network"]]
States=[]


seven_team=[]
for i in range(0,numsim):
    adj=nteams.nteam_net(7,[5,5,5,5,5,5,5],[[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d],[d,d,d,d,d,d,d]])[0]
    networks.append([7,adj])
    steadys=boolean_smil.steady_states(adj,10000)
    ssf=boolean_smil.steady_state_frequency(steadys,adj)
    state_pos=fsc.nteam_on_hybrid_dist(7,[0,5,10,15,20,25,30,35],ssf,adj)[1:-1]
    seven_team.append(state_pos)
    
n1=len(seven_team)
n2=len(seven_team[0])

labels=["{}_on".format(i+1) for i in range(0,n2)]

States.append(labels)

for i in seven_team:
    print(i)
    States.append(i)


seven_team=np.matrix(seven_team)

'''with open('data/Figure1/Fig1D/7Teams/networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1D/7Teams/TwoTeamStates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(States)
'''

axs[1, 2].boxplot(seven_team, labels=labels)
axs[1, 2].set_xlabel("Number of Teams on")
axs[1, 2].set_ylabel("Frequency")
axs[1, 2].set_title("Seven Teams")

print(labels)


plt.show()