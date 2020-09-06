from boyer_moore import BMSearch
from naive_algorithm import naiveSearch
import matplotlib.pyplot as plt
import timeit

def loadFile(path):
    with open(path, encoding='utf8') as file:
        data = file.readlines()
        text = []
        for line in data:
            line = line.rstrip('\n')
            words = line.split(' ')
            for word in words:
                if word != '':
                    text.append(word)
    return text

if __name__ == '__main__':
    text = loadFile("pan-tadeusz.txt")
    patterns = []
    sampleSize = []
    naiveTimes = []
    BMTimes = []
    for i in range(100, 1001, 100):
        patterns = text[:i]
        totalNaiveTime = 0
        for j in range(0, i-1):
            time = timeit.timeit("naiveSearch(patterns[j], text)", "from __main__ import naiveSearch, patterns, text, j", number=1)
            totalNaiveTime += time
        print(f"Naive algorithm\t Size: {i}\tTime: {totalNaiveTime}")
        naiveTimes.append(totalNaiveTime)
        totalBMTime = 0
        for j in range(0, i-1):
            time = timeit.timeit("BMSearch(patterns[j], text)", "from __main__ import BMSearch, patterns, text, j", number=1)
            totalBMTime += time
        print(f"Boyer-Moore algorithm\t Size: {i}\tTime: {totalBMTime}")
        BMTimes.append(totalBMTime)
        sampleSize.append(i)
    
    with open("results.txt", 'w') as file:
        file.write("\t\tNaive search time \nSample size\t\t\t\tTime\n")
        for time, size in zip(naiveTimes, sampleSize):
            line = f"{size} \t\t\t{time}\n"
            file.write(line)
    
        file.write("\t\tBoyer-Moore search time\nSample size\t\t\t\tTime\n")
        for time, size in zip(BMTimes, sampleSize):
            line = f"{size} \t\t\t{time}\n"
            file.write(line)

    plt.figure()
    plt.plot(sampleSize, naiveTimes)
    plt.title("Naive algorithm search time")
    plt.ylabel("Time [s]")
    plt.xlabel("Sample size")

    plt.figure()
    plt.plot(sampleSize, BMTimes)
    plt.title("Boyer_Moore algorithm search time")
    plt.ylabel("Time [s]")
    plt.xlabel("Sample size")

    plt.show()

            