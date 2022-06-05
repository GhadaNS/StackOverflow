import P3Q1
import csv


def TestACC(N, RList):
    ACCListTest = {}
    for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
        ESet = 'Estar[j,j+1]'
        AcObj = P3Q1.AccFunc(N, x, ESet)
        ACC = AcObj.ACC(RList[x])  # Simply calculate ACC with given range
        ACCListTest[x] = ACC
    ACCListTest = {k: v for k, v in sorted(ACCListTest.items(), key=lambda item: item[1], reverse=True)}
    with open("TestACC.csv", "w") as f:  # Save TestACC as csv file
        w = csv.writer(f)
        w.writerow(['Similarity', 'Accuracy'])
        A = [[key, value] for key, value in ACCListTest.items()]
        w.writerows(A)
    return ACCListTest
