import csv
import os
import networkx as nx


def V_Asterisk(N):
    for i in range(1, N):
        fname1 = "Edges-" + str(i) + ".txt"
        fname2 = "Edges-" + str(i+1) + ".txt"
        if os.stat(fname1).st_size != 0 and os.stat(fname2).st_size != 0:
            G1 = nx.read_edgelist(fname1)
            G2 = nx.read_edgelist(fname2)
            V1 = set(G1.nodes())
            V2 = set(G2.nodes())
            V_Asterisk = set.intersection(V1, V2)
            with open("V_Asterisk" + str(i) + "-" + str(i+1) + ".csv", "w") as f:
                csv.writer(f).writerow(V_Asterisk)
