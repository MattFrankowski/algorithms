from graph import Graph, Node
from math import inf


class Dijkstra:
    def __init__(self):
        self.graph = Graph()
        self.coveredGraph = []
        self.graph_start = 0

    def loadGraph(self, path):
        self.graph.loadNodes(path)

    def findStartingNode(self):
        for i in range(len(self.graph.nodes)):
            if(self.graph.nodes[i].cost == 0):
                self.graph_start = i
                break

    def minDistance(self, index):
        min = inf
        for node in self.graph.nodes:
            if node.distance < min and node.id not in self.coveredGraph:
                min = node.distance
                minIndex = node.id
        return minIndex

    def dijkstra(self):
        u = self.graph_start
        self.graph.nodes[u].distance = 0
        self.coveredGraph.append(u)
        for i in self.graph.nodes:
            for v in self.graph.nodes[u].neighbors:
                alt = self.graph.nodes[u].distance + self.graph.nodes[v].cost
                if alt < self.graph.nodes[v].distance:
                    self.graph.nodes[v].distance = alt
                    self.graph.nodes[v].last_node = u
            u = self.minDistance(u)
            self.coveredGraph.append(u)
            if self.graph.nodes[u].cost == 0:
                self.print_path(u)
                break

    def print_path(self, finish):
        current = finish
        path = set()
        while current != self.graph_start:
            path.add(current)
            current = self.graph.nodes[current].last_node
        path.add(current)
        for i in range(36):
            if i in path:
                print(self.graph.nodes[i].cost, end="")
            else:
                print(' ', end='')
            if i % 6 == 5:
                print()



if __name__ == '__main__':

    for i in range(3):
        print(f"Data sample {i + 1}")
        dijkstra = Dijkstra()
        dijkstra.loadGraph(f"data_example{i+1}.txt")
        dijkstra.findStartingNode()
        dijkstra.dijkstra()


