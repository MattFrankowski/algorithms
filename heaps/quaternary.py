from math import ceil

class QuaternaryHeap():
    def __init__(self, array=None):
        if array is None:
            self._array = []
            self._heapSize = 0
        else:
            self._array = array
            self._heapSize = len(array)
            self.buildHeap()

    def first(self, node):
        return node * 4 + 1

    def second(self, node):
        return node * 4 + 2

    def third(self, node):
        return node * 4 + 3

    def fourth(self, node):
        return node * 4 + 4

    def parent(self, node):
        return node // 4 - 1

    def heapify(self, root):
        first = self.first(root)
        second = self.second(root)
        third = self.third(root)
        fourth = self.fourth(root)
        if first < self._heapSize and self._array[first] > self._array[root]:
            largest = first
        else:
            largest = root
        if second < self._heapSize and self._array[second] > self._array[largest]:
            largest = second
        if third < self._heapSize and self._array[third] > self._array[largest]:
            largest = third
        if fourth < self._heapSize and self._array[fourth] > self._array[largest]:
            largest = fourth
        if largest != root:
            self._array[root], self._array[largest] = self._array[largest], self._array[root]
            self.heapify(largest)

    def buildHeap(self):
        for node in range(self._heapSize // 4 - 1, -1, -1):
            self.heapify(node)

    def insert(self, key):
        self._heapSize += 1
        self._array.append(key)
        node = self._heapSize - 1
        parent = self.parent(node)
        while(node > 0):
            if self._array[node] > self._array[parent]:
                self._array[node], self._array[parent] = self._array[parent], self._array[node]
                node = parent
                parent = self.parent(parent)
            else:
                break

    def printHeap(self):
        floor = 0
        width = 4
        for i in range(ceil(self._heapSize / 4)):
            children = [self.first(i), self.second(i), self.third(i), self.fourth(i)]
            print(self._array[i], end='')
            if children[0] < self._heapSize:
                print(f" -> {self._array[children[0]]}", end='')
            for child in children[1:]:
                if child < self._heapSize:
                    print(f", {self._array[child]}", end='')
            print()
            if i == floor:
                floor += width
                width *= 4
                print()

if __name__ == '__main__':
    pass