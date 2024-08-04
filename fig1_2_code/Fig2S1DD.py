import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np

import boolean_smil
import state_classification as fsc
import ternary
plt.style.use("ggplot")


FigData=[["Team1","Team2","Team3","MeanFrust","StdFrust"]]

scale=15
#density_varying_0_1
den=0.9
total_ndoes=15
data=[]
values=[]
#This program partitions 15 into all possible sets and constructs a three team network with those sets as nodes. We then plot the mean frustration/mean of mean frustration of those networks, possibly making a heat map. 
frust_size=np.zeros((16,16))
for i in range(0,16):
    for j in range(0,16-i):
        k=15-(i+j)
        adj=nteams.nteam_net(3,[i,j,k],[[den,den,den],[den,den,den],[den,den,den]])[0]
    
        steadys=boolean_smil.steady_states(adj,10000)
        ssf=boolean_smil.steady_state_frequency(steadys,adj)
        frust_data=frustration.ensemble_frustration(steadys,adj)
        mean_frust=np.mean(frust_data)
        std_frust=np.std(frust_data)
        frust_size[i][j]=mean_frust

        data.append([i,j,k])

        FigData.append([i,j,k,mean_frust,std_frust])
        values.append(mean_frust)
values = np.array(values)
norm_values = (values - values.min()) / (values.max() - values.min())

# Create a ternary plot
figure, tax = ternary.figure(scale=scale)
tax.boundary(linewidth=2.0)
tax.gridlines(multiple=10, color="black", linestyle='--')

# Set axis labels and title
fontsize = 12
tax.left_axis_label("Team 1 size", fontsize=fontsize)
tax.right_axis_label("Team 2 size", fontsize=fontsize)
tax.bottom_axis_label("Team 3 size", fontsize=fontsize)
tax.set_title("Frustration for different sets of sizes Density {}".format(den), fontsize=15)

# Plot the heat map
for ((x, y, z), value) in zip(data, norm_values):
    tax.scatter([(x , y , z )], marker='o', color=plt.cm.plasma(value), s=50)
'''

import csv #FOR STORING DATA
with open('data/Figure2/Fig2S1D/Den9/FigData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData)



# Add a colorbar
'''
sm = plt.cm.ScalarMappable(cmap=plt.cm.plasma, norm=plt.Normalize(vmin=values.min(), vmax=values.max()))
sm._A = []
cbar = plt.colorbar(sm, ax=tax.get_axes(), orientation='vertical')
cbar.set_label('Frustration')

# Show the plot
tax.show()