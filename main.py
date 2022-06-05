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
net = pd.read_csv("a.txt", sep=" ", header=None)
net.columns = ["src", "dst", "tstamp"]  # Labeling columns for easier data manipulation
net = net.sort_values(by=['tstamp'])  # Order data chronologically
net = net.reset_index(drop=True)  # Resetting indices after reordering
print(net)

# Getting N ------------------------------------------------------------------------------------------------------------
N = int(input('Please enter N: '))
while True:  # Input conflict (In case user inputs an invalid value)
    if N <= 0:
        N = int(input('Please enter a valid N: '))
    else:
        break

# Time Partition -------------------------------------------------------------------------------------------------------
t_min, t_max, t = P1Q1.TPartition(net, N)
print("\nt_min: %s\nt_max:" % t_min, t_max)
print('t:', t)

# Subgraphs' Edge list creation ----------------------------------------------------------------------------------------
Sub = P1Q2.SubGraph(N)
Sub.SubgraphEdgeLists(net, t)
del net, t
gc.collect()

# Subgraphs' Adjacency Lists Creation ----------------------------------------------------------------------------------
Sub.AdjList()

# Edges and Vertices of each subgraph ----------------------------------------------------------------------------------
nV = list()  # To get the number of vertices in every time interval
nE = list()  # To get the number of edges in every time interval
for i in range(1, N + 1):
    fname = "Edges-" + str(i) + ".txt"
    if os.stat(fname).st_size == 0:  # In case some time intervals have empty Subgraphs
        nE.append(0)  # The number of both vertices & edges is 0
        nV.append(0)
        open("VerticesSet-" + str(i) + ".csv", 'w').close()
        open("EdgesSet-" + str(i) + ".csv", 'w').close()
    else:
        G = pd.read_csv(fname, sep=' ', header=None)
        E = P1Q3_1.GetEdges(G)
        P1Q3_1.SaveEdges(E, i)
        V = P1Q3_1.GetVertices(G)
        P1Q3_1.SaveVertices(V, i)
        nE.append(len(E.index))
        nV.append(len(V))
        del G, E, V
        gc.collect()

# |V| and |E| time evolution Graph -------------------------------------------------------------------------------------
P1Q3_2.GraphVandE(nE, nV)
# P1Q3_2.PlotHisto(nV, nE).HistogramVandE()
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

# PART II --------------------------------------------------------------------------------------------------------------

# V* and E* sets -------------------------------------------------------------------------------------------------------
VEstar = P2Q1.VstarEstar(N)
VEstar.VandEstar()

# |V*| and |E*| time evolution Graph -----------------------------------------------------------------------------------
VEstar.GraphVandEstar()

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
print('\n---- Training Accuracy ---- Descending Order')
print(ACCListTrain)
'''for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
    print('Best', x, 'Train Accuracy is', ACCListTrain[x], 'In', RList[x])'''

# ACC for Testing Graphs -----------------------------------------------------------------------------------------------
print('\n----- Testing Accuracy ----- Descending Order')
ACCListTest = P3Q3.TestACC(N, RList)
print(ACCListTest)
'''for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
    print(x, 'Test Accuracy is', ACCListTest[x], 'In', RList[x])'''

# Plotting ACC Results -------------------------------------------------------------------------------------------------
P3Extra.HistACC(ACCListTrain, ACCListTest)
P3Extra.Hist(ACCListTrain, 'Train')
P3Extra.Hist(ACCListTest, 'Test')
