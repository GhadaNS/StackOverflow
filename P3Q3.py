import P3Q1


def TestACC(N, RList):
    ACCListTest = {}
    for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
        ESet = 'Estar[j,j+1]'
        AcObj = P3Q1.AccFunc(N, x, ESet)
        ACC = AcObj.ACC(RList[x])  # Simply calculate ACC with given range
        ACCListTest[x] = ACC
    return ACCListTest
