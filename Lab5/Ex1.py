from collections import deque

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


def person_is_seller(name):
    return name.getId()[0] == 'a'


graph = Graph()
graph.addEdge("you", "alice")
graph.addEdge("you", "bob")
graph.addEdge("you", "claire")
graph.addEdge("bob", "anuj")
graph.addEdge("bob", "peggy")
graph.addEdge("claire", "thom")
graph.addEdge("claire", "jonny")


def search(name):
    search_queue = deque()
    search_queue += graph.getVertex(name).getConnections()
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person.getId() + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


search("you")