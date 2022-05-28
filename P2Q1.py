import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class VstarEstar:
    def __init__(self, N):
        self.N = int(N)
        self.nVstar: list = [0]
        self.nEstar1: list = [0]
        self.nEstar2: list = [0]

    def VandEstar(self):
        for j in range(1, self.N):
            Vprev = pd.read_csv('vertices-set%s.csv' % j)  # V[tj-1,tj]
            Vnext = pd.read_csv('vertices-set%s.csv' % (j + 1))  # V[tj,tj+1]
            # Vstar = set(Vprev).intersection(set(Vnext))
            Vstar = [i for i in Vprev if i in Vnext]  # V*[tj-1,tj+1]
            self.nVstar.append(len(Vstar))
            with open("Vstar" + str(j) + ".csv", 'w') as f:
                csv.writer(f).writerow(Vstar)

        for j in range(1, self.N):
            Eprev = pd.read_csv('Edges-set%s.csv' % j, header=None)
            Eprev.columns = ["u", "v"]
            Vstar = list(pd.read_csv('Vstar%s.csv' % j))
            Vstar = [int(x) for x in Vstar]
            Estar = [Eprev.iloc[i] for i in range(len(Eprev.index)) if
                     Eprev.u.iloc[i] in Vstar and Eprev.v.iloc[i] in Vstar]
            self.nEstar1.append(len(Estar))
            fname = "Estar[j-1,j]" + str(j) + ".csv"
            with open(fname, 'w') as f:
                for i in range(len(Estar)):
                    csv.writer(f, delimiter=' ').writerow(Estar[i])

        for j in range(1, self.N):
            Eprev = pd.read_csv('Edges-set%s.csv' % (j + 1), header=None)
            Eprev.columns = ["u", "v"]
            Vstar = list(pd.read_csv('Vstar%s.csv' % j))
            Vstar = [int(x) for x in Vstar]
            Estar = [Eprev.iloc[i] for i in range(len(Eprev.index)) if
                     Eprev.u.iloc[i] in Vstar and Eprev.v.iloc[i] in Vstar]
            self.nEstar2.append(len(Estar))
            fname = "Estar[j,j+1]" + str(j) + ".csv"
            with open(fname, 'w') as f:
                for i in range(len(Estar)):
                    csv.writer(f, delimiter=' ').writerow(Estar[i])

        plt.subplot()
        plt.plot(self.nVstar, 'c.-', label='|V*|')
        plt.plot(self.nEstar1, 'm.-', label='|E*[j-1,j]|')
        plt.plot(self.nEstar2, 'y.-', label='|E*[j,j+1]|')
        plt.title('time evolution of the volumes |V*|, |E*[j-1,j]| and |E*[j,j+1]|')
        plt.xlabel('(Tj,Tj+1)')
        plt.xticks(np.arange(1, self.N, 1))
        plt.xlim(1, self.N - 1)
        plt.legend()
        plt.savefig('Time_evolution_of_nVstar_&_nEstar.png', format="PNG")
        plt.show()
        plt.close()
