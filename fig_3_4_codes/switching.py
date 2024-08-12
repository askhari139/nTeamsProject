import random
import boolean_formalism as bf
import phenotype as pn
import multiprocessing as mp

def pertrep(mat,ini,permissible,teams,zero): #individual sequential perturbation experiment
    
    strini=bf.statetostring(ini) #convert initial state to a string
    icopy=ini.copy()
    flippednodes=[] #nodes flipped

    while True:
        flipnode=random.sample(permissible,1) #pick node to flip from list allowed nodes
        if len(flippednodes)==len(permissible):
            break
            
        if flipnode[0] not in flippednodes: #check if it hasnt been flipped already
            flippednodes.append(flipnode[0])
            
            icopy[flipnode[0]]=-icopy[flipnode[0]] if zero==False else (1-icopy[flipnode[0]]) #flip
            instate=[] 
            instate.append(icopy) 
            finstate=bf.sim(mat,instate,True,zero) #simulate from perturbed initial state till steady state reached
            if strini!=bf.statetostring(finstate[0]): #check if final state = initial state
                break
        
    return flippednodes,finstate[0]

                    
def perturbsim(ini,trials,permissible,mat,teams,zero,mt): #multiple repetitions of pertrep
    
    #mat: network adjacency matrix
    #trials: no. of repetitions
    #ini: initial state
    #permissible: list of nodes allowed to be flipped
    #teams: composition of teams for given network (contains a list for each team, in order of team index)
    #zero: True for 1/0 formalism, False for 1/-1 (Keep at False)
    #mt: True if multithreading desired, else False
    
    flips=[] #no. of flips for each repetition
    phens=[] #destination after each repetition
    hammings=[] #initial(unperturbed)-destination hamming corresponding to each repetition
    
    
    if mt==False: #no multithreading
        for k in range (trials):
            flippednodes,finstate=pertrep(mat,ini,permissible,teams,zero)
            flips.append(len(flippednodes))
            phens.append(pn.classify(finstate,teams))
            hammings.append(pn.hamming(finstate,ini))
            
    else: #multithread
        params=[[mat,ini,permissible,teams,zero] for k in range(trials)]
        with mp.Pool() as p:
            result=p.starmap(pertrep,params)
        for r in result:
            flips.append(len(r[0]))
            phens.append(pn.classify(r[1],teams))
            hammings.append(pn.hamming(r[1],ini))
                    
    return flips,phens,hammings  
          

def multipertrep(ini,mat,teams,nperts,zero): #individual strong perturbation experiment
    
    icopy=ini.copy()
    nodestoflip=[] #list of nodes to flip
    
    if type(nperts)==list: #if amount of perturbation is provided for each team
        for ind in range(len(teams)):
            nodestoflip+=random.sample(teams[ind],nperts[ind])
    else: #if pertubation is not team-specific
        nodestoflip=random.sample([i for i in range(len(mat))],nperts)
        
    for node in nodestoflip:
        icopy[node]=-icopy[node] if zero==False else (1-icopy[node]) #perturb initial state
    instate=[]
    instate.append(icopy) 
    finstate=bf.sim(mat,instate,True,zero) #simulate from perturbed state till steady state reached
    return finstate


def multipert(ini,trials,mat,teams,percperts,zero,mt): #multiple repetitions of multipertrep
    
    #mat: network adjacency matrix
    #trials: no. of repetitions
    #ini: initial state
    #percperts: list containing proportion of each team to be perturbed, or float for proportion of overall network to be perturbed (without team specificity)
    #teams: composition of teams for given network (contains a list for each team, in order of team index)
    #zero: True for 1/0 formalism, False for 1/-1 (Keep at False)
    #mt: True if multithreading desired, else False
    
    phens=[] #destination after each repetition
    nperts=[] #perturbation as no. of nodes
    hams=[] #initial(unperturbed)-destination hamming corresponding to each repetition
    
    if type(percperts)==list: #if perturbation proportions are provided for each team
        for i in range(len(teams)):
            nperts.append(int(percperts[i]*len(teams[i])))
    else: #if no team specificity in perturbation
        nperts=int(percperts*len(mat))
        
    if mt==False: #no multithreading
        for i in range(trials):
            finstate=multipertrep(ini,mat,teams,nperts,zero)
            phens.append(pn.classify(finstate[0],teams)) 
            hams.append(pn.hamming(finstate[0],ini))
            
    else: #multithreading
        params=[[ini,mat,teams,nperts,zero] for k in range(trials)]
        with mp.Pool() as p:
            result=p.starmap(multipertrep,params) #use multithreading to speed things up
        for finstate in result:
            phens.append(pn.classify(finstate[0],teams)) 
            hams.append(pn.hamming(finstate[0],ini))

    return phens,hams

