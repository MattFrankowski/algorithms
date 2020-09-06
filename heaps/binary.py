class BinaryHeap():
    def __init__(self, array=None):
        if array is None:
            self._array = []
            self._heapSize = 0
        else:
            self._array = array
            self._heapSize = len(array)
            self.buildHeap()

    def left(self, node):
        return node * 2 + 1

    def right(self, node):
        return node * 2 + 2

    def parent(self, node):
        return node // 2 - 1

    def heapify(self, root):
        left = self.left(root)
        right = self.right(root)
        if left < self._heapSize and self._array[left] > self._array[root]:
            largest = left
        else:
            largest = root
        if right < self._heapSize and self._array[right] > self._array[largest]:
            largest = right
        if largest != root:
            self._array[root], self._array[largest] = self._array[largest], self._array[root]
            self.heapify(largest)

    def buildHeap(self):
        for node in range(self._heapSize // 2 - 1, -1, -1):
            self.heapify(node)

    def insert(self, key):
        self._heapSize += 1
        self._array.append(key)
        node = self._heapSize - 1
        parent = self.parent(node)
        while(node > 0):
            if self._array[node] > self._array[parent]:
                self._array[node], self._array[parent] = self._array[parent], self._array[node]
            node = self.parent(node)
            parent = self.parent(parent)

    def printHeap(self):
        floor = 2
        for i in range(self._heapSize // 2):
            left = self.left(i)
            right = self.right(i)
            print(self._array[i], end='')
            if left < self._heapSize:
                print(f" -> {self._array[left]}", end='')
            if right < self._heapSize:
                print(f", {self._array[right]}", end='')
            print()
            if i == floor - 2:
                floor *= 2
                print()



if __name__ == '__main__':
    pass