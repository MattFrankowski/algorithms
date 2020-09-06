import numpy as np
import timeit
import matplotlib.pyplot as plt
from bst import BstTree, BstNode
from avl import AvlNode, AvlTree


if __name__ == '__main__':
    searchTimesB = []
    insertionTimesB = []
    insertionSampleSize = []
    searchSampleSize = []
    searchTimesA = []
    insertionTimesA = []
    arr = []
    for i in range(1000, 10001, 1000):
        bst = BstTree()
        avl = AvlTree()
        arr.extend(np.random.randint(low=1, high=3000, size=1000))
        time = timeit.timeit("bst.insert(arr)", setup="from __main__ import bst, arr", number=1)
        insertionTimesB.append(float(time))
        time = timeit.timeit("avl.loadTree(arr)", setup="from __main__ import avl, arr", number=1)
        insertionTimesA.append(float(time))
        insertionSampleSize.append(i)

    snippetB = """for j in range(i):
            bst.search(searchArr[j])"""
    snippetA = """for j in range(i):
            avl.search(searchArr[j])"""
    arr = np.random.randint(low=1, high=3000, size=10000)
    bst = BstTree()
    bst.insert(arr)
    avl = AvlTree()
    avl.loadTree(arr)
    for i in range(100, 1001, 100):
        searchArr = arr[:i]
        time = timeit.timeit(snippetB, setup="from __main__ import i, bst, searchArr", number=1)
        searchTimesB.append(float(time))
        time = timeit.timeit(snippetA, setup="from __main__ import i, avl, searchArr", number=1)
        searchTimesA.append(float(time))
        searchSampleSize.append(i)

    with open("results.txt", 'w') as file:
        file.write('BST insertion\nSample size  Time\n')
        for time, size in zip(insertionTimesB, insertionSampleSize):
                line = f"{size} {time}\n"
                file.write(line)
        file.write('\nAVL insertion\nSample size  Time\n')
        for time, size in zip(insertionTimesA, insertionSampleSize):
                line = f"{size} {time}\n"
                file.write(line)
        file.write('\nBST search\nSample size  Time\n')
        for time, size in zip(searchTimesB, searchSampleSize):
                line = f"{size} {time}\n"
                file.write(line)
        file.write('\nAVL search\nSample size  Time\n')
        for time, size in zip(searchTimesA, searchSampleSize):
                line = f"{size} {time}\n"
                file.write(line)

plt.figure()
plt.plot(insertionSampleSize, insertionTimesB)
plt.plot(insertionSampleSize, insertionTimesA)
plt.legend(['BST', 'AVL'], loc='upper left')
plt.title("insertion time chart")
plt.ylabel("Time [s]")
plt.xlabel("Sample size")

plt.figure()
plt.plot(searchSampleSize, searchTimesB)
plt.plot(searchSampleSize, searchTimesA)
plt.legend(['BST', 'AVL'], loc='upper left')
plt.title("BST search time chart")
plt.ylabel("Time [s]")
plt.xlabel("Sample size")
plt.show()
    

