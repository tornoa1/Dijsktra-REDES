from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def agregarNodo(self, value):
        self.nodes.add(value)

    def agregarBorde(self, fromNode, toNode, distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

#Algoritmo Dijkstra
def dijkstra(graph, inicial):
    visited = {inicial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited, path

customGraph = Graph()
customGraph.agregarNodo("0")
customGraph.agregarNodo("1")
customGraph.agregarNodo("2")
customGraph.agregarNodo("3")
customGraph.agregarNodo("4")
customGraph.agregarNodo("5")
customGraph.agregarNodo("6")
customGraph.agregarNodo("7")
customGraph.agregarNodo("8")
customGraph.agregarNodo("9")

customGraph.agregarBorde("0", "1", 4)
customGraph.agregarBorde("0", "2", 6)
customGraph.agregarBorde("0", "3", 3)
customGraph.agregarBorde("1", "2", 5)
customGraph.agregarBorde("1", "4", 3)
customGraph.agregarBorde("2", "4", 1)
customGraph.agregarBorde("2", "5", 1)
customGraph.agregarBorde("2", "6", 3)
customGraph.agregarBorde("3", "2", 2)
customGraph.agregarBorde("3", "6", 6)
customGraph.agregarBorde("4", "5", 2)
customGraph.agregarBorde("4", "7", 4)
customGraph.agregarBorde("5", "7", 2)
customGraph.agregarBorde("5", "8", 1)
customGraph.agregarBorde("5", "9", 8)
customGraph.agregarBorde("6", "5", 3)
customGraph.agregarBorde("6", "8", 5)
customGraph.agregarBorde("7", "9", 7)
customGraph.agregarBorde("8", "9", 4)


print(dijkstra(customGraph, "0"))