import switching as sw
import artificial as art   
import boolean_formalism as bf
import os
import pandas as pd
import phenotype as pn

def main(nteams,size,weight,inconfigs,dests,mt):
    
    #nteams: no. of teams
    #inconfigs: list of initial conditions
    #size: size of each team
    #weight: edge weights for network (keep at 1)
    #dests: Desired destination
    #mt: multithreading (True if desited, else False)
        
    cwd=os.getcwd()
    cdir=cwd+"//switch_data//network_data_"+str(size)+"//"
    #cdir=cwd+"//network_data_"+str(size)+"//"
    dens=[] # density of each network
    phens=[] #destinations for all densities, for all networks at each density
    flips=[] #no. of flips to switch for all densities, for all networks at each density
    inits=[] #initial states for all densities, for all networks at each density
    destins=[] #actual destination for all densities, for all networks at each density
    hams=[] #initial-destination(actual) hamming for all densities, for all networks at each density
    inhams=[] #initial-destination(desired) hamming for all densities, for all networks at each density
    
    for i in range(2,10):
        
        #initialise network density
        density=i/10
        print(density)
        dens.append(density)
        flips.append([]) #no. of flips for all networks at given density
        phens.append([]) #destinations for all networks at given density
        inits.append([]) #initial states for all networks at given density 
        destins.append([]) #actual destination for all networks at a given density
        hams.append([]) #initial-destination hamming for all networks at given density
        inhams.append([]) #initial-destination(desired) hamming for networks at a given density
        
        for index in range(100): 
            
            netid=str(nteams)+'_'+str(size)+'_'+str(int(density*100))+"_"+str(index)+".topo"
            net,id_to_node=bf.parse_topo(cdir+netid)[0:2] #construct network from topo file
            unordteams=pn.partition(pn.influence(net), nteams)
            teams=[] #order teams using indices from topo file
            for _ in range (len(unordteams)):
                for team in unordteams: 
                    if int(id_to_node[team[0]][0])==_+1:
                        teams.append(team)
                        
            ftot=[] #no. of flips for each simulation on given network
            ptot=[] #destination for each simulation on given network
            intot=[] #initial state for each simulation on given network
            destot=[] #actual destination for each simulation on given network
            htot=[] #initial-destination(actual) hamming for each simulation on given network
            inhtot=[] #initial-destination(desired) hamming for each simulation on given network
            
            netinits=[] #choose initial conditions which are steady on given network
            for state in inconfigs:
                if state=='other' or str(art.makeinistate(net, teams, state, False,True))!='error':
                    netinits.append(state)
                
            
            for init in netinits: 
                
                if init!='other':  #create steady non-hybrid initial state         
                    ini=art.makeinistate(net, teams, init, False,True) 
                    inclass=init
                    
                else: #create random hybrid initial state that is steady
                    while True:
                        ini=bf.randomstate(len(net), False)
                        if bf.issteady(ini, net, False)==True:
                            inclass=pn.classify(ini, teams)
                            if inclass not in dests:
                                break
                    
                        
                for dest in dests: #simulate for all given directions
                    
                    permissible=[] #generate set of flippable nodes
                    desti=art.makeinistate(net, teams, dest, False,False)
                    for node in range(len( desti)):
                        if desti[node]!=ini[node]:
                            permissible.append(node)
                    
                    inham=pn.hamming(ini, desti)
                    
                    f,p,h=sw.perturbsim(ini, 100, permissible, net, teams,False,mt)
                        
                    ftot+=f
                    ptot+=p
                    htot+=h
                    
                    if len(f)!=0: #check if switching has occurred atleast once
                        for flip in f:
                            intot.append(inclass)
                            destot.append(dest)
                            inhtot.append(inham)
                            
            flips[i-2].append(ftot)
            phens[i-2].append(ptot)
            inits[i-2].append(intot)
            destins[i-2].append(destot)
            hams[i-2].append(htot)
            inhams[i-2].append(inhtot)
                        
    return flips,phens,dens,inits,destins ,hams,inhams
              
data=[]
cwd=os.getcwd()
nteamslist=[2,3] #list of nteams parameters
size=5 #size per team
weight=1 #edge weight (do not change)
mt=False #multithreading (change to True if desired)
destslist=[['01'],['001','011']]
initslist=[['10','other'],['100','010','110','101','other']]
for _ in range(0,2): #generate data for all parameter sets
    flips,phens,dens,ins,destins,hams,inhams=main(nteamslist[_],size,weight,initslist[_],destslist[_],mt)  
    for den in range(len(dens)):
        for net in range(len(flips[den])):
            for i in range(len(flips[den][net])):
                data.append([nteamslist[_],ins[den][net][i],dens[den],net,flips[den][net][i],phens[den][net][i],destins[den][net][i],hams[den][net][i],inhams[den][net][i]])

cols=["#teams","initial","density","network index","#flips","destination","direction","dest-dir hamming","init-dir hamming"]
netdata=pd.DataFrame(data,columns=cols)
cwd=os.getcwd()
os.chdir(cwd+"//switch_data")
netdata.to_csv((os.getcwd()+"//directed_random_"+str(size)+".csv"),sep=',',index=False)