import pandas as pd
import csv
import os
import gc


def GetEdges(G):
    E = G.drop_duplicates()  # Dropping duplicate edges, in case two vertices connect more than once per T
    E = E.reset_index(drop=True)  # Resetting indices after dropping duplicate edges
    return E


def SaveEdges(E, i):
    with open("EdgesSet-" + str(i) + ".csv", "w") as f:  # Save edge list in csv file
        w = csv.writer(f)
        for j in range(len(E.index)):  # writing edges in rows one by one
            w.writerow(E.iloc[j, :])


def GetVertices(G):
    G.columns = ["src", "dst"]
    V = set()  # Creating empty set for vertices
    V.update(G.src.tolist(), G.dst.tolist())
    # Updating set with vertices from src & dst where duplicates are automatically dropped
    return V


def SaveVertices(V, i):
    with open("VerticesSet-" + str(i) + ".csv", 'w') as f:  # Vertices set in csv file
        csv.writer(f).writerow(V)


def nVandnE(N):
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
            E = GetEdges(G)
            SaveEdges(E, i)
            V = GetVertices(G)
            SaveVertices(V, i)
            nE.append(len(E.index))
            nV.append(len(V))
            del G, E, V
            gc.collect()
    return nV, nE
