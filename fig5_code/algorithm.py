'''import required libraries'''
import numpy as np
import pandas as pd
import numpy.linalg as lin
import os

def make_dir(new_dir): 
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    return "made dir " + str(new_dir)

def maxpositiverun_df(array):
    '''Returns a subset of input dataframe, containing only non-negative values.
        
        Parameters
        ----------
        array: dataframe
            the dataframe needs to be sorted by values beforehand.
        
        Returns
        --------
        stretcharray: list
            the list of longest non-negative piece'''
    maxvalue=0
    stretcharray=[]
    stretches=[]
    counterr=0
    for n in range(len(array)):   
        if array[n]>=0:
            counterr+=1
            if counterr>maxvalue:
                maxvalue=counterr
            stretches.append(array[n])
        else:
            counterr=0
            
            stretches=[]
        if len(stretches)>0:    
            stretcharray.append(stretches)    
    
    return stretcharray

def maxnegativerun_df(array):
    '''Returns a subset of input dataframe, containing only negative values.
        
        Parameters
        ----------
        array: dataframe
            the dataframe needs to be sorted by values beforehand.
        
        Returns
        --------
        stretcharray: list
            The list of longest negative piece'''
    maxvalue=0
    stretcharray=[]
    stretches=[]
    counterr=0
    for n in range(len(array)):
        
        if array[n]<0:

            counterr+=1
            if counterr>maxvalue:
                maxvalue=counterr
            stretches.append(array[n])
        else:
            counterr=0
            
            stretches=[]
        if len(stretches)>0:    
            stretcharray.append(stretches)    
    
    return stretcharray  

def create_df_w_eigenvector(matrix):
    df= pd.DataFrame(columns= ["nodes", "eigen coeffs"])
    df["nodes"]= np.arange(0, matrix.shape[0])
    eig_vals= lin.eig(matrix)[0]
    eig_vals_filt=[i for i in eig_vals if i.imag==0]
    try:
        dom_eig_val= max(eig_vals_filt)
    except ValueError:
        print("no dom eig vector")
        return df
    
    index= [i for i in range(0,len(eig_vals)) if eig_vals[i]==dom_eig_val]
    vector= lin.eig(matrix)[1].T[index[0]].real

    if len(vector)==1:
        df["eigen coeffs"]= np.array(vector)[0]
    else:
        df["eigen coeffs"]= lin.eig(matrix)[1].T[index[0]].real

    return df

def remove_nodes_from_graph(Adj, array_w_nodes):
    new_adj= np.delete(Adj, array_w_nodes, 1)
    new_adj= np.delete(new_adj, array_w_nodes, 0)
    return new_adj

def get_nodes_from_graph(Adj, array_w_nodes):
    '''Returns adj_matrix of induced subgraph of given set of nodes.
        
        Parameters
        ----------
        Adj: matrix
            the adj_matrix of the main graph
        array_w_nodes: list
            the indices of nodes, whose induced subgraph is needed.
        
        Returns
        --------
        new_adj: list
            the induced subgraph.'''
    nodes= np.arange(0, len(Adj)).tolist()
    nodes_to_remove= [k for k in nodes if k not in array_w_nodes]
    new_adj= remove_nodes_from_graph(Adj, nodes_to_remove)
    return new_adj 

def team_segregate(Adj):
    '''Returns lists that segregate the nodes into two "teams".
        
        Parameters
        ----------
        Adj: matrix
            the input matrix.
        
        Returns
        --------
        [team1, team2]: [list,list]
            each entry is the list of indices of nodes belogning to one team in one iteration'''
    
    df= create_df_w_eigenvector(Adj)
    d=maxpositiverun_df(df.sort_values("eigen coeffs")["eigen coeffs"].values)
    if len(d)==0:
        data1=[]
        print("no eig vector")
    else:
        data1= np.array(maxpositiverun_df(df.sort_values("eigen coeffs")["eigen coeffs"].values)[0])
    d=maxnegativerun_df(df.sort_values("eigen coeffs")["eigen coeffs"].values)
    if len(d)==0:
        data2=[]
        print("no eig vector")
    else:
        data2= np.array(maxnegativerun_df(df.sort_values("eigen coeffs")["eigen coeffs"].values)[0])

    team1= [i for i in range(len(df.values[:,1])) if df.values[:,1][i] in data1]
    team2= [i for i in range(len(df.values[:,1])) if df.values[:,1][i] in data2]

    return [team1, team2]

def check_edge_criteria(matrix):
    '''Returns if the input matrix contains negative edges.
    
        Parameters
        ----------
        matrix: matrix
            the input matrix.
        
        Returns
        --------
        True/ False : Boolean
            if the matrix contains, returns false; else returns true.'''
    x, y= len(matrix),len(matrix)
    for i in range(x):
        for j in range(y):
            if matrix[i][j]==-1:
                return False
    return True

def iteratively_perform_sort(Adj):
    '''Returns final team segration after multiple iterations of algorithm.
    
        Parameters
        ----------
        Adj: matrix
            the input matrix.
        
        Returns
        --------
        filtered_teams : list
            list of all the predicted teams; each entry contains the indices of nodes segreated into one team.'''
    teams= team_segregate(Adj)
    filtered_teams= []

    for i in range(50):
        if len(teams)==0:
            print("done")
            return filtered_teams
        else:
            team= teams[0]
            teams.pop(0)
            new_nodes= team.copy()
            new_adj= get_nodes_from_graph(Adj, team)

            if not check_edge_criteria(new_adj):

                new_teams= team_segregate(new_adj)
                new_team1= [new_nodes[k] for k in new_teams[0]]
                new_team2= [new_nodes[k] for k in new_teams[1]]

                teams.append(new_team1)
                teams.append(new_team2)

            else: 
                filtered_teams.append(new_nodes)
        
    return filtered_teams