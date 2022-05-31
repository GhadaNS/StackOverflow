import csv


def GetEdges(G):
    E = G.drop_duplicates()
    E = E.reset_index(drop=True)
    return E


def SaveEdges(E, i):
    with open("EdgesSet-" + str(i) + ".csv", "w") as f:
        w = csv.writer(f)
        for j in range(len(E.index)):
            w.writerow(E.iloc[j, :])


def GetVertices(G):
    G.columns = ["src", "dst"]
    V = set()
    V.update(G.src.tolist(), G.dst.tolist())
    return V


def SaveVertices(V, i):
    with open("VerticesSet-" + str(i) + ".csv", 'w') as f:
        csv.writer(f).writerow(V)
