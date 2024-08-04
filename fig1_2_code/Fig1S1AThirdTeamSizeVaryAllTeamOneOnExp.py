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




#The size of the third team is varied and activation of the three different teams is measured

'''
you have a list of ssf's and list of densities/sizes/time

'''
def ssf_merge(keys,ssfs, dict):
    #ssfs is a lisf of ssfs in increasing order 
    for i in ssfs:
        n=len(i[0])
        for j in range(0,n):
            if i[0][j] in keys:
                dict[i[0][j]].append(i[1][j])
            elif i[0][j] not in keys:
                dict[i[0][j]]=[i[1][j]]
                keys.append(i[0][j])
            
        for key in keys:
            if key not in i[0]:
                dict[key].append(0)
    return(dict,keys)
#The key has to be defined and known before

def dict_create(keys):
    dict={}
    for i in keys:
        dict[i]=[]
    return(dict)




den=0.3
keys=[1,2,3]

networks=[["ThirdTeamSize","Network"]]
Team1Trij=[["ThirdTeamSize","OneOnFreqMean","StdDev"]]
Team2Trij=[["ThirdTeamSize","OneOnFreqMean","StdDev"]]
Team3Trij=[["ThirdTeamSize","OneOnFreqMean","StdDev"]]

diff_trijectories=[] #List of dictionaries having different tijectories

for j in range(0,50):
    ssfs=[]
    teamsize=[] 
    for i in range(1,25):
        teamsize.append(i)

        
        adj=nteams.nteam_net(3,[5,5,i],[[den,den,den],[den,den,den],[den,den,den]])[0]
        networks.append([i,adj])   
        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)
        
        ssfs.append(fsc.pure_teamon_freq(3,[0,5,10,10+i],steadys,adj))
        print(i,j)

    dict=dict_create(keys)
    data=ssf_merge(keys,ssfs,dict)[0]
    diff_trijectories.append(data)


#Mean and error caclulation for different trijectories 
mean_trij=[]
error_trij=[]
trijectory_list=[]


#The below uses the keys as indices such that index=key-1 and makes a nested list of all trijectories 
count=0
for i in keys:
    trijectory_list.append([])
    
    for j in diff_trijectories:
        
        trijectory_list[count].append(j[i])
    count+=1
for i in trijectory_list:

    mean_trij.append(np.mean(i,axis=0))
    error_trij.append(np.std(i,axis=0))
print(len(mean_trij))





tot=len(mean_trij[0])

for i in range(0,tot):
    Team1Trij.append([teamsize[i],mean_trij[0][i],error_trij[0][i]])
    Team2Trij.append([teamsize[i],mean_trij[1][i],error_trij[1][i]])
    Team3Trij.append([teamsize[i],mean_trij[2][i],error_trij[2][i]])



'''import csv
with open('data/Figure1/Fig1S1A/NetworkThirdTeam.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1S1A/Team1Trij.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Team1Trij)
with open('data/Figure1/Fig1S1A/Team2Trij.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Team2Trij)
with open('data/Figure1/Fig1S1A/Team3Trij.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Team3Trij)
'''


for i in range(0,len(mean_trij)):
    
    #print(mean_trij[i],type(mean_trij[i]))
    #print(teamsize,len(teamsize))
    
    
    plt.errorbar(teamsize,mean_trij[i],error_trij[i],capsize=4, marker="o",label="team_{} on".format(i+1))

plt.xlabel("Third team size")
plt.ylabel("Frequency")
plt.legend()
plt.title("Third team size variation")
plt.show()

