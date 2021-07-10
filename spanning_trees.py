import numpy
import itertools
import copy

def spanning_trees_number_exact(g):
    def get_edges():
        all_edges = []
        for i in range(g.get_n()):
            neighbors = g.get_neighbors(i)
            for j in neighbors:
                new_edge = [j, i]
                new_edge.sort()
                if not new_edge in all_edges:
                    all_edges.append(new_edge)
        all_edges.sort()
        return all_edges

    e = get_edges()
    num = 0
    good_trees = []
    trees = list(itertools.combinations(e, g.get_n() - 1))

    for tree in trees:
        tree = list(tree)
        if tree[0][0] == 0:
            nodes = [0]
            potential_tree = copy.deepcopy(tree)
            while len(nodes) < g.get_n():
                nodes_size = len(nodes)
                for i in nodes:
                    for j in list(tree):
                        if i in j:
                            node_1 = j[0]
                            node_2 = j[1]
                            if not node_1 in nodes:
                                nodes.append(node_1)
                            if not node_2 in nodes:
                                nodes.append(node_2)
                            tree.remove(j)
                if nodes_size == len(nodes):
                    break
            if len(nodes) == g.get_n():
                good_trees.append(potential_tree)
                num += 1
    return num, good_trees


def spanning_trees_number_math(g):
    adjacency = g.get_adjacency()
    n = g.get_n()

    degrees = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                degrees[i][j] = g.get_degree(i)
	    degrees[i][j] -= adjacency[i][j]

    new_matrix = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
    for i in range(n - 1):
        for j in range(n - 1):
            new_matrix[i][j] = degrees[i + 1][j + 1]

    return numpy.linalg.det(new_matrix)