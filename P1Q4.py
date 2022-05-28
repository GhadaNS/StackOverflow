from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
import csv


def Cent(G, i):

    fig, axs = plt.subplots(2, 3)  # Create 6 subplots
    fig.delaxes(axs[1, 2])  # Delete the last subplot as we only need 5 for the 5 centrality measures
    fig.suptitle('Centrality Measures G' + str(i))

    # Degree Centrality
    dc = nx.degree_centrality(G)
    dc = dict(sorted(dc.items(), key=lambda item: item[1]))  # Sort by value
    # C = Counter(dc.values())  # counting occurrences of dc values
    # xlabel = list(C.keys())
    # valsum = sum(C.values())
    # y = [v / valsum for v in C.values()]
    x = list(dc.values())
    axs[0, 0].hist(x, edgecolor='black', weights=np.ones_like(x) / len(x))
    # n, bins, patches = plt.hist(x, len(C), density=True, facecolor='g', alpha=0.75)
    # plt.grid(axis='y', alpha=0.75)
    # plt.bar(x, y, color='g')
    # plt.xticks(list(np.arange(1, len(xlabel)+1)), xlabel, rotation=50)
    # plt.savefig('Degree_centrality_G' + str(i) + '.png', format="PNG")
    axs[0, 0].set_title('Degree centrality', fontsize=10)
    axs[0, 0].set_ylabel('Relative Frequency', fontsize=8)
    # plt.xlabel('Degree centrality')
    # plt.ylabel('Frequency')
    # plt.show()
    w = csv.writer(open("Degree_centrality_G" + str(i) + ".csv", "w"))
    for key, val in dc.items():
        w.writerow([key, val])

    # Closeness Centrality
    cc = nx.closeness_centrality(G)
    cc = dict(sorted(cc.items(), key=lambda item: item[1]))  # Sort by value
    x = list(cc.values())
    # fig = plt.figure()
    # ax = fig.add_subplot()
    axs[0, 1].hist(x, edgecolor='black', weights=np.ones_like(x) / len(x))
    # plt.savefig('Closeness_centrality_' + str(i) + '.png', format="PNG")
    axs[0, 1].set_title('Closeness centrality', fontsize=10)
    # plt.xlabel('Closeness centrality')
    # plt.ylabel('Frequency')
    # plt.show()
    w = csv.writer(open("Closeness_centrality_G" + str(i) + ".csv", "w"))
    for key, val in cc.items():
        w.writerow([key, val])

    # Betweenness Centrality
    bc = nx.betweenness_centrality(G)
    bc = dict(sorted(bc.items(), key=lambda item: item[1]))  # Sort by value
    x = list(bc.values())
    axs[0, 2].hist(x, edgecolor='black', weights=np.ones_like(x) / len(x))
    axs[0, 2].set_title('Betweenness centrality', fontsize=10)
    w = csv.writer(open("Betweenness_centrality_G" + str(i) + ".csv", "w"))
    for key, val in bc.items():
        w.writerow([key, val])

    # Eigenvector Centrality
    ec = nx.eigenvector_centrality(G, 1000)
    ec = dict(sorted(ec.items(), key=lambda item: item[1]))  # Sort by value
    x = list(ec.values())
    axs[1, 0].hist(x, edgecolor='black', weights=np.ones_like(x) / len(x))
    axs[1, 0].set_title('Eigenvector centrality', fontsize=10)
    axs[1, 0].set_ylabel('Relative Frequency', fontsize=8)
    w = csv.writer(open("Eigenvector_centrality_G" + str(i) + ".csv", "w"))
    for key, val in ec.items():
        w.writerow([key, val])

    # Katz Centrality
    kc = nx.katz_centrality(G)
    kc = dict(sorted(kc.items(), key=lambda item: item[1]))  # Sort by value
    x = list(kc.values())
    axs[1, 1].hist(x, edgecolor='black', weights=np.ones_like(x) / len(x))
    axs[1, 1].set_title('Katz centrality', fontsize=10)
    w = csv.writer(open("katz_centrality_graph_" + str(i) + ".csv", "w"))
    for key, val in kc.items():
        w.writerow([key, val])

    plt.tight_layout()
    plt.savefig('Centrality_Measures_G' + str(i) + '.png', format="PNG")
    plt.show()
    plt.close()
