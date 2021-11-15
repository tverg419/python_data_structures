class Vertex:

    def __init__(self, value):
        self.key = value
        self.adjacent = {}
    
    # takes in a vertex and a weight and adds the weight to adjacents dict
    def add_edge(self, v, w):
        self.adjacent[v] = w
   
    def get_key(self):
        return self.key

    def get_edge(self, adj):
        return self.adjacent[adj]

    def __str__(self):
        return f'{self.key} is connected to: {str([[v.key, self.get_edge(v)] for v in self.adjacent])}'

class Graph:

    def __init__(self):
        self.adjList = {}
        self.numVertices = 0
    
    def add_vertex(self, key):
        newVertex = Vertex(key)
        self.numVertices += 1
        self.adjList[key] = newVertex
        return newVertex

    def add_edge(self, start, end, wt):
        if start not in self.adjList:
            startVertex = self.add_vertex(start)
        if end not in self.adjList:
            endVertex = self.add_vertex(end)
        self.adjList[start].add_edge(self.adjList[end], wt)
    
    def get_vertex(self, key):
        if key in self.adjList:
            return self.adjList[key]
        else:
            return None

    def get_all_vertices(self):
        return self.adjList.keys()

    def __iter__(self):
        return iter(self.adjList.values())

    def contains_vertex(self, key):
        return key in self.adjList

if __name__ == "__main__":
    g = Graph()
    
    aList = [[0, 1, 5], [0, 5, 2], [1, 2, 4], [2, 3, 9], [3, 4, 5], [3, 5, 3], [4, 0, 1], [5, 2, 1], [5, 4, 8]]
    for v in aList:
        g.add_edge(v[0], v[1], v[2])

    for n in g.get_all_vertices():
        print(g.get_vertex(n))
