import nteams
import matplotlib.pyplot as plt 
import numpy as np
import boolean_smil
import random
plt.style.use("ggplot")

def single_pos_gen(nteams,team_indices,n):
    output=[]
    #n=number of nodes
    for i in range(nteams):
        state=[]
        for j in range(0,n):
            if j>=team_indices[i] and j<team_indices[i+1]:
                state.append(1)
            else:
                state.append(-1)
        output.append(state)
    return(output)

#I get double positive by changing -1 to 1 since in three teams everything is symmetric 

def double_pos_gen(nteams,team_indices,n):
    output=[]
    #n=number of nodes
    for i in range(nteams):
        state=[]
        for j in range(0,n):
            if j>=team_indices[i] and j<team_indices[i+1]:
                state.append(-11)
            else:
                state.append(1)
        output.append(state)
    return(output)

def triple_pos_gen(nteams,team_indices,n):
    #Triple positive only for three teams
    output=[]
    state=[]
    for i in range(0,n):
        state.append(1)
    output.append(state)
    return(output)

def random_hybrid_state(nteams,team_indices,n):
    
    output=[]
    for num in range(0,100):    
        state=[]
        for i in range(0,n):
            state.append(random.choice([1,-1]))
        output.append(state)
    return(output)


NetworksFrustDist=[["Adj","FrustDist","Density"]]
FigData=[["MeanFrust","StdFrust","Density"]]

density=[]
mean_frust=[]
std_frust=[]
for i in np.linspace(0,1,20):
    frust=[]
    density.append(i)
    for j in range(0,100):
        adj=nteams.nteam_net(3,[5,5,5],[[i,i,i],[i,i,i],[i,i,i]])[0]
        for k in single_pos_gen(3,[0,5,10,15],15):
            print(k)
            frust.append(boolean_smil.frustration(k,adj))
        
        NetworksFrustDist.append([adj,frust,i])
    
    mean_frust.append(np.mean(frust))

    print(np.mean(frust))

    std_frust.append(np.std(frust))
    print(np.std(frust))

    FigData.append([np.mean(frust),np.std(frust),i])

'''import csv
with open('data/Figure2/Fig2S1F1/NetworkFrustDist.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(NetworksFrustDist)

with open('data/Figure2/Fig2S1F1/FigData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)
'''


plt.plot(density,mean_frust,marker="o",color="r")
plt.errorbar(density,mean_frust,std_frust,capsize=4, color="r")
plt.xlabel("Density")
plt.ylabel("Frustration")
plt.title("Frustration of States with One Team On")
plt.show()
