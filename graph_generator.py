import copy

from graph import *


class graph_generator:
    def __init__(self):
        self.adjacency = []
        self.percent = 1

    def next_graph(self, graph_type, n, m, percent=1):
        def is_consistent(new_adjacency):
            new_n = len(new_adjacency)
            checked = [1] + [0] * (new_n - 1)
            checked_s = [0] * new_n
            iteration = 0
            while sum(checked_s) < new_n and iteration < new_n:
                iteration += 1
                neighbors = []
                for k in range(len(checked)):
                    if checked[k] == 1:
                        checked_s[k] = 1
                        for l in range(len(new_adjacency[k])):
                            if new_adjacency[k][l] == 1:
                                neighbors.append(l)
                                checked[l] = 1
                        if sum(checked_s) == new_n:
                            return True
            return False
        self.percent = percent

        if graph_type == "complete":
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

        elif graph_type == "percent":
            self.adjacency = [[1 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        self.adjacency[i][j] = 0
            edges = []
            for i in range(n):
                for j in range(n):
                    if not [i, j] in edges and not [j, i] in edges and self.adjacency[i][j] == 1:
                        edges.append([i, j])
            all_edges = len(edges)
            edges_max = all_edges
            while len(edges) > self.percent * edges_max:
                adjacency_temp = copy.deepcopy(self.adjacency)
                random_edge = int(np.random.uniform(0, len(edges)))
                u, v = edges[random_edge][0], edges[random_edge][1]
                if not adjacency_temp[u][v] == 0:
                    adjacency_temp[u][v] = 0
                    adjacency_temp[v][u] = 0
                    if is_consistent(adjacency_temp):
                        self.adjacency = adjacency_temp.copy()
                        all_edges -= 1
                    if [u, v] in edges:
                        edges.remove([u, v])
                    else:
                        edges.remove([v, u])
            return graph(adjacency=self.adjacency)
