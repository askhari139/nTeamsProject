import switching as sw
import boolean_formalism as bf
import artificial as art   
import phenotype as pn
import os
import pandas as pd

def main(nteams,inconfigs,size,den): 
    
    #nteams: no. of teams
    #inconfigs: list of initial conditions
    #size: size of each team
    #density: network density
    
    cwd=os.getcwd()
    cdir=cwd+"//switch_data//network_data_"+str(size)+"//"
    allphen=[]  #destinations for all networks, for all levels of perturbation
    perts=[]    #levels of perturbation
    initlist=[] #initial conditions corresponding to each destination
    hammings=[] #hamming distance for corresponding initial-destination pairs
    
    for i in range(1,nteams*size): # perturbation proportions
        perts.append(i/(nteams*size))
        
    for pert in perts:
        
        phens=[] #destinations for all networks, for a given amount of perturbation
        inits=[] #initial conditions corresponding to each destination
        hams=[] #hamming distance for corresponding initial-destination pairs
        
        for index in range(100):
            
            print(perts.index(pert),index)
            netid=str(nteams)+'_'+str(size)+'_'+str(int(den*100))+"_"+str(index)+".topo" #target network file
            net,id_to_node=bf.parse_topo(cdir+netid)[0:2] #create network from file
            unordteams=pn.partition(pn.influence(net), nteams)
            
            teams=[] #order teams according to indexing in topo file
            for i in range (len(unordteams)):
                for team in unordteams:
                    if int(id_to_node[team[0]][0])==i+1:
                        teams.append(team)
                        
            phen=[] #destinations for a given network
            inis=[] #initial state corresponding to each destination  
            ham=[]  #hamming distance of corresponding initial and destinations
            
            for init in inconfigs: #create initial conditions
                ini=art.makeinistate(net, teams, init, False,False) #generate initial state
                phenlist,h=sw.multipert(ini, 100, net, teams, pert, False,False) #destinations and hammings for hundred repititions with current initial state
                for p in phenlist:
                    inis.append(init)
                phen+=phenlist
                ham+=h
                
            phens.append(phen)
            inits.append(inis)
            hams.append(ham)
            
        allphen.append(phens)
        initlist.append(inits)
        hammings.append(hams)
        
    return perts,allphen,initlist,hammings
        
inits=[["10"],["100","110"]] #initial states
size=5
nteamslist=[2,3] 
den=[i/10 for i in range(2,10)] #density range
data=[]

for i in range(2): #simulate for given parameters
    for d in den:
        print(i,d)
        perts,phens,inis,hams=main(nteamslist[i],inits[i],size,d) 
        for p in range(len(perts)):
            for net in range(len(phens[p])):
                for rep in range(len(phens[p][net])):
                    data.append([nteamslist[i],perts[p],d,net,inis[p][net][rep],phens[p][net][rep],hams[p][net][rep]])
cwd=os.getcwd()
filename="multirandom_"+str(size)+".csv"
address=cwd+"//switch_data//"+filename
cols=["#teams","perturbation","density","network index","initial","destination","hamming"]
netdata=pd.DataFrame(data,columns=cols)

netdata.to_csv(address,sep=',',index=False)