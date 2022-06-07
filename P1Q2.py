import pandas as pd
import P1Q3_1
import csv
import os
import gc


class SubGraph:

    def __init__(self, N):
        self.N = N

    def SubgraphEdgeLists(self, net, t):
        i = 0  # For iterating through df rows
        j = 1  # For iterating through "t" time list
        while j < self.N:  #
            i1 = i  # The index of the subgraph's first row
            while t[j - 1] <= net.tstamp[i] < t[j]:  # When 1 <= j < N
                i2 = i  # The index of the subgraph's last row
                i += 1  # We increment "i" as long as condition true, to keep all values within the interval
            fname = "Edges-" + str(j) + ".txt"
            with open(fname, "w") as f:  # Save edge list in txt file
                net.iloc[i1:i2 + 1, 0:2].to_csv(f, sep=" ", header=None, index=False)  # Writing only src & dst columns
            j += 1
        #  Once j == N, All the rest of the edges belong to the last subgraph
        i1 = i
        i2 = len(net.index) - 1
        fname = "Edges-" + str(j) + ".txt"
        with open(fname, "w") as f:
            net.iloc[i1:i2 + 1, 0:2].to_csv(f, sep=" ", header=None, index=False)

    def AdjLists(self):
        for i in range(1, self.N + 1):
            fname = "Edges-" + str(i) + ".txt"
            if os.stat(fname).st_size != 0:  # File is not empty
                G = pd.read_csv(fname, sep=' ', header=None)
                V = sorted(list(P1Q3_1.GetVertices(G)))  # Sorted list of vertices
                AdjList = dict.fromkeys(V, [])  # Dictionary with vertices as keys
                E = P1Q3_1.GetEdges(G)  # df of edges
                for key in AdjList:
                    AdjList[key] = E[E.src == key].dst.tolist()  # Adding to each dictionary key values of dst vertices
                with open("AdjList-" + str(i) + ".csv", "w") as f:  # Save Adjacency list as csv file
                    w = csv.writer(f)
                    A = [[key] + value for key, value in AdjList.items()]
                    w.writerows(A)
                del G, V, E, AdjList, A
                gc.collect()
