from math import ceil

class TernaryHeap():
    def __init__(self, array=None):
        if array is None:
            self._array = []
            self._heapSize = 0
        else:
            self._array = array
            self._heapSize = len(array)
            self.buildHeap()

    def left(self, node):
        return node * 3 + 1

    def middle(self, node):
        return node * 3 + 2

    def right(self, node):
        return node * 3 + 3

    def parent(self, node):
        return node // 3 - 1

    def heapify(self, root):
        left = self.left(root)
        middle = self.middle(root)
        right = self.right(root)
        if left < self._heapSize and self._array[left] > self._array[root]:
            largest = left
        else:
            largest = root
        if middle < self._heapSize and self._array[middle] > self._array[largest]:
            largest = middle
        if right < self._heapSize and self._array[right] > self._array[largest]:
            largest = right
        if largest != root:
            self._array[root], self._array[largest] = self._array[largest], self._array[root]
            self.heapify(largest)

    def buildHeap(self):
        for node in range(self._heapSize // 3 - 1, -1, -1):
            self.heapify(node)

    def insert(self, key):
        self._heapSize += 1
        self._array.append(key)
        node = self._heapSize - 1
        parent = self.parent(node)
        while(parent >= 0):
            if self._array[node] > self._array[parent]:
                self._array[node], self._array[parent] = self._array[parent], self._array[node]
                node = parent
                parent = self.parent(parent)
            else:
                break
    
    def printHeap(self):
        floor = 0
        width = 3
        for i in range(ceil(self._heapSize / 3)):
            children = [self.left(i), self.middle(i), self.right(i)]
            print(self._array[i], end='')
            if children[0] < self._heapSize:
                print(f" -> {self._array[children[0]]}", end='')
            for child in children[1:]:
                if child < self._heapSize:
                    print(f", {self._array[child]}", end='')
            print()
            if i == floor:
                floor += width
                width *= 3
                print()

if __name__ == '__main__':
    pass