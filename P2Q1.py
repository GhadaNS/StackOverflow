import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import gc
import os


class VstarEstar:
    def __init__(self, N):
        self.N = int(N)
        self.nVstar: list = []
        self.nEstar1: list = []
        self.nEstar2: list = []

    def VandEstar(self):
        for j in range(1, self.N):
            if os.stat('VerticesSet-%s.csv' % j).st_size == 0 or os.stat('VerticesSet-%s.csv' % (j + 1)).st_size == 0:
                # In case some time intervals have empty Subgraphs
                self.nVstar.append(0)  # The number of both vertices & edges is 0
                self.nEstar1.append(0)
                self.nEstar2.append(0)
                open("Vstar-" + str(j) + ".csv", 'w').close()  # Create empty files
                open("Estar[j-1,j]-" + str(j) + ".csv", 'w').close()
                open("Estar[j,j+1]-" + str(j) + ".csv", 'w').close()
            else:
                # Creation of V*[tj-1,tj+1]
                Vprev = pd.read_csv('VerticesSet-%s.csv' % j)  # V[tj-1,tj]
                Vnext = pd.read_csv('VerticesSet-%s.csv' % (j + 1))  # V[tj,tj+1]
                Vstar = [i for i in Vprev if i in Vnext]  # V*[tj-1,tj+1] = intersect(V[tj-1,tj], V[tj,tj+1])
                del Vprev, Vnext
                gc.collect()
                if len(Vstar) == 0:  # If |V*| there will be no edges
                    self.nVstar.append(0)  # The number of both vertices & edges is 0
                    self.nEstar1.append(0)
                    self.nEstar2.append(0)
                    open("Vstar-" + str(j) + ".csv", 'w').close()  # Create empty files
                    open("Estar[j-1,j]-" + str(j) + ".csv", 'w').close()
                    open("Estar[j,j+1]-" + str(j) + ".csv", 'w').close()
                    continue  # Moves to next iteration
                self.nVstar.append(len(Vstar))  # |V*[tj-1,tj+1]|
                with open("Vstar-" + str(j) + ".csv", 'w') as f:  # Save V* Set in csv file
                    csv.writer(f).writerow(Vstar)

                # Creation of E*[tj-1,tj]
                Eprev = pd.read_csv('EdgesSet-%s.csv' % j, header=None)
                Eprev.columns = ["u", "v"]
                Vstar = [int(x) for x in Vstar]
                # Keep persistent edges whose vertices are part of V*
                Estar = [Eprev.iloc[i] for i in range(len(Eprev.index)) if
                         Eprev.u.iloc[i] in Vstar and Eprev.v.iloc[i] in Vstar]
                del Eprev
                gc.collect()
                self.nEstar1.append(len(Estar))  # |E*[tj-1,tj]|
                with open("Estar[j-1,j]-" + str(j) + ".csv", 'w') as f:  # Save Previous E* Set in csv file
                    for i in range(len(Estar)):
                        csv.writer(f, delimiter=' ').writerow(Estar[i])
                del Estar
                gc.collect()

                # Creation of E*[tj,tj+1]
                Enext = pd.read_csv('EdgesSet-%s.csv' % (j + 1), header=None)
                Enext.columns = ["u", "v"]
                Vstar = [int(x) for x in Vstar]
                Estar = [Enext.iloc[i] for i in range(len(Enext.index)) if
                         Enext.u.iloc[i] in Vstar and Enext.v.iloc[i] in Vstar]
                del Enext, Vstar
                gc.collect()
                self.nEstar2.append(len(Estar))
                with open("Estar[j,j+1]-" + str(j) + ".csv", 'w') as f:
                    for i in range(len(Estar)):
                        csv.writer(f, delimiter=' ').writerow(Estar[i])
                del Estar
                gc.collect()

    def GraphVandEstar(self):
        plt.subplot()  # Creating one subplot
        plt.plot(self.nVstar, 'm.-', label='|V*[tj-1,tj+1]|')
        plt.plot(self.nEstar1, 'c.-', label='|E*[tj-1,tj]|')
        plt.plot(self.nEstar2, 'y.-', label='|E*[tj,tj+1]|')
        plt.legend(fontsize=9)  # To display plot labels
        plt.title('Time evolution of the volumes |V*[tj-1,tj+1]|, |E*[tj-1,tj]| and |E*[tj,tj+1]|', fontsize=12)
        plt.xlabel('Time intervals')
        plt.ylabel('Set cardinality')
        # plt.xticks(np.arange(0, self.N-1, 1), np.arange(1, self.N, 1)) # Setting x ticks positions 0-(N-1) & labels 1-N
        plt.savefig('Time_evolution_of_nVstar_&_nEstar.png', format="PNG")
        plt.show()
        plt.close()
        del self.nVstar, self.nEstar1, self.nEstar2
        gc.collect()
