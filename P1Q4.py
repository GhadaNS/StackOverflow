from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
import csv
import gc


def Cent(G, i):

    fig, axs = plt.subplots(2, 3)  # Create 6 subplots
    fig.delaxes(axs[1, 2])  # Delete the last subplot as we only need 5 for the 5 centrality measures
    fig.suptitle('Centrality Measures G' + str(i))

    # Degree Centrality
    dc = nx.degree_centrality(G)
    dc = dict(sorted(dc.items(), key=lambda item: item[1]))  # Sort by value
    '''C = Counter(dc.values())  # counting occurrences of dc values
    xlabel = list(C.keys())
    valsum = sum(C.values())
    y = [v / valsum for v in C.values()]'''
    x = list(dc.values())
    axs[0, 0].hist(x, color="#1c2e4a", edgecolor='black', weights=np.ones_like(x) / len(x))
    # First subplot in [0,0] is filled with relative frequency of degree centrality values
    # All values are weighted with 1/len(x) to get the relative frequency i.e. each x[i] is plotted x[i]/len(x)
    '''n, bins, patches = plt.hist(x, len(C), density=True, facecolor='g', alpha=0.75)
    plt.grid(axis='y', alpha=0.75)
    plt.bar(x, y, color='g')
    plt.xticks(list(np.arange(1, len(xlabel)+1)), xlabel, rotation=50)
    plt.savefig('Degree_centrality_G' + str(i) + '.png', format="PNG")'''
    axs[0, 0].set_title('Degree centrality', fontsize=10)
    axs[0, 0].set_ylabel('Relative Frequency', fontsize=8)
    '''plt.xlabel('Degree centrality')
    plt.ylabel('Frequency')
    plt.show()'''
    '''w = csv.writer(open("Degree_centrality_G" + str(i) + ".csv", "w"))
    for key, val in dc.items():  # Saving centrality values in csv file
        w.writerow([key, val])'''
    del dc  # We delete pointer to dc values for space optimization
    gc.collect()  # For the actual deletion of the values
    # Same goes for the rest of the centrality measures

    # Closeness Centrality
    cc = nx.closeness_centrality(G)
    cc = dict(sorted(cc.items(), key=lambda item: item[1]))  # Sort by value
    x = list(cc.values())
    '''fig = plt.figure()
    ax = fig.add_subplot()'''
    axs[0, 1].hist(x, color="#8b008b", edgecolor='black', weights=np.ones_like(x) / len(x))
    # plt.savefig('Closeness_centrality_' + str(i) + '.png', format="PNG")
    axs[0, 1].set_title('Closeness centrality', fontsize=10)
    '''plt.xlabel('Closeness centrality')
    plt.ylabel('Frequency')
    plt.show()'''
    '''w = csv.writer(open("Closeness_centrality_G" + str(i) + ".csv", "w"))
    for key, val in cc.items():
        w.writerow([key, val])'''
    del cc
    gc.collect()

    # Betweenness Centrality
    bc = nx.betweenness_centrality(G)
    bc = dict(sorted(bc.items(), key=lambda item: item[1]))  # Sort by value
    x = list(bc.values())
    axs[0, 2].hist(x, color="#8B8000", edgecolor='black', weights=np.ones_like(x) / len(x))
    axs[0, 2].set_title('Betweenness centrality', fontsize=10)
    '''w = csv.writer(open("Betweenness_centrality_G" + str(i) + ".csv", "w"))
    for key, val in bc.items():
        w.writerow([key, val])'''
    del bc
    gc.collect()

    # Eigenvector Centrality
    ec = nx.eigenvector_centrality(G, 1000)
    ec = dict(sorted(ec.items(), key=lambda item: item[1]))  # Sort by value
    x = list(ec.values())
    axs[1, 0].hist(x, color="#d2691e", edgecolor='black', weights=np.ones_like(x) / len(x))
    axs[1, 0].set_title('Eigenvector centrality', fontsize=10)
    axs[1, 0].set_ylabel('Relative Frequency', fontsize=8)
    '''w = csv.writer(open("Eigenvector_centrality_G" + str(i) + ".csv", "w"))
    for key, val in ec.items():
        w.writerow([key, val])'''
    del ec
    gc.collect()

    # Katz Centrality
    kc = nx.katz_centrality_numpy(G)
    kc = dict(sorted(kc.items(), key=lambda item: item[1]))  # Sort by value
    x = list(kc.values())
    axs[1, 1].hist(x, color="#006400", edgecolor='black', weights=np.ones_like(x) / len(x))
    axs[1, 1].set_title('Katz centrality', fontsize=10)
    '''w = csv.writer(open("Katz_centrality_G" + str(i) + ".csv", "w"))
    for key, val in kc.items():
        w.writerow([key, val])'''
    del kc
    gc.collect()

    plt.tight_layout()
    plt.savefig('Centrality_Measures_G' + str(i) + '.png')  # Saving plot as png file
    # plt.show()  # Displaying plot
    plt.close()  # Closing plot
