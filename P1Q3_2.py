from matplotlib import pyplot as plt


def GraphVandE(nE, nV):  # Line graphs of |E| and |V|
    plt.rcParams['font.family'] = ['Times New Roman', 'serif']
    plt.subplot()  # Creating one subplot
    plt.plot(nV, 'c.-', label='|V[tj-1,tj]|')  # For creating graph of No. Vertices
    plt.plot(nE, 'm.-', label='|E[tj-1,tj]|')  # For creating graph of No. Edges
    plt.title('Time evolution of |V[tj-1,tj]| and |E[tj-1,tj]|', fontsize=12)
    plt.xlabel('Time intervals')
    plt.ylabel('Set cardinality')
    '''N = len(nV)
    plt.xticks(np.arange(0, N, 9), np.arange(1, N+1, 9))  # Setting x ticks positions 0-N & labels 1-N+1'''
    plt.legend(fontsize=9)  # To display plot labels
    plt.savefig('Time_evolution_of_nV_&_nE.png')
    # plt.show()
    plt.close()
