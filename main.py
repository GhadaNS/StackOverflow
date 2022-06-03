import pandas as pd
import networkx as nx
import P1Q1
import P1Q2
import P1Q3_1
import P1Q3_2
import P1Q4
import P2Q1
import P2Q2
import P3Q1
import gc
import os

# Reading the edges' set file ------------------------------------------------------------------------------------------
net = pd.read_csv('a.txt', sep=" ", header=None)
net.columns = ["src", "dst", "tstamp"]  # Labeling columns for easier data manipulation
net = net.sort_values(by=['tstamp'])  # Just in case Edges aren't ordered by time stamp
net = net.reset_index(drop=True)  # Resetting indices after reordering
print(net)

# Getting N ------------------------------------------------------------------------------------------------------------
N = int(input('Please enter N: '))
while True:  # Input conflict (In case user inputs an invalid value
    if N <= 0:
        N = int(input('Please enter a valid N: '))
    else:
        break

# Time Partition -------------------------------------------------------------------------------------------------------
t_min, t_max, t = P1Q1.TPartition(net, N)
print("t_min %s\nt_max" % t_min, t_max)
print('T', t)

# Subgraphs' Edge list creation ----------------------------------------------------------------------------------------
Sub = P1Q2.SubGraph(N)
Sub.SubgraphEdgeLists(net, t)
del net, t
gc.collect()

# Subgraphs' Adjacency Matrices Creation -------------------------------------------------------------------------------
"""for i in range(1, N + 1):
    fname = "Edges-" + str(i) + ".txt"
    if os.stat(fname).st_size != 0:  # File is not empty
        G = pd.read_csv(fname, sep=' ', header=None)"""
# Sub.AdjMAt()

# Subgraphs' Adjacency Lists Creation ----------------------------------------------------------------------------------
# Sub.AdjList()

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
# P1Q3_2.GraphVandE(nE, nV)
# P1Q3_2.PlotHisto(nV, nE).HistogramVandE()
del nV, nE
gc.collect()

# Centrality Measures --------------------------------------------------------------------------------------------------
for i in range(1, N + 1):
    fname = "Edges-" + str(i) + ".txt"
    if os.stat(fname).st_size != 0:
        G = nx.read_edgelist(fname)  # Reading the graph from previously created edge list
        # P1Q4.Cent(G, i)
        del G
        gc.collect()

# V* and E* sets -------------------------------------------------------------------------------------------------------
VEstar = P2Q1.VstarEstar(N)
VEstar.VandEstar()

# |V*| and |E*| time evolution Graph -----------------------------------------------------------------------------------
# VEstar.GraphVandEstar()

# Similarity Matrices --------------------------------------------------------------------------------------------------
P2Q2.Similarities(N)

# ACC Function ---------------------------------------------------------------------------------------------------------
for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
    ESet = 'Estar[j-1,j]'
    AcObj = P3Q1.AccFunc(N, x, ESet)
    R = AcObj.PrvSimVal()
    RMin, RMax = IdMin, IdMax = 0, len(R) - 1  # Min and Max values indices of R
    ACC_best = AcObj.ACC((R[IdMin], R[IdMax]))
    i = 0
    ACC_best1 = ACC_best
    while IdMin < IdMax - 1:
        ACC = AcObj.ACC((R[IdMin + 1], R[IdMax]))
        if ACC > ACC_best:
            ACC_best = ACC
            RMin = IdMin + 1
        ACC = AcObj.ACC((R[IdMin], R[IdMax - 1]))
        if ACC > ACC_best:
            ACC_best = ACC
            RMax = IdMax - 1
        ACC_best2 = ACC_best
        if ACC_best1 == ACC_best2:  # To stop the while loop once the maximum accuracy isn't changing anymore
            break
        else:
            ACC_best1 = ACC_best2
        IdMin += 1
        IdMax -= 1
        i += 1
    y = 'R' + x  # Rx* name for each Similarity Measurement
    exec("y = (R[RMin], R[RMax])")  # Applying the value to the name
    print('Best', x, 'Accuracy is', ACC_best, 'In', (R[RMin], R[RMax]))
    print('From', AcObj.AccList, '\n')
