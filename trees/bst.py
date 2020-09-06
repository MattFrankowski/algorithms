class BstNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.quantity = 1

    def insert(self, value):
        if self.value == value:
            self.quantity += 1
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BstNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BstNode(value)

    def search(self, key, index):
        if self.value == key:
            return index
        else:
            if key < self.value:
                if self.left:
                    index = index * 2
                    self.left.search(key, index)
                else:
                    return False
            else:
                if self.right:
                    index = index * 2 + 1
                    self.right.search(key, index)
                else:
                    return False


class BstTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        for i in range(len(data)):
            if self.root:
                self.root.insert(data[i])
            else:
                self.root = BstNode(data[i])

    def search(self, key):
        if self.root:
            return self.root.search(key, 1)


if __name__ == '__main__':
    pass
