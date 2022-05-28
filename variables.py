import networkx as nx
import itertools as it


G = nx.complete_graph(5)
hi = list(it.combinations([0, 1, 2, 3, 4], 2))
preds = nx.jaccard_coefficient(G, hi)
for u, v, p in preds:
    print(f"({u}, {v}) -> {p:.8f}")
