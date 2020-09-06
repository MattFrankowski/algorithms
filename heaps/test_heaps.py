import matplotlib.pyplot as plt
import random
from binary import BinaryHeap
from ternary import TernaryHeap
from quaternary import QuaternaryHeap
import numpy as np
import timeit

if __name__ == '__main__':
    binaryTimes = []
    ternaryTimes = []
    quaternaryTimes = []

    sampleSize = []

    arr = np.random.randint(low=1, high=3000, size=100000)
    for i in range(10000, 100001, 10000):
        array = arr[:i]
        averageTime = 0
        for j in range(10):
            time = timeit.timeit("binaryHeap = BinaryHeap(array)", setup="from __main__ import BinaryHeap, array", number=1)
            averageTime += time
        averageTime /= 10
        binaryTimes.append(float(averageTime))
        sampleSize.append(i)
        averageTime = 0
        for j in range(10):
            time = timeit.timeit("ternaryHeap = TernaryHeap(array)", setup="from __main__ import TernaryHeap, array", number=1)
            averageTime += time
        averageTime /= 10      
        ternaryTimes.append(float(averageTime))
        averageTime = 0
        for j in range(10):
            time = timeit.timeit("quaternaryHeap = QuaternaryHeap(array)", setup="from __main__ import QuaternaryHeap, array", number=1)
            averageTime += time
        averageTime /= 10       
        quaternaryTimes.append(float(averageTime))

    with open("results.txt", 'w') as file:
        file.write("\t\tBinary heap creation\nSample size\t\t\t\tTime\n")
        for time, size in zip(binaryTimes, sampleSize):
            line = f"{size}\t\t\t{time}\n"
            file.write(line)
    
        file.write("\t\tTernary heap creation\nSample size\t\t\t\tTime\n")
        for time, size in zip(ternaryTimes, sampleSize):
            line = f"{size}\t\t\t{time}\n"
            file.write(line)

        file.write("\t\tQuaternary heap creation\nSample size\t\t\t\tTime\n")
        for time, size in zip(quaternaryTimes, sampleSize):
            line = f"{size}\t\t\t{time}\n"
            file.write(line)


    plt.figure()
    plt.plot(sampleSize, binaryTimes)
    plt.title("Creating binary heap chart")
    plt.ylabel("Time [s]")
    plt.xlabel("Sample size")
    
    plt.figure()
    plt.plot(sampleSize, ternaryTimes)
    plt.title("Creating ternary heap chart")
    plt.ylabel("Time [s]")
    plt.xlabel("Sample size")

    plt.figure()
    plt.plot(sampleSize, quaternaryTimes)
    plt.title("Creating quaternary heap chart")
    plt.ylabel("Time [s]")
    plt.xlabel("Sample size")

    plt.figure()
    plt.plot(sampleSize, binaryTimes)
    plt.plot(sampleSize, ternaryTimes)
    plt.plot(sampleSize, quaternaryTimes)
    plt.legend(["Binary", "Ternary", "Quaternary"], loc="upper left")
    plt.title("Creating  heap time comparison")
    plt.ylabel("Time [s]")
    plt.xlabel("Sample size")
    plt.show()
