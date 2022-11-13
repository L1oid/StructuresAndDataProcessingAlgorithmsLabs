class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def reverse_graph(graph: Graph):
    r_graph = Graph()
    for vert in graph:
        for neighbor in vert.getConnections():
            r_graph.addEdge(neighbor.getId(), vert.getId())
    return r_graph


graph = Graph()
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(2, 1)
graph.addEdge(1, 3)

print("Given graph:")
for vert in graph:
    for neighbor in vert.getConnections():
        print(vert.getId(), neighbor.getId())

r_graph = reverse_graph(graph)

print("Inverted graph:")
for vert in r_graph:
    for neighbor in vert.getConnections():
        print(vert.getId(), neighbor.getId())
