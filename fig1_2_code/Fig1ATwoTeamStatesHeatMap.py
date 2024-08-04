import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nteams
import boolean_smil
def generate_matrix(N):
    """Generate an N x N matrix with values ranging from -1 to 1."""
    return np.random.uniform(-1, 1, (N, N))

def plot_heatmap(matrix):
    """Plot a heatmap of the given matrix."""
    plt.figure(figsize=(8, 6))
    ax=sns.heatmap(matrix, annot=False, cmap='coolwarm', center=0)
    plt.title('Steady States of a Two Team Network')
    plt.xlabel('Nodes')
    plt.ylabel('Steady States')
    frame1 = plt.gca()
    #frame1.axes.xaxis.set_ticklabels([])
    plt.tick_params(left = False) 
    colorbar = ax.collections[0].colorbar

    # Customize the color bar labels
    colorbar.set_ticks([-1,  1])
    colorbar.set_ticklabels(['State= 1',  'State= -1'])
    colorbar.ax.invert_yaxis()  # Ensure label 1 is at the top and label 2 at the bottom

    frame1.axes.yaxis.set_ticklabels([])
    plt.show()

d=0.3
adj=nteams.nteam_net(2,[5,5],[[d,d],[d,d]])[0]
# Example usage
steadys=boolean_smil.steady_states(adj,10000)
ssf=boolean_smil.steady_state_frequency(steadys,adj)
mat=[]
nstead=len(ssf[0])
for i in range(0,nstead):
    for j in range(0,ssf[1][i]):
        mat.append(ssf[0][i])

N = 10  # Change this value to the desired matrix size
matrix = generate_matrix(N)
print(mat)


'''import csv

data=[["Steady States"]]

for i in mat:
    data.append("{}".format(i))

with open('data/Figure1/Figure1ATwoTeamSteadyStates.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
'''


plot_heatmap(mat)
