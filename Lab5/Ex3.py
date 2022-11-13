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


graph = Graph()
graph.addEdge("3/4 cup milk", "1 cup mix")
graph.addEdge("1 egg", "1 cup mix")
graph.addEdge("1 oil", "1 cup mix")
graph.addEdge("1 cup mix", "pour 1/4 cup")
graph.addEdge("1 cup mix", "heat syrup")
graph.addEdge("heat griddle", "pour 1/4 cup")
graph.addEdge("pour 1/4 cup", "turn when bubbly")
graph.addEdge("turn when bubbly", "eat")
graph.addEdge("heat syrup", "eat")


def dfs(graph: Graph):
    visited = {}
    unvisited_nodes = list(graph.getVertices())
    for node in unvisited_nodes:
        visited[node] = False
    stack = []

    for node in unvisited_nodes:
        if visited[node] == False:
            dfsUtil(node, visited, stack)
    print(stack)


def dfsUtil(node, visited, stack):
    visited[node] = True

    neighbors = []
    for neighbor in graph.getVertex(node).getConnections():
        neighbors.append(neighbor.getId())

    for neighbor in neighbors:
        if visited[neighbor] == False:
            dfsUtil(neighbor, visited, stack)
    stack.insert(0, node)


dfs(graph)
