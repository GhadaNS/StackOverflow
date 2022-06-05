import P3Q1
import csv


def TrainACC(N):
    RList = {}
    ACCListTrain = {}
    for x in ['Sgd', 'Scn', 'Sjc', 'Sa', 'Spa']:
        ESet = 'Estar[j-1,j]'
        AcObj = P3Q1.AccFunc(N, x, ESet)
        R = AcObj.PrvSimVal()
        Rl, Rr = IdL, IdR = 0, len(R) - 1  # Min and Max values indices of R
        # IdLeft/Right are used for iterating through all the possible R (Range) list intervals
        # Rleft/right are used to keep indices of interval for best ACC
        ACC_best = AcObj.ACC((R[IdL], R[IdR]))  # We start assuming the whole range gives the best ACC
        # then we reduce that range if we get a better ACC, till we reach an interval with the best ACC
        ACC_best1 = ACC_best
        while IdL < IdR - 1:
            ACC = AcObj.ACC((R[IdL + 1], R[IdR]))  # Calculate ACC with reduced range one step from left
            if ACC > ACC_best:  # If calculated better than previous best ACC
                ACC_best = ACC  # Update best ACC
                Rl = IdL + 1  # Reduce "best" range one step from left
            ACC = AcObj.ACC((R[IdL], R[IdR - 1]))  # Calculate ACC with reduced range one step from right
            if ACC > ACC_best:  # If calculated better than previous best ACC
                ACC_best = ACC  # Update best ACC
                Rr = IdR - 1  # Reduce "best" range one step from right
            ACC_best2 = ACC_best  # present best ACC
            if ACC_best1 == ACC_best2:  # If previous best ACC == present best ACC
                break  # To stop the while loop once the maximum accuracy isn't changing anymore
            else:
                ACC_best1 = ACC_best2
            IdL += 1  # Reduce range one step from left
            IdR -= 1  # Reduce range one step from right
        # y = 'R' + x  # Rx* name for each Similarity Measurement
        # exec("y = (R[RLeft], R[RRight])")  # Applying the value to the name
        RList[x] = (R[Rl], R[Rr])
        ACCListTrain[x] = ACC_best
    ACCListTrain = {k: v for k, v in sorted(ACCListTrain.items(), key=lambda item: item[1], reverse=True)}
    with open("Rx.csv", "w") as f, open("TrainACC.csv", "w") as t:  # Save Rx* and TrainACC as csv file
        w1 = csv.writer(f)
        w2 = csv.writer(t)
        w1.writerow(['Similarity', 'RMin', 'RMax'])
        w2.writerow(['Similarity', 'Accuracy'])
        A = [[key] + [value[0], value[1]] for key, value in RList.items()]
        B = [[key, value] for key, value in ACCListTrain.items()]
        w1.writerows(A)
        w2.writerows(B)
    return ACCListTrain, RList
