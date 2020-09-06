from bubblesort import bubble_sort
from quicksort import quicksort
from selectionsort import selection_sort
import matplotlib.pyplot as plt
import timeit

file = open("wyniki.txt", "w+") 


def load_file(path):
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


def print_time(time, array_size, sort_type):
    statement = f"Array size: {array_size}, time: {time}"
    file.write(f"{statement}\n")
    print(statement)


if __name__ == '__main__':
    text = load_file('pan-tadeusz.txt')
    sort_names = {'bubble_sort' : 'Bubble sort', 'selection_sort' : 'Selection sort', 'quicksort' : 'Quicksort'}
    for sort in sort_names.keys():
        times = []
        array_sizes = []
        print(sort_names[sort])
        file.write(f"{sort_names[sort]}\n")
        for i in range(1000, 10001, 1000):
            array = text[:i]
            time = timeit.timeit(f"{sort}(array)", setup=f"from __main__ import {sort}, array", number=1)
            times.append(float(time))
            array_sizes.append(i)
            print_time(float(time), i, {sort})
        plt.figure()
        plt.plot(array_sizes, times)
        plt.title(sort_names[sort])
        plt.xlabel('Array size')
        plt.ylabel('Time (seconds)')
        print()
    plt.show()
    file.close()

