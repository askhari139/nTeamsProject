import switching as sw
import artificial as art   
import boolean_formalism as bf
import os
import pandas as pd
import phenotype as pn

def main(nteams,size,weight,inconfigs,mt):
    
    #nteams: no. of teams
    #inconfigs: list of initial conditions
    #size: size of each team
    #weight: edge weights for network (keep at 1)
    #mt: multithreading (True if desited, else False)
    
    cwd=os.getcwd()
    cdir=cwd+"//switch_data//network_data_"+str(size)+"//"
 
    dens=[] # density of each network
    phens=[] #destinations for all densities, for all networks at each density
    flips=[] #no. of flips to switch for all densities, for all networks at each density
    hams=[] #initial-destination hamming for all densities, for all networks at each density
    inits=[] #initial states for all densities, for all networks at each density
    
    for i in range(2,10):
        
        #initialise network density
        density=i/10
        print(density)
        dens.append(density)
        flips.append([]) #no. of flips for all networks at given density
        phens.append([]) #destinations for all networks at given density
        hams.append([]) #initial-destination hamming for all networks at given density
        inits.append([]) #initial states for all networks at given density 
        
        for index in range(100): 
            
            netid=str(nteams)+'_'+str(size)+'_'+str(int(density*100))+"_"+str(index)+".topo"
            net,id_to_node=bf.parse_topo(cdir+netid)[0:2] #construct network from topo file
            unordteams=pn.partition(pn.influence(net), nteams)
            teams=[] #order teams using indices from topo file
            for _ in range (len(unordteams)):
                for team in unordteams: 
                    if int(id_to_node[team[0]][0])==_+1:
                        teams.append(team)
                      
            permissible=[] #generate set of flippable nodes
            for team in teams:
                for node in team:
                    permissible.append(node)
                    
            ftot=[] #no. of flips for each simulation on given network
            ptot=[] #destination for each simulation on given network
            intot=[] #initial state for each simulation on given network
            htot=[] #initial-destination hamming for each simulation on given network
            
            netinits=[] #choose initial conditions which are steady on given network
            for state in inconfigs:
                if str(art.makeinistate(net, teams, state, False,True))!='error':
                    netinits.append(state)
                    
            for init in netinits: #simulate for each initial condition
                ini=art.makeinistate(net, teams, init, False,True) #generate initial state 
            
                f,p,h=sw.perturbsim(ini, 100, permissible, net, teams,False,mt)
                ftot+=f
                ptot+=p
                htot+=h
                
                if len(f)!=0: #check if switching has occurred atleast once
                    for flip in f:
                        intot.append(init)
                        
            flips[i-2].append(ftot)
            phens[i-2].append(ptot)
            hams[i-2].append(htot)
            inits[i-2].append(intot)
                    
    return flips,phens,hams,inits,dens  
              
data=[]
cwd=os.getcwd()
size=5 #size of each team
params=[[2,size,1,["10",'01'],False],[3,size,1,["100",'110','010','011','001','101'],False]] #parameter sets
for param in params: #generate data
    flips,phens,hams,inits,dens=main(*param)  
    for den in range(len(dens)):
        for net in range(len(flips[den])):
            for i in range(len(flips[den][net])):
                data.append([param[0],inits[den][net][i],dens[den],net,flips[den][net][i],phens[den][net][i],hams[den][net][i]])

cols=["#teams","initial","density","network index","#flips","destination","hamming"]
netdata=pd.DataFrame(data,columns=cols)
cwd=os.getcwd()
os.chdir(cwd+"//switch_data")
netdata.to_csv((os.getcwd()+"//randompert_"+str(size)+".csv"),sep=',',index=False)
