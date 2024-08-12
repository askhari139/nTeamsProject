import numpy as np
import scipy.stats as sci
from scipy.cluster import hierarchy as hi
import statistics as st
import copy

#library of functions for analysing boolean phenotypes

def score(teams,state): #assigns a team-score to phenotypes 
    scores=[]
    for i in teams:
        scores.append(0)
    for i in range(len(teams)):
        for j in range(len(state)):
            if j in teams[i]:
                if state[j]==1:
                    scores[i]+=1 #increment score of corresponding team by 1 if node is ON
        scores[i]/=len(teams[i]) #normalize
    return scores
            
            
def bimodality(labelledststates): #bimodality coefficient
    n=len(labelledststates)
    k=sci.stats.kurtosis(labelledststates)
    s=sci.stats.skew(labelledststates)
    denom= 3*(((n-1)**2)/((n-2)*(n-3)))+k
    numer=(s**2)+1
    return numer/denom
    
def divmat(numer,denom):
    n=len(numer)
    newmat=np.zeros((n,n))
    for i in range (0,n):
        for j in range (0,n):
            if denom[i][j]!=0:
                newmat[i][j]=(numer[i][j])/(denom[i][j])
    return newmat

def influence(mat): #influence matrix calc
    adj=mat.copy()
    n=len(mat)
    adjmax=np.zeros((n,n))
    for i in range (0,n):
        for j in range (0,n):
            if mat[i][j]!=0:
                adjmax[i][j]=1
    summ=np.zeros((n,n))
    div=0
    for i in range (1,11):
        numer=np.linalg.matrix_power(adj,i)
        denom=np.linalg.matrix_power(adjmax,i)
        summ=summ+(divmat(numer,denom))#*1/i
        div+=1/i
        
    return summ/10
        
            
def tkl(influence,t1,t2):
    summ=0
    n=len(t1)*len(t2)
    for i in t1:
        for j in t2:
            summ+=(influence[i][j])
    return summ/n

def strength(influence,teams): #team strength calc
    comps=[]
    for i in teams:
        for j in teams:
            comps.append(abs(tkl(influence,i,j)))
    
    return st.mean(comps)

def partition(influence,n): #determine teams using hierarchical clustering
    
    d = hi.distance.pdist(influence)
    L = hi.linkage(d, method = 'complete')
    clust = hi.cut_tree(L, n_clusters = n)
    cluster = np.transpose(clust)
   
    teams=[]
    for i in range (n):
        teams.append([])
    
    for i in range (len(cluster[0])):
        teams[cluster[0][i]].append(i)
    
    return teams

def classify(state,teams): #create team shorthand for a given steady state
#eg. Team1 ON, team2 OFF, team3 ON -> '101'

    classif=[]
    for team in teams:
        onnodes=0
        for node in team:
            if state[node]==1:
                onnodes+=1
        if onnodes==len(team):
            classif.append(1)
        if onnodes==0:
            classif.append(0)
        
    index=0
        
    if len(classif)!=len(teams):
        classif=[5] #dummy value if atleast one team is neither completely ON nor OFF
    for i in classif:
        index=index*(10)+i #convert list to a numerical index
    
    index=str(index) #convert numerical index to string
    if index !="5" and len(index)!=len(teams):
        while len(index)<len(teams):
            index="0"+index
            
    if index=="5": #hybrid phenotypes
        index="other"
    return index
               
def ispure(index): #check if a given team shorthand is pure
    indexcopy=copy.deepcopy(index)
    check=0
    for i in range (len(indexcopy)):
        if indexcopy[i]=="1":
            check+=1
        
    return True if check==1 else False

def issemipure(index): #check if a given team shorthand is semi-pure
    indexcopy=copy.deepcopy(index)
    check=0
    for i in range (len(indexcopy)):
        if indexcopy[i]=="1":
            check+=1
        
    return True if check>1 else False
    

def hamming(state1,state2): #hamming distance between 2 given boolean states
    h=0
    for i in range(len(state1)):
        if state1[i]!=state2[i]:
            h+=1
    h/=len(state1)
    return h


