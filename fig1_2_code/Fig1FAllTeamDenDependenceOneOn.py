import nteams
import frustration
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np
import datetime
import boolean_smil
from scipy import stats

plt.style.use("ggplot")
import state_classification as fsc


#Graph of percentage of states with one team on vs density for two teams and three teams 

path1="/home/vaibhav/ayaye/research/cancer_systems_biology_laboratory/2_3_teams/figure1_24/pure_percentage"

density=[]

numsim=10000



avg_freq_2=[]
std2=[]


avg_freq_3=[]
std3=[]


avg_freq_4=[]
std4=[]


avg_freq_5=[]
std5=[]


avg_freq_6=[]
std6=[]


avg_freq_7=[]
std7=[]



#Data Storage 
networks=[["NoTeams","Density","Adj"]]

FigData2=[["MeanFracOneOn","Std","Density"]]
FigData3=[["MeanFracOneOn","Std","Density"]]
FigData4=[["MeanFracOneOn","Std","Density"]]
FigData5=[["MeanFracOneOn","Std","Density"]]
FigData6=[["MeanFracOneOn","Std","Density"]]
FigData7=[["MeanFracOneOn","Std","Density"]]


TotFigData=[["MeanFracOneOn","Std","Density","NoTeams"]]


for i in np.linspace(0,0.99,10):
    density.append(i)
    freq3_dist=[]
    freq_3=0
    freq3_dist=[]

    freq2_dist=[]
    freq_2=0
    freq2_dist=[]


    freq4_dist=[]
    freq_4=0
    freq4_dist=[]


    freq5_dist=[]
    freq_5=0
    freq5_dist=[]

    freq6_dist=[]
    freq_6=0
    freq6_dist=[]


    freq7_dist=[]
    freq_7=0
    freq7_dist=[]



    count=0

    for j in range(0,50):
        count+=1

        adj_2=nteams.nteam_net(2,[5,5],[[i,i],[i,i]])[0]
        networks.append([2,i,adj_2])
        steadys_2=boolean_smil.steady_states(adj_2,numsim)
        ss_2=boolean_smil.steady_state_frequency(steadys_2,adj_2)
        data2=fsc.states_classification_ssf(2,[0,5,10],ss_2,adj_2)[-1]
        
        freq2_dist.append(data2)




        adj_3=nteams.nteam_net(3,[5,5,5],[[i,i,i],[i,i,i],[i,i,i]])[0]
        networks.append([3,i,adj_3])
        steadys_3=boolean_smil.steady_states(adj_3,numsim)
        ss_3=boolean_smil.steady_state_frequency(steadys_3,adj_3)
        data3=fsc.states_classification_ssf(3,[0,5,10,15],ss_3,adj_3)[-1]
        
        freq3_dist.append(data3)
        


        adj_4=nteams.nteam_net(4,[5,5,5,5],[[i,i,i,i],[i,i,i,i],[i,i,i,i],[i,i,i,i]])[0]
        networks.append([4,i,adj_4])
        steadys_4=boolean_smil.steady_states(adj_4,numsim)
        ss_4=boolean_smil.steady_state_frequency(steadys_4,adj_4)
        data4=fsc.states_classification_ssf(4,[0,5,10,15,20],ss_4,adj_4)[-1]
        
        freq4_dist.append(data4)


        adj_5=nteams.nteam_net(5,[5,5,5,5,5],[[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i],[i,i,i,i,i]])[0]
        networks.append([5,i,adj_5])
        steadys_5=boolean_smil.steady_states(adj_5,numsim)
        ss_5=boolean_smil.steady_state_frequency(steadys_5,adj_5)
        data5=fsc.states_classification_ssf(5,[0,5,10,15,20,25],ss_5,adj_5)[-1]
        
        freq5_dist.append(data5)

        adj_6=nteams.nteam_net(6,[5,5,5,5,5,5],[[i,i,i,i,i,i],[i,i,i,i,i,i],[i,i,i,i,i,i],[i,i,i,i,i,i],[i,i,i,i,i,i],[i,i,i,i,i,i]])[0]
        networks.append([6,i,adj_6])
        steadys_6=boolean_smil.steady_states(adj_6,numsim)
        ss_6=boolean_smil.steady_state_frequency(steadys_6,adj_6)
        data6=fsc.states_classification_ssf(6,[0,5,10,15,20,25,30],ss_6,adj_6)[-1]
        
        freq6_dist.append(data6)

        adj_7=nteams.nteam_net(7,[5,5,5,5,5,5,5],[[i,i,i,i,i,i,i],[i,i,i,i,i,i,i],[i,i,i,i,i,i,i],[i,i,i,i,i,i,i],[i,i,i,i,i,i,i],[i,i,i,i,i,i,i],[i,i,i,i,i,i,i]])[0]
        networks.append([7,i,adj_7])
        steadys_7=boolean_smil.steady_states(adj_7,numsim)
        ss_7=boolean_smil.steady_state_frequency(steadys_7,adj_7)
        data7=fsc.states_classification_ssf(7,[0,5,10,15,20,25,30,35],ss_7,adj_7)[-1]
        
        freq7_dist.append(data7)



        
    print(i,datetime.datetime.now())
    avg_freq_2.append(np.mean(freq2_dist))
    std2.append(np.std(freq2_dist))
    FigData2.append([np.mean(freq2_dist),np.std(freq2_dist),i])
    TotFigData.append([np.mean(freq2_dist),np.std(freq2_dist),i,2])



    avg_freq_3.append(np.mean(freq3_dist))
    std3.append(np.std(freq3_dist))
    FigData3.append([np.mean(freq3_dist),np.std(freq3_dist),i])
    TotFigData.append([np.mean(freq3_dist),np.std(freq3_dist),i,3])
    
    
    
    avg_freq_4.append(np.mean(freq4_dist))
    std4.append(np.std(freq4_dist))
    FigData4.append([np.mean(freq4_dist),np.std(freq4_dist),i])
    TotFigData.append([np.mean(freq4_dist),np.std(freq4_dist),i,4])

    
    avg_freq_5.append(np.mean(freq5_dist))
    std5.append(np.std(freq5_dist))
    FigData5.append([np.mean(freq5_dist),np.std(freq5_dist),i])
    TotFigData.append([np.mean(freq5_dist),np.std(freq5_dist),i,5])



    avg_freq_6.append(np.mean(freq6_dist))
    std6.append(np.std(freq6_dist))
    FigData6.append([np.mean(freq6_dist),np.std(freq6_dist),i])
    TotFigData.append([np.mean(freq6_dist),np.std(freq6_dist),i,6])

    
    avg_freq_7.append(np.mean(freq7_dist))
    std7.append(np.std(freq7_dist))
    FigData7.append([np.mean(freq7_dist),np.std(freq7_dist),i])
    TotFigData.append([np.mean(freq7_dist),np.std(freq7_dist),i,7])



#plt.plot(density,avg_freq_3, marker ="o", label="Three Teams")
#plt.plot(density,avg_freq_2, marker ="o", label="Two Teams")
#plt.plot(density,avg_freq_4, marker ="o", label="Four Teams")


'''import csv
with open('data/Figure1/Fig1F/Networks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(networks)

with open('data/Figure1/Fig1F/TwoTeam/OneTeamOnFinal.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData2)

with open('data/Figure1/Fig1F/ThreeTeam/OneTeamOnFinal.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData3)

with open('data/Figure1/Fig1F/FourTeam/OneTeamOnFinal.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData4)


with open('data/Figure1/Fig1F/FiveTeam/OneTeamOnFinal.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData5)


with open('data/Figure1/Fig1F/SixTeam/OneTeamOnFinal.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData6)

with open('data/Figure1/Fig1F/SevenTeam/OneTeamOnFinal.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(FigData7)

with open('data/Figure1/Fig1F/FinalFig1F.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(TotFigData)
'''

















plt.errorbar(density,avg_freq_2,std2, capsize=4, label="Two Teams",marker="o",alpha=0.5)
plt.errorbar(density,avg_freq_3,std3, capsize=4,label="Three Teams",marker="o",alpha=0.5)
plt.errorbar(density,avg_freq_4,std4, capsize=4,label="Four Teams",marker="o",alpha=0.5)
plt.errorbar(density,avg_freq_5,std5, capsize=4,label="Five Teams",marker="o",alpha=0.5)
plt.errorbar(density,avg_freq_6,std6, capsize=4,label="Six Teams",marker="o",alpha=0.5)
plt.errorbar(density,avg_freq_7,std7, capsize=4,label="Seven Teams",marker="o",alpha=0.5)

plt.legend()
plt.ylabel("Fraction of OneOn states")
plt.xlabel("Density")
plt.title("Density Dependence of Fraction of States with One Team On")
plt.legend(loc="upper left")
#plt.text(0.1,0.99, "p value(A)={}".format(pval))
plt.show()
