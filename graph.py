import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class graph:
    def __init__(self, adjacency):
        def update_neighbors():
            def is_neighbor(n, m):
                if self.adjacency[n][m] == 1:
                    return True
                return False

            for i in range(self.n):
                neighbors = []
                for j in range(self.n):
                    if is_neighbor(i, j):
                        neighbors.append(j)
                self.neighbors_list.append(neighbors)

        self.adjacency = adjacency
        self.n = len(adjacency)
        self.neighbors_list = []
        update_neighbors()

    def get_n(self):
        return self.n

    def get_adjacency(self):
        return self.adjacency

    def get_neighbors(self, i):
        return self.neighbors_list[i]

    def get_degree(self, i):
        return sum(self.adjacency[i])

    def show_graph(self):
        adjacency_matrix = np.array(self.get_adjacency())
        rows, cols = np.where(adjacency_matrix == 1)
        edges = zip(rows.tolist(), cols.tolist())

        gr = nx.Graph()
        gr.add_edges_from(edges)

        label_dict = {}
        for i in range(len(adjacency_matrix)):
            label_dict[i] = str(i)

        nx.draw(gr, labels=label_dict, width=6, node_size=750, with_labels=True, edge_color='blue')
        plt.show()

    def show_graph_with_colour_edges(self, e):
        adjacency_matrix = np.array(self.get_adjacency())
        rows, cols = np.where(adjacency_matrix == 1)
        edges = zip(rows.tolist(), cols.tolist())
        gr = nx.Graph()
        gr.add_edges_from(edges)
        edges = gr.edges
        color_map = []
        for edge in edges:
            if list(edge) in e:
                color_map.append('green')
            else:
                color_map.append('blue')

        label_dict = {}
        for i in range(len(adjacency_matrix)):
            label_dict[i] = str(i)

        nx.draw(gr, labels=label_dict, width=6, node_size=750, with_labels=True, edge_color=color_map)
        plt.show()
