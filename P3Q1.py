import pandas as pd
import os

for j in range(1, 20):
    if os.stat('Vstar-%s.csv' % j).st_size == 0:  # In case some time intervals have empty Subgraphs
        Vstar = list(pd.read_csv('Vstar-%s.csv' % j))
    else:
        Vstar = []
    # |E0| = |V* x V*| eq(10)
    E0 = len(Vstar) ** 2 # The number of all possible permutations(V*, 2)
    # |^Ex*[tj-1,tj+1]| = |{edge in E0 if Sx(edge) in Rx}|


def ACC(Rx, Sx, j):
    if os.stat('Vstar-%s.csv' % j).st_size == 0:  # In case some time intervals have empty Subgraphs
        Vstar = []
    else:
        Vstar = list(pd.read_csv('Vstar-%s.csv' % j))
    # |E0| = |V* x V*| eq(10)
    E0 = len(Vstar) ** 2 # The number of all possible permutations P(V*, 2)
    # |^Ex*[tj-1,tj+1]| = |{edge in E0 if Sx(edge) in Rx}|
    # |E0| = |V* x V*|
    # E0 =
