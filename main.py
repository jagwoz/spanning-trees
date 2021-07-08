from graph_generator import *
from spanning_trees import *
import random

if __name__ == '__main__':
    generator = graph_generator()
    graph = generator.next_graph(graph_type="percent", n=10, m=3, percent=0.5)
    graph.show_graph()

    nr_1 = spanning_trees_number_math(graph)
    nr_2, good_edges = spanning_trees_number_exact(graph)

    print("\nSpanning trees number (math): {}".format(nr_1))
    print("Spanning trees number (exact algorithm): {}".format(nr_2))

    print("\nSpanning trees examples:")
    for i in range(5):
        print(random.choice(good_edges))
    graph.show_graph_with_colour_edges(random.choice(good_edges))

