#Fig1S1F2ThreeTeamDiffSizeAllTeam

import seaborn as sns
import matplotlib.pyplot as plt
import nteams 
import boolean_smil
import state_classification as fsc
import numpy as np 
import frustration



plt.style.use("ggplot")


#its a set of subplots where the density is varied and activation of each team is kept track of with each subplot having third team of a different size 

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


networks=[["ThirdTeamSize","ThirdTeamDensity","Network"]]
Team1Trij=[["ThirdTeamSize","ThirdTeamDensity","OneOnFreqMean","StdDev"]]
Team2Trij=[["ThirdTeamSize","ThirdTeamDensity","OneOnFreqMean","StdDev"]]
Team3Trij=[["ThirdTeamSize","ThirdTeamDensity","OneOnFreqMean","StdDev"]]

third_team=7

keys=[1,2,3]

den1=0.3 #den1 is the density of all the other teams and den 2 is the density of the third team


diff_trijectories=[] #List of dictionaries having different tijectories

for count in range(0,50): #Counts the number of trijectories you're averaging from 
    ssfs=[]
    density=[] 
    for den2 in np.linspace(0,1,10):
        density.append(den2)

        pure_count=[]
        
        adj=nteams.nteam_net(3,[5,5,third_team],[[den1,den1,den2],[den1,den1,den2],[den2,den2,den2]])[0]
        networks.append([third_team,den2,adj]) 
        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)
        
        ssfs.append(fsc.pure_teamon_freq(3,[0,5,10,10+third_team],steadys,adj))
    print(count)
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
    Team1Trij.append([third_team,density[i],mean_trij[0][i],error_trij[0][i]])
    Team2Trij.append([third_team,density[i],mean_trij[1][i],error_trij[1][i]])
    Team3Trij.append([third_team,density[i],mean_trij[2][i],error_trij[2][i]])


'''import csv
with open('data/Figure1/Fig1S1EFG/ThirdSize{}/Networks.csv'.format(third_team), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1S1EFG/ThirdSize{}/Team1Trij.csv'.format(third_team), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Team1Trij)
with open('data/Figure1/Fig1S1EFG/ThirdSize{}/Team2Trij.csv'.format(third_team), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Team2Trij)
with open('data/Figure1/Fig1S1EFG/ThirdSize{}/Team3Trij.csv'.format(third_team), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(Team3Trij)
'''

for i in range(0,len(mean_trij)):
    
    print(mean_trij[i],type(mean_trij[i]))
    
    
    plt.errorbar(density,mean_trij[i],error_trij[i],capsize=4, marker="o",label="team_{} on".format(i+1))

plt.xlabel("Density")
plt.ylabel("Frequency")
plt.legend()
plt.title("Third team(Size ={}) density variation ".format(third_team))
plt.show()