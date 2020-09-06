def selection_sort(array):
    sample_length = len(array)
    for i in range(sample_length - 1):
        min = i
        for j in range(i+1, sample_length):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
