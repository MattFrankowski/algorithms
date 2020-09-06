from math import inf


class Node:
    def __init__(self, id, cost):
        self.id = id
        self.cost = cost
        self.distance = inf
        self.neighbors = []
        self.getNeighbourIds()

    def __repr__(self):
        return str(self.id) + ', ' + str(self.cost)

    def getNeighbourIds(self):
        if self.id > 5:
            self.neighbors.append(self.id - 6)
        if self.id < 30:
            self.neighbors.append(self.id + 6)
        if self.id % 6 != 5:
            self.neighbors.append(self.id + 1)
        if self.id % 6 != 0:
            self.neighbors.append(self.id - 1)

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __le__(self, other):
        return self.distance <= other.distance

    def __ge__(self, other):
        return self.distance >= other.distance

    def __ne__(self, other):
        return self.distance != other.distance


class Graph:
    def __init__(self):
        self.nodes = []

    def loadFromFile(self, path):
        data = ''
        with open(path) as file:
            line = file.readline()
            while line:
                line = line.rstrip('\n')
                data += line
                line = file.readline()
        return data

    def convertData(self, data):
        nodes = []
        for i in range(36):
            node = Node(i, int(data[i]))
            nodes.append(node)
        return nodes

    def loadNodes(self, path):
        data = self.loadFromFile(path)
        self.nodes = self.convertData(data)



if __name__ == '__main__':
    pass