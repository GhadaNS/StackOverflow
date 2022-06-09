import pandas as pd
import networkx as nx
import P1Q1
import P1Q2
import P1Q3_1
import P1Q3_2
import P1Q4
import P2Q1
import P2Q2
import P3Q2
import P3Q3
import P3Extra
import gc
import os


# PART I ---------------------------------------------------------------------------------------------------------------

# Reading the edges' set file ------------------------------------------------------------------------------------------
net = pd.read_csv("C:/Users/naits/Documents/UnivPi/SN/sx-stackoverflow.txt", sep=" ", header=None)
net = net.iloc[:1001, :]  # First 10k Edges
net.columns = ["src", "dst", "tstamp"]  # Labeling columns for easier data manipulation
net = net.sort_values(by=['tstamp'])  # Order data chronologically
net = net.reset_index(drop=True)  # Resetting indices after reordering
print(net)

# Getting N ------------------------------------------------------------------------------------------------------------
N = input('Please enter \"N\" the number of the network\'s time partitions: ')
while True:  # Input conflict (In case user inputs an invalid value)
    if not N.isnumeric() or int(N) == 0:  # Input != number or Input == 0
        N = input('Please enter a valid N: ')  # Read input again
    else:
        break
N = int(N)

# Time Partition -------------------------------------------------------------------------------------------------------
t_min, t_max, t = P1Q1.TPartition(net, N)
print("\nt_min: %s\nt_max:" % t_min, t_max)
print('t:', t, '\n')

# Subgraphs' Edge list creation ----------------------------------------------------------------------------------------
Sub = P1Q2.SubGraph(N)
Sub.SubgraphEdgeLists(net, t)
del net, t
gc.collect()

# Subgraphs' Adjacency Lists Creation ----------------------------------------------------------------------------------
Sub.AdjLists()

# |V| and |E| time evolution Graph -------------------------------------------------------------------------------------
nV, nE = P1Q3_1.nVandnE(N)
P1Q3_2.GraphVandE(nE, nV)
print("---Plotting graph of |V[tj-1,tj]| and |E[tj-1,tj]| Time evolution finished---")
del nV, nE
gc.collect()

# Centrality Measures --------------------------------------------------------------------------------------------------
for i in range(1, N + 1):
    fname = "Edges-" + str(i) + ".txt"
    if os.stat(fname).st_size != 0:
        G = nx.read_edgelist(fname)  # Reading the graph from previously created edge list
        P1Q4.Cent(G, i)
        del G
        gc.collect()
print("---Plotting Centrality histograms finished---")

# PART II --------------------------------------------------------------------------------------------------------------

# V* and E* sets -------------------------------------------------------------------------------------------------------
VEstar = P2Q1.VstarEstar(N)
VEstar.VandEstar()

# |V*| and |E*| time evolution Graph -----------------------------------------------------------------------------------
VEstar.GraphVandEstar()
print("---Plotting graph of |V*[tj-1,tj+1]|, |E*[tj-1,tj]| and |E*[tj,tj+1]| Time evolution finished---")

# Similarity Matrices --------------------------------------------------------------------------------------------------
P2Q2.Similarities(N)

# PART III -------------------------------------------------------------------------------------------------------------

# Optimal Range Sets Rx* -----------------------------------------------------------------------------------------------
print('\n-- Optimal Range Sets Rx* --')
ACCListTrain, RList = P3Q2.TrainACC(N)
print(RList)
'''for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
    print('Best', x, 'Rx* is', RList[x])'''

# ACC for Training Graphs ----------------------------------------------------------------------------------------------
print('\n---- Training Accuracy ---- Ranked from highest to lowest')
print(ACCListTrain)
'''for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
    print('Best', x, 'Train Accuracy is', ACCListTrain[x], 'In', RList[x])'''

# ACC for Testing Graphs -----------------------------------------------------------------------------------------------
print('\n----- Testing Accuracy ----- Ranked from highest to lowest')
ACCListTest = P3Q3.TestACC(N, RList)
print(ACCListTest)
'''for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
    print(x, 'Test Accuracy is', ACCListTest[x], 'In', RList[x])'''

# Plotting ACC Results -------------------------------------------------------------------------------------------------
P3Extra.HistACC(ACCListTrain, ACCListTest)
print("\n---Plotting Accuracy bar chart finished---")
P3Extra.Hist(ACCListTrain, 'Train')
print("---Plotting Training Accuracy histogram finished---")
P3Extra.Hist(ACCListTest, 'Test')
print("---Plotting Testing Accuracy histogram finished---")
