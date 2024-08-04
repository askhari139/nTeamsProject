#To calculate various functions about frustration 
import scipy.stats as sci


def edge_count(adj):
    n=len(adj)
    count=0

    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]!=0:
                count+=1
    return(count)


def frust(state,adj):
    n=len(adj)

    edge= edge_count(adj)

    frustration_count=0
    for i in range(0,n):
        for j in range(0,n):
            if adj[i][j]* state[i]*state[j]<0:
                frustration_count+=1
    frustration=frustration_count/edge

    return(frustration)

def ensemble_frustration(states,adj ):
    #Input a list of steady states, get a list of frustration values
    output=[]
    for i in states:
        output.append(frust(i,adj))
    return(output)


def frustration_wrt2(state,teamindices,adj):
#Let's calculate the frustration for first two teams, whatever that maybe.

    n=len(adj)

    edge=0

    frustration_count=0

    n2=teamindices[2]

    frustration_count=0
    for i in range(0,n2):
        for j in range(0,n2):
            if adj[i][j]!=0:
                edge+=1
            
            if adj[i][j]* state[i]*state[j]<0:
                frustration_count+=1
    frustration=frustration_count/edge

    return(frustration)

def ensemble_frustration_wrt2(states,adj ):
    #Input a list of steady states, get a list of frustration values
    output=[]
    for i in states:
        output.append(frust(i,adj))
    return(output)

def biomdality(frust_dist):

    n=len(frust_dist)
    if n!=2 and n!=3:
        k=sci.stats.kurtosis(frust_dist)
        s=sci.stats.kurtosis(frust_dist)
        denom= 3*(((n-1)**2)/((n-2)*(n-3)))+k
        numer=(s**2)+1

        return(denom/numer)
    else:
        return(0)
