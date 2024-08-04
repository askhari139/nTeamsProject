import numpy as np
import pandas as pd
import numpy.linalg as lin

def generate_n_team_matrix(team_size_array):
    '''Returns a matrix with desired team structure; density 1.
        
        Parameters
        ----------
        teamsizearray: list
            i_th entry of the list is the size of the i_th team.
        
        Returns
        --------
        Adj_matrix: list
            Desired adjenceny matrix.
        array_ranges: list
            i_th entry of this list contains the indices of nodes belonging to the i_th team.'''
    Shape= sum(team_size_array)

    array_ranges= []
    for i in range(len(team_size_array)):
        sum_uptil_i= sum(team_size_array[0:i])
        if i==0:
            array_ranges.append(np.arange(0,team_size_array[i]))
        if i==len(team_size_array)-1:
            array_ranges.append(np.arange(sum_uptil_i+team_size_array[i-1], Shape))
        else:
            array_ranges.append(np.arange(sum_uptil_i+team_size_array[i], sum_uptil_i+team_size_array[i]+team_size_array[i+1]))
        
    Adj_matrix= np.ones(shape=(Shape, Shape))
    Adj_matrix= -Adj_matrix

    for i in range (0,Shape):
        for j in range (0,Shape):
            for k in np.arange(0,len(array_ranges)-1):
                if i in array_ranges[k] and j in array_ranges[k]:
                    Adj_matrix[i,j]=1
    

    return Adj_matrix, array_ranges

def count_edges_in_box(matrix, x, y):
    count=0
    for i in range(x[0],x[1]):
        for j in range(y[0], y[1]):
            if matrix[i,j]!=0:
                count+=1
    return count

def remove_edges_in_box(matrix, x, y, density):
    Adj= matrix
    count_team= count_edges_in_box(Adj, x, y)
    edges_to_remove= int(np.ceil(count_team* (1-density)))

    for edge in range(edges_to_remove):
        i_del= np.random.randint(x[0], x[1])
        j_del= np.random.randint(y[0], y[1])
        if Adj[i_del, j_del]!=0:
            Adj[i_del,j_del]=0
        count_team= count_edges_in_box(Adj, x, y)
        edges_to_remove= np.ceil(count_team* (1-density/2))
    return Adj
    
def generate_n_team_matrix_sparse(team_array, density_matrix):
    '''Returns a matrix with desired team structure; any density.
        
        Parameters
        ----------
        teamsizearray: list
            i_th entry of the list is the size of the i_th team.
        density_matrix: matrix
            (i,j)_th entry is the density of edges going from i_th team to j_th team.
        
        Returns
        --------
        Adj: list
            Desired adjenceny matrix.
        array: list
            i_th entry of this list contains the indices of nodes belonging to the i_th team.'''
    Adj, array= generate_n_team_matrix(team_array)
    array_w_ranges=[]
    for i in range(len(array)):
        if len(array[i])>0:
            array_w_ranges.append([array[i][0],array[i][-1]+1])
        else:
            array_w_ranges.append([0,0])

    for i in range(len(array_w_ranges)-1):
        for j in range(len(array_w_ranges)-1):
            Adj= remove_edges_in_box(Adj, x=array_w_ranges[i], y=array_w_ranges[j], density=density_matrix[i,j])
    
    return Adj, array