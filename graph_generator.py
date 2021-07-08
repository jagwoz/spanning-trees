from graph import *

class graph_generator:
    def __init__(self):
        self.adjacency = []

    def next_graph(self, graph_type, n, m):
        if graph_type == "full":
            self.adjacency = [[1 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        self.adjacency[i][j] = 0
            return graph(adjacency=self.adjacency)

        elif graph_type == "grid":
            v = (m + 1) * (n + 1)
            self.adjacency = [[0 for _ in range(v)] for _ in range(v)]
            for i in range(m + 1):
                for j in range(n + 1):
                    actual = i * (n + 1) + j
                    if actual < v - 1 and j < n:
                        self.adjacency[actual][actual + 1] = 1
                        self.adjacency[actual + 1][actual] = 1
                    if i < m:
                        self.adjacency[actual][actual + n + 1] = 1
                        self.adjacency[actual + n + 1][actual] = 1
            return graph(adjacency=self.adjacency)
