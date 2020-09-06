class AvlNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.quantity = 1
        self.height = 1

    def __repr__(self):
        return str(self.value)


class AvlTree:
    def __init__(self):
        self.root = None

    def insertNode(self, value):
        self.root = self.insert(self.root, value)

    def insert(self, root, value):
        if not root:
            return  AvlNode(value)
        elif value == root.value:
            root.quantity += 1
            return root
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # left left
        if balance > 1 and value < root.left.value: 
            return self.rotateRight(root)
  
        # right right
        if balance < -1 and value > root.right.value: 
            return self.rotateLeft(root) 
  
        # left right 
        if balance > 1 and value > root.left.value: 
            root.left = self.rotateLeft(root.left) 
            return self.rotateRight(root) 
  
        # right left 
        if balance < -1 and value < root.right.value: 
            root.right = self.rotateRight(root.right) 
            return self.rotateLeft(root) 
  
        return root 

    def _search(self, key, root):
        if root.value == key or not root:
            return root
        else:
            if key < root.value:
                if root.left:
                    return self._search(key, root.left)
            else:
                if root.right:
                    return self._search(key, root.right)

    def loadTree(self, data):
        for value in data:
            self.insertNode(value)

    def search(self, key):
        return self._search(key, self.root)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def rotateLeft(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        a.height = 1 + max(self.getHeight(a.left), self.getHeight(a.right))
        return a
    
    def rotateRight(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        a.height = 1 + max(self.getHeight(a.left), self.getHeight(a.right))
        return a


if __name__ == "__main__":
    avl = AvlTree()
    avl.loadTree([1, 2, 3, 4])
    pass