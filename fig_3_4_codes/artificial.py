import numpy as np
import random as rn
import boolean_formalism as bf
import phenotype as pn

#library for constructing and analysing networks
def peripheral(mat): #find peripheral nodes in a network
    per=0
    
    for i in range(len(mat)):
        checkin=0
        checkout=0
        for j in range(len(mat)):
            if mat[i][j]!=0:
                checkout+=1
                
            if mat[j][i]!=0:
                checkin+=1
                
        if checkin==0 or checkout==0:
            per+=1
            
    return per

def actedges(t1,t2,mat): #count activating edges in a network
    edges=0
    for i in t1:
        for j in t2:
            if mat[i][j]==1:
                edges+=1
    return edges

def inhibedges(t1,t2,mat): #count inhibiting edges
    edges=0
    for i in t1:
        for j in t2:
            if mat[i][j]==-1:
                edges+=1
    return edges

def sameteam(i,j,t): #check if nodes i and j belong to the same team t
    if i in t and j in t:
        return True
    elif i not in t and j not in t:
        return True
    else:
        return False

def rectify(t1,t2,mat): #reverse inconsistent edges in a network
    rectmat=mat.copy()
    for i in range(len(mat)):
        for j in range(len(mat)):
            if sameteam(i,j,t1) or sameteam(i,j,t2):
                if mat[i][j]==-1:
                    rectmat[i][j]=1 
            else:
                if mat[i][j]==1 :
                    rectmat[i][j]=-1
    return rectmat

def edges(mat): #count edges in a network
    edg=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=0:
                edg+=1
    return edg



def randnetwork(netsize,den): #completely random network (no teams)
    net=np.zeros((netsize,netsize))
    a=0
    while a < int((netsize**2)*den):
        source=rn.randint(0,netsize-1)
        target=rn.randint(0,netsize-1)
        if net[source][target]==0:
            x=rn.randint(0,1)
            net[source][target]=1 if x==1 else -1
            a+=1
    return net


                
def multiteamnetwork(teamsizes,densities,weights): #create a network with multiple teams, having given densities and weights
#input teamsizes as list/array
#input densities and weights as matrices where element (i,j) describes the density or weight of edges from team i to team j
     netsize=sum(teamsizes)
     teams=[] #initialise teams
     for teamsize in teamsizes:
         teams.append([])
     node=0
     for i in range(len(teams)):
         while (len(teams[i])<teamsizes[i]):
             teams[i].append(node)
             node+=1
     while True:
         net=np.zeros((netsize,netsize)) #initialize adjacency matrix        
         for i in range(len(densities)):
             for j in range(len(densities[i])):
                 a=0
                 while a < (teamsizes[i]*teamsizes[j])*densities[i][j]:
                     source=rn.choice(teams[i]) 
                     target=rn.choice(teams[j])
                     if net[source][target]==0:
                         net[source][target]=weights[i][j] if i==j else -weights[i][j]
                         a+=1
         realteams=pn.partition(pn.influence(net), len(teamsizes))
         if realteams==teams:
             break
     return net, teams  
 
def uniformnetwork(n,teamsize,density): #create a network of uniform density with n teams
    teamsizes=[]
    dens=[]
    wts=[]
    for i in range (n):
        teamsizes.append(teamsize)
        dens.append([])
        wts.append([])
    for den in range(len(dens)):
        for i in range (n):
            dens[den].append(density) 
            wts[den].append(1)
    net, teams=multiteamnetwork(teamsizes, dens, wts)
    return net, teams

def makeinistate(net,teams,teamconfigs,zero,steadyonly): #create an initial state from a team shorthand 
#eg. input: '100'-> state with team1 ON, team2 OFF, team3 OFF
    ststate=np.zeros((len(net)))
    for i in range(len(teamconfigs)):
        for node in teams[i]:
            if teamconfigs[i]=='1':
                ststate[node]=1
            elif zero==False:
                ststate[node]=-1
    return ststate if (bf.issteady(ststate, net,zero)==True or steadyonly==False) else "error" #return a string 'error' if the initial state is unsteady


def makehybstate(net,teams,teamconfigs,zero,steadyonly): #create a hybrid initial state from given initial parameters
#eg. input: [0.4,0.5,0.3] -> 40% of team1 ON, 50% of team2 ON, 30% of team3 ON
    ststate=np.zeros((len(net)))
    for i in range(len(teamconfigs)):
        sample=rn.sample(teams[i], int(teamconfigs[i]*len(teams[i])))
        for node in sample:
            ststate[node]=1
    return ststate if (bf.issteady(ststate, net,zero)==True or steadyonly==False) else "error"
        
    
def randedgedel(net,ndels): #random delete edges from a network
    mat=net.copy()
    check=0
    while check<ndels:
        source=rn.randint(0, len(mat)-1)
        target=rn.randint(0, len(mat)-1)
        if mat[source][target]!=0:
            check+=1
            mat[source][target]=0
    return mat
    

            
        
    
        