from matplotlib import pyplot as plt
import numpy as np


def GraphVandE(nE, nV):  # Line graphs of |E| and |V|
    plt.rcParams['font.family'] = ['Times New Roman', 'serif']
    plt.subplot()  # Creating one subplot
    plt.plot(nV, 'c.-', label='|V[tj-1,tj]|')  # For creating graph of No. Vertices
    plt.plot(nE, 'm.-', label='|E[tj-1,tj]|')  # For creating graph of No. Edges
    plt.title('Time evolution of |V| and |E|', fontsize=12)
    plt.xlabel('\" j \"')
    N = len(nV)
    plt.xticks(np.arange(0, N, 1), np.arange(1, N+1, 1))  # Setting x ticks positions 0-N & labels 1-N+1
    plt.legend(fontsize=9)  # To display plot labels
    plt.savefig('Time_evolution_of_nV_&_nE.png', format="PNG")
    plt.show()
    plt.close()


class PlotHisto():  # Histograms of both |E| and |V|
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
        plt.tight_layout()
        plt.show()
        plt.close()

# I thought I may need this
# {M = math.ceil(math.log2(N))
# if M < 5:
#    M = N
# else:
#    M = M * 3
# Tj = ['T'+str(i) for i in range(1, N+1)]
# plt.xticks(list(np.arange(N)), Tj)} I tried to use ticks that shrink when size gets bigger --> disappointment


# Bar chart ------------------------------------------------------------------------------------------------------------

# set width of bar
# barWidth = 0.25
# plt.subplots(figsize=(8, 6))

# Set position of bar on X axis
# br1 = np.arange(len(nV))
# br2 = [x + barWidth for x in br1]

# Make the plot
# plt.bar(br1, nV, color='b', edgecolor='grey', width=barWidth, label='|V|')
# plt.bar(br2, nE, color='r', edgecolor='grey', width=barWidth, label='|E|')

# Adding Xticks
# plt.xlabel('Tj')

# plt.legend()
# plt.show()
