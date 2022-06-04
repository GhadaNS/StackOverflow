import csv


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
