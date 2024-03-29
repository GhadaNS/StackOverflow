import networkx as nx
import numpy as np
import pandas as pd
import os
import gc
import sys


class AccFunc:
    def __init__(self, N, x, ESet):
        self.N = N
        self.x = x
        self.AccList = None
        self.ESet = ESet
        self.Eps = sys.float_info.epsilon

    def PrvSimVal(self):  # Estar[j-1,j] Similarity values for training purposes
        R = set()
        for i in range(1, self.N):
            if os.stat('Estar[j-1,j]-%s.csv' % i).st_size != 0:  # In case some time intervals have empty Subgraphs
                Sx = pd.read_csv(self.x + '_Estar[j-1,j]-%s.csv' % i, index_col=0)
                R.update(np.unique(Sx.to_numpy()).tolist())  # Getting all the possible similarity values of Si
        R = sorted(list(R))  # Sorting all possible Similarity values of all time intervals
        del Sx
        gc.collect()
        return R

    def ACC(self, Rx):
        Acc = []
        for i in range(1, self.N):
            G = nx.read_edgelist(self.ESet + '-%s.csv' % i)
            if not nx.is_empty(G):
                Vstar = list(pd.read_csv('Vstar-%s.csv' % i))
                Sx = pd.read_csv(self.x + '_Estar[j-1,j]-%s.csv' % i, index_col=0)
                Sx.index = Sx.index.map(str)  # Since indices are read as ints we convert them back to str for 'loc' use
                E = G.edges()
                # |E0| = |V* x V*| eq(10)
                lE0 = len(Vstar) ** 2  # The number of all possible permutations P(V*, 2)
                # |^Ex*[tj-1,tj+1]| = |{edge in E0 if Sx(edge) in Rx}| eq(13)
                '''Ex = set()
                for u in Vstar:
                    for v in Vstar:
                        if u < v and Rx[0] < Sx.loc[u, v] < Rx[-1]:
                            Ex.add((u, v))'''  # These lines are resumed in the next line list comprehension
                Ex = [(u, v) for u in Vstar for v in Vstar if u < v and Rx[0] <= Sx.loc[u, v] <= Rx[-1]]
                EXEx = [e for e in E if e in Ex]  # Intersection(E, Ex) for the calculation of TPR & TNR
                # Some lengths for the calculation of TPR & TNR - calculate them once for all
                lE, lEXEx = len(E), len(EXEx)
                # TPR(Rx, E) eq(15)
                TPR = lEXEx / lE
                # TNR(Rx, E) eq(16)
                TNR = 1 - ((len(Ex) - lEXEx) + self.Eps) / ((lE0 - lE) + self.Eps)
                # Lambda eq(17)
                L = lE / lE0
                # ACC Calculation
                Acc.append(L * TPR + (1 - L) * TNR)
                del G, E, Ex, EXEx, Vstar, Sx
                gc.collect()
        self.AccList = Acc
        return np.mean(Acc)
