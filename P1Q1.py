import csv


def TPartition(net, N):
    t_min = net.tstamp[0]  # instead  of min that takes time we use [0], as we already sorted the df by tstamp
    t_max = net.tstamp[len(net.index)-1]  # Same as min, we just get the last cell
    Dt = t_max - t_min  # The whole time length
    dt = Dt / N  # The interval length
    t = [t_min + i * dt for i in range(N + 1)]  # List of time intervals
    with open("T.csv", 'w') as f:  # Save time intervals in csv file
        csv.writer(f).writerow(t)
    return t_min, t_max, t
