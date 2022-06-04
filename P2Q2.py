import networkx as nx
import pandas as pd
import os


def Similarities(N):
    for j in range(1, N):
        if os.stat('Vstar-%s.csv' % j).st_size == 0:  # In case some time intervals have empty Subgraphs
            for Sim in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:  # Create empty similarity matrices
                open(Sim + "_Estar[j-1,j]-" + str(j) + ".csv", 'w').close()
        else:
            Vstar = list(pd.read_csv('Vstar-%s.csv' % j))
            G = nx.read_edgelist('Estar[j-1,j]-' + str(j) + '.csv')
            G.add_nodes_from(Vstar)
            for Sim in [GD, CN, JC, A, PA]:
                Sim(j, G, Vstar)


def GD(j, G, Vstar):
    Sgd = nx.floyd_warshall_numpy(G)  # returns a numpy matrix with all shortest paths
    Sgd = pd.DataFrame(Sgd, index=Vstar, columns=Vstar)  # The matrix put into df with Vstar as indices & columns
    Sgd.to_csv('Sgd_Estar[j-1,j]-%s.csv' % j)


def CN(j, G, Vstar):
    Scn = pd.DataFrame(0, index=Vstar, columns=Vstar)  # Initializing the Scn with zeros & Vstar as indices & columns
    for u in Vstar:
        for v in Vstar:
            Scn.loc[u, v] = len(list(nx.common_neighbors(G, u, v)))  # The number of common  neighbors
    Scn.to_csv('Scn_Estar[j-1,j]-%s.csv' % j)


def JC(j, G, Vstar):
    Sjc = pd.DataFrame(0, index=Vstar, columns=Vstar)  # Initializing the Scj with zeros & Vstar as indices & columns
    jc = nx.jaccard_coefficient(G)  # Returns an iterator of tuples (u, v, c): u & v are nodes & c is their jc
    for u, v, c in jc:
        Sjc.loc[u, v] = c
        Sjc.loc[v, u] = c  # The neighbors for u and v will be the same regardless of the direction of the edge
    Sjc.to_csv('Sjc_Estar[j-1,j]-%s.csv' % j)


def A(j, G, Vstar):
    Sa = pd.DataFrame(0, index=Vstar, columns=Vstar)  # Initializing the Scj with zeros & Vstar as indices & columns
    AA = nx.adamic_adar_index(G)  # Returns an iterator of tuples (u, v, a): u & v are nodes & a is their aa
    for u, v, p in AA:
        Sa.loc[u, v] = p
        Sa.loc[v, u] = p  # The AA for u and v will be the same regardless of the direction of the edge
    Sa.to_csv('Sa_Estar[j-1,j]-%s.csv' % j)


def PA(j, G, Vstar):
    Spa = pd.DataFrame(0, index=Vstar, columns=Vstar)  # Initializing the Scj with zeros & Vstar as indices & columns
    pa = list(nx.preferential_attachment(G))  # Returns an iterator of tuples (u, v, p): u & v are nodes & p is their pa
    for u, v, p in pa:
        Spa.loc[u, v] = p
        Spa.loc[v, u] = p  # The PA for u and v will be the same regardless of the direction of the edge
    Spa.to_csv('Spa_Estar[j-1,j]-%s.csv' % j)
