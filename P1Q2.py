import pandas as pd
import P1Q3_1
import csv
import os


class SubGraph:

    def __init__(self, N):
        self.N = N

    """def PrintMatrix(self, mat):
        # Loop over all rows
        for k in range(0, len(mat)):
            print("[", end="")
            # Loop over each column in row i
            for t in range(0, len(mat[k])):
                # Print out the value in row i, column j
                print(mat[k][t], end="")
                # Only add a tab if we're not in the last column
                if t != len(mat[k]) - 1:
                    print("\t", end="")
            print("]\n")"""

    def SubgraphEdgeLists(self, net, t):
        i = 0  # For iterating through df rows
        j = 1  # For iterating through "t" time list
        while j < self.N:  #
            i1 = i  # The index of the subgraph's first row
            while t[j - 1] <= net.tstamp[i] < t[j]:  # When 1 <= j < N
                i2 = i  # The index of the subgraph's last row
                i += 1
            fname = "Edges-" + str(j) + ".txt"
            with open(fname, "w") as f:
                net.iloc[i1:i2 + 1, 0:2].to_csv(f, sep=" ", header=None, index=False)  # Writing only src & dst columns
            j += 1
        i1 = i
        while i < len(net.index) and t[j - 1] <= net.tstamp[i] <= t[j]:  # When j == N
            i2 = i
            i += 1
        fname = "Edges-" + str(j) + ".txt"
        with open(fname, "w") as f:
            net.iloc[i1:i2 + 1, 0:2].to_csv(f, sep=" ", header=None, index=False)

    def AdjMAt(self):
        for i in range(1, self.N + 1):
            fname = "Edges-" + str(i) + ".txt"
            if os.stat(fname).st_size != 0:  # File is not empty
                G = pd.read_csv(fname, sep=' ', header=None)
                V = sorted(list(P1Q3_1.GetVertices(G)))
                Map = {}  # Mapping the list of Vertices from user IDs to a sequence of integers
                k = 0  # so we can create the adjacency matrix
                for vertex in V:
                    Map[vertex] = k
                    k += 1
                E = P1Q3_1.GetEdges(G)
                E = E.applymap(lambda x: Map[x])
                N = len(V)
                Mat = [[0] * N for _ in range(N)]
                for j in range(len(E.index)):
                    u = E.src[j]
                    v = E.dst[j]
                    Mat[u][v] = 1
                with open("AdjMat" + str(i) + ".csv", "w") as f:
                    w = csv.writer(f)
                    for j in range(len(Mat)):
                        w.writerow(Mat[j])

    def AdjList(self):
        for i in range(1, self.N + 1):
            fname = "Edges-" + str(i) + ".txt"
            if os.stat(fname).st_size != 0:  # File is not empty
                G = pd.read_csv(fname, sep=' ', header=None)
                V = sorted(list(P1Q3_1.GetVertices(G)))
                AdjList = dict.fromkeys(V, [])
                E = P1Q3_1.GetEdges(G)
                for key in AdjList:
                    AdjList[key] = E[E.src == key].dst.tolist()
                with open("AdjList" + str(i) + ".csv", "w") as f:
                    w = csv.writer(f)
                    A = [[key] + value for key, value in AdjList.items()]
                    w.writerows(A)
