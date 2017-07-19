import queue
import copy

class Vertex(object):
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.vertexList = set()
        self.vertexCost = dict()

    def hasAdjVertex(self):
        return len(self.vertexList) != 0

    def addAdjVertex(self, v, weight):
        self.vertexList.add(v)
        self.vertexCost[v] = weight

    def getNumOfAdjVertex(self):
        return len(self.vertexList)


class Graph(object):
    def __init__(self, vertexes):
        self.vertex = vertexes
        self.adjList = [Vertex(i) for i in range(vertexes + 1)]
        self.cost = [0] * (vertexes + 1)


    def getVertexNum(self):
        return self.vertex

    def getAdjVertexList(self, u):
        if u >= 0 and u <= self.vertex:
            return self.adjList[u].vertexList

    def printGraph(self):
        for i in range(self.vertex + 1):
            print("%d:" %(i))
            print(self.adjList[i].vertexList)



# UndirectGraph uses the Graph for the base class
class UndirectGraph(Graph):
    def __init__(self, vertexes):
        super().__init__(vertexes)

    def addEdge(self, u, v, weight=0):
        if u <= self.vertex and u >= 0 and v <= self.vertex and v >= 0 and u != v:
            self.adjList[u].addAdjVertex(v, weight)
            self.adjList[v].addAdjVertex(u, weight)
        else:
            print("arguments is illegal!")

    def addVertex(self):
        self.vertex = self.vertex + 1
        self.adjList.append(Vertex(self.vertex))


class DirectGraph(Graph):
    def __init__(self, vertexes):
        super().__init__(vertexes)
        self.indegree = [0] * (self.vertex + 1)

    def addEdge(self, u, v, weight=0):
        if u <= self.vertex and u >= 0 and v <= self.vertex and v >= 0:
            self.adjList[u].addAdjVertex(v, weight)
            self.indegree[v] = self.indegree[v] + 1

    def topsort(self):
        # topNum is the list use to store the sort result
        topNum = [0] * (self.vertex + 1)
        q = queue.Queue()
        counter = 0
        indegreeTemp = copy.deepcopy(self.indegree)

        # Put all the vertex with 0 indegree(no vertex is coming into
        # this vertex) into the queue
        for vertex in range(self.vertex + 1):
            if self.indegree[vertex] == 0:
                q.put(vertex)

        while (not q.empty()):
            v = q.get()
            counter = counter + 1
            topNum[v] = counter

            vertexList = self.getAdjVertexList(v)

            for u in vertexList:
                indegreeTemp[u] = indegreeTemp[u] - 1
                if indegreeTemp[u] == 0:
                    q.put(u)

        # Cycle exists
        if counter != (self.vertex + 1):
            return []

        return topNum

    def breadthFirstSearch(self):
        pass

    def Dijkstra(self):
        pass



if __name__=="__main__":
    test = DirectGraph(6)
    test.addEdge(0, 1)
    test.addEdge(0, 6)
    test.addEdge(0, 5)
    test.addEdge(1, 2)
    test.addEdge(1, 6)
    test.addEdge(2, 6)
    test.addEdge(2, 3)
    test.addEdge(3, 4)
    test.addEdge(5, 4)
    test.addEdge(6, 3)
    test.addEdge(6, 4)
    test.addEdge(6, 5)
    print(test.topsort())
    print([0,1,2,3,4,5,6])
