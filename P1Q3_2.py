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


'''class PlotHisto:  # Histograms of both |E| and |V|
    def __init__(self, nV, nE):
        self.nV = nV
        self.nE = nE

    def PlotV(self):
        y = self.nV
        N = len(y)
        x = range(N)
        plt.subplot(1, 2, 1)
        plt.title('Vertices Histogram')
        plt.xlabel('Time Intervals Bins')
        plt.ylabel('Number of Vertices')
        plt.bar(x, y, align='edge', color="cyan")

    def PlotE(self):
        y = self.nE
        N = len(y)
        x = range(N)
        plt.subplot(1, 2, 2)
        plt.title('Edges Histogram')
        plt.xlabel('Time Intervals Bins')
        plt.ylabel('Number of Edges')
        plt.bar(x, y, align='edge', color="magenta")

    def HistogramVandE(self):
        self.PlotV()
        self.PlotE()
        plt.savefig('nV_&_nE_Histograms.png')
        plt.tight_layout()
        # plt.show()
        plt.close()'''
