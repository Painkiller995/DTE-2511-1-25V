"""
A module for representing topological sorting of a graph.
"""

from graph import Graph


class GraphTopologicalSorting(Graph):
    """
    A class for representing a graph and performing topological sorting.
    """


if __name__ == "__main__":
    graph = GraphTopologicalSorting()
    graph.add_node("X")
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("P")
    graph.add_edge("X", "A")
    graph.add_edge("X", "B")
    graph.add_edge("A", "P")
    graph.add_edge("B", "P")
    print(graph)
    print("--" * 20)
