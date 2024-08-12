import os 
import artificial as art
import boolean_formalism as bf

#generate networks of symmetric density with given parameters

size=5 #size of each team
weight=1 #edge weights ; keep at 1
nteams=2 #no. of teams in each network
nnets=100 #no. of networks

cwd=os.getcwd()
address=cwd+"//switch_data//network_data_"+str(size)
if os.path.exists(address)==False:
    os.mkdir(address)
    
ids=[i for i in range(0,size*nteams)] 
nodes=[]
for node in ids:
    nodes.append(str(int(node/size+1))+"_"+str(int(node%size)+1))
id_to_node=dict(zip(ids,nodes)) #create dictionary of node indices to node identities

#initialise network size and edge weights
sizes=[]
wts=[]
for i in range(nteams): 
    sizes.append(size)
    wts.append([])
    for j in range(nteams):
        wts[i].append(weight)

#make networks of uniform densities from 20% to 90% (increments of 10%)
for i in range(2,10):
    density=i/10
    densities=[]
    for a in range(nteams):
        densities.append([])
        for b in range(nteams):
            densities[a].append(density)
    
    check=0   
    time=0
    
    while check<nnets: #generate nnet random networks
        randmat, teams=art.multiteamnetwork(sizes, densities, wts) #generate network
        if art.peripheral(randmat)==0: #make sure initial state is steady
            filename=str(nteams)+'_'+str(size)+'_'+str(int(density*100))+"_"+str(check)+".topo"
            bf.write_topo(randmat, id_to_node, address+"//"+filename) #save network
            print(density,check)
            check+=1
            