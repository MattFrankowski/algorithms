import timeit
import sys
import matplotlib.pyplot as plt
sys.setrecursionlimit(10**6)


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j+1], array[j]


def quicksort(array):
    qsort(array, 0, len(array) - 1)
    return array


def qsort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        qsort(array, left, mid - 1)
        qsort(array, mid + 1, right)


def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[right] = array[right], array[i+1]
    return i + 1
