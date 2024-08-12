import switching as sw
import boolean_formalism as bf
import artificial as art   
import phenotype as pn
import os
import pandas as pd
import multiprocessing as mp

def pertrep(nteams,size,den,cdir,inconfigs,pert):
    phens=[] #destinations for all networks, for a given amount of perturbation
    inits=[] #initial conditions corresponding to each destination
    hams=[] #hamming distance for corresponding initial-destination pairs
    
    for index in range(100):
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
    
    return phens,inits,hams

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
    
    for i in range(6**nteams): #generate all combinations of perturbation proportions
        perts.append([])
        for t in range(nteams):
            perts[i].append((int(i/6**t)%6)/6*6/5)
        
        
    params=[[nteams,size,den,cdir,inconfigs,pert] for pert in perts]
    with mp.Pool() as p:
        result=p.starmap(pertrep,params)
    for r in result:
        allphen.append(r[0])
        initlist.append(r[1])
        hammings.append(r[2])
        
    return perts,allphen,initlist,hammings
        
inits=[["10"],["100","110"]] #initial states
size=5
nteams=[2,3]
den=[i/10 for i in range(2,10)] #density range
data=[]

for i in range(2): #simulate for given parameters
    for d in den:
        print(i,d)
        perts,phens,inis,hams=main(nteams[i],inits[i],size,d)
        for p in range(len(perts)):
            for net in range(len(phens[p])):
                for rep in range(len(phens[p][net])):
                    data.append([nteams[i],perts[p],d,net,inis[p][net][rep],phens[p][net][rep],hams[p][net][rep]])

cols=["#teams","perturbation","density","network index","initial","destination","hamming"]
netdata=pd.DataFrame(data,columns=cols)
filename="directed_"+str(size)+".csv"
netdata.to_csv((os.getcwd()+"//switch_data//"+filename),sep=',',index=False)