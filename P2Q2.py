import itertools as it
import networkx as nx
import pandas as pd


def Similarities(N):
    for i in range(1, N):
        Vstar = list(pd.read_csv('Vstar%s.csv' % i))
        G = nx.read_edgelist('Estar[j-1,j]' + str(i) + '.csv')
        G.add_nodes_from(Vstar)
        CN(i, G, Vstar)
        JC(i, G, Vstar)


def CN(i, G, Vstar):
    Scn = pd.DataFrame(0, index=Vstar, columns=Vstar)  # Initializing the Scn with zeros
    for u in Vstar:
        for v in Vstar:
            Scn.loc[u, v] = len(list(nx.common_neighbors(G, u, v)))  # The number of common  neighbors
    fname = "Scn_Estar[j-1, j]" + str(i) + '.csv'
    with open(fname, "w") as f:
        Scn.to_csv(f)


def JC(i, G, Vstar):
    Sjc = pd.DataFrame(0, index=Vstar, columns=Vstar)  # Initializing the Scj with zeros
    jc = nx.jaccard_coefficient(G)
    for u, v, c in jc:
        Sjc.loc[u, v] = c
        Sjc.loc[v, u] = c  # The neighbors for u and v will be the same regardless of the direction of the edge
    fname = "Sjc_Estar[j-1, j]" + str(i) + '.csv'
    with open(fname, "w") as f:
        Sjc.to_csv(f)
