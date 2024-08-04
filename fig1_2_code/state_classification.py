import boolean_smil
import nteams
import frustration


#This program is supposed to calculate the percentage and perhaps even seggregate the pure states from hybrid states. 

def state_classification(noteams,team_indices, state,adj):
    #team_indices is a list having start indices of each team and its assumed that a single team is between two indices, the end index must be included in this 
    #nteams must = len(team_indices)
    
    #This outputs the state followed by boolean value indicating whether its a pure state or not
    n=noteams
    
    nteam_on=0

 
    team_on_list=[]
    noteam_on_scores =[]



    for i in range(0,n):

        team_on_count=0
        team_size=team_indices[i+1]-team_indices[i]
        for j in range(team_indices[i],team_indices[i+1]):
            

            if state[j]==1:
                team_on_count+=1
        if team_on_count==team_size:
            nteam_on+=1
            team_on_list.append(i+1)  #Min team is team 0
        elif team_on_count!=team_size and team_on_count!=0:
            noteam_on_scores.append(team_on_count)
    
    
    output=0
    if nteam_on==1 and len(noteam_on_scores)==0:
        output=1
    return(state,output)

def states_classification(noteams,team_indices,states,adj):
    pure_states=[]
    other_states=[]

    for i in states:
        output=state_classification(noteams,team_indices,i,adj)
        if output[1]==1:
            #print(output)


            pure_states.append(i)
            #print("pure_states:", pure_states)
            #print("----------------------")
        else:
            
            #print(output)
            other_states.append(i)
            #print("Other states", other_states)    
            #print("---------------")
    total_states=len(states)
    pure_fraction=len(pure_states)/total_states
    return(pure_states,other_states,pure_fraction)

#Funtion to classify which team is on in pure states 

def team_on_data(noteams,team_indices,states,adj):

    #Given an input of single positive states, it outputs the index of team which is on (starting from 1)

    data=states_classification(noteams,team_indices,states,adj)
    purefac=data[-1]
    pure_states=data[0]
    #now we check the pure states
    team_on_list=[]
    for state in pure_states:
        
        n=noteams
        
        nteam_on=0

    
        team_on=0
        noteam_on_scores =[]


           #Index for team is i

        for i in range(0,n): #n iterations for n teams i=0 is team 1

            team_on_count=0  #Counter for number of nodes on in a team
            team_size=team_indices[i+1]-team_indices[i]

    
            for j in range(team_indices[i],team_indices[i+1]):
                

                if state[j]==1:
                    team_on_count+=1
            if team_on_count==team_size:
                nteam_on+=1
                team_on=i+1  #Min team is team 1

        
                team_on_list.append(team_on)
    return(team_on_list)


def pure_teamon_freq(noteams,team_indices,steadys,adj):
    #It outputs the frequency of different teams being on. 
    tot_freq=len(steadys)

    data=team_on_data(noteams,team_indices,steadys,adj)
    team_on_ssf=boolean_smil.steady_state_frequency(data,adj)
    for i in range(0,len(team_on_ssf[0])):
        if tot_freq!=0:
            team_on_ssf[1][i]=team_on_ssf[1][i]/tot_freq
        else:
            team_on_ssf[1][i]=0
    return(team_on_ssf)




def states_classification_ssf(noteams,team_indices,ssf,adj):
    #this acts on the steady state distribution, hope it gives correct results. 

    total_states=len(ssf[0])
    pure_freq=0
    pure_states=[]
    pure_state_freq_dist=[]
    
    total_freq=0
    for i in ssf[1]:
        total_freq+=i
    
    for i in range(0,total_states):
        if state_classification(noteams,team_indices, ssf[0][i], adj)[-1]==1:
            pure_freq+=ssf[1][i]
            pure_states.append(ssf[0][i])
            pure_state_freq_dist.append(ssf[1][i])
    if total_freq!=0:
        purefrac=pure_freq/total_freq
    else:
        purefrac=0
    return([pure_states,pure_state_freq_dist],purefrac)

#--------------------------------------- 
#The above program only looks for states having one team on
#Now we look for states having any number of teams on and differentiate them from hybrid states



def nteams_on(noteams,team_indices, state,adj):
    #team_indices is a list having start indices of each team and its assumed that a single team is between two indices, the end index must be included in this 
    #nteams must = len(team_indices)
    
    #This outputs the number of teams which are on if the state isn't hybrid else it returns that it is a hybrid state
    
    n=noteams
    
    nteam_on=0

 
    team_on_list=[] #Keeps track of which teams are on
    noteam_on_scores =[] #+x if the team is hybrid where x is the number of on nodes


    for i in range(0,n):

        team_on_count=0
        team_size=team_indices[i+1]-team_indices[i]
        for j in range(team_indices[i],team_indices[i+1]):
            

            if state[j]==1:
                team_on_count+=1
        if team_on_count==team_size:
            nteam_on+=1
            team_on_list.append(i+1)  #Min team is team 0
        elif team_on_count!=team_size and team_on_count!=0:
            noteam_on_scores.append(team_on_count)
    
    
    output=[0,0] #First index of the list indicates the number of teams which are on and the second index indicates if the state is hybrid or not. Not hybrid =0 , hybrid =1
    output[0]=nteam_on

    if len(noteam_on_scores)==0:
        output[1]=0
    else:
        output[1]=1
    return(state,output)

def nteam_on_hybrid_dist(noteams,team_indices,ssf,adj):
    #this acts on the steady state distribution, hope it gives correct results. 

    total_states=len(ssf[0])
    n=noteams
    nteam_on_freq=[0 for i in range(0,n+2)] #i'th entry has i teams on and n+1 th entry has hybrid states

   
    total_freq=0
    for i in ssf[1]:
        total_freq+=i
    
    for i in range(0,total_states):
        data=nteams_on(noteams,team_indices, ssf[0][i], adj)[-1]
        if data[1]==1:
            if total_freq!=0:
                nteam_on_freq[n+1]+= (ssf[1][i]/total_freq)
        elif data[1]==0:
            if total_freq!=0:
                nteam_on_freq[data[0]]+=ssf[1][i]/total_freq
            
    return(nteam_on_freq)

def bar_plot_xaxis(frequencies):
    xax=[]
    for i in range(len(frequencies)):
        if i!=len(frequencies)-1:
            xax.append("{}_Team_On".format(i))
        else:
            xax.append("Hybrid")
    return(xax)


'''import nteams
import boolean_smil
d=0.8

adj=nteams.nteam_net(3,[5,5,5],[[d,d,d],[d,d,d],[d,d,d]])[0]

steadys=boolean_smil.steady_states(adj,1000)
ssf=boolean_smil.steady_state_frequency(steadys,adj)
print(pure_teamon_freq(3,[0,5,10,15],steadys,adj))
print(ssf)
'''
