"""
This module is an implementation of Dijkstra's algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import heapq

from weighted_graph_obj import Edge, Node, WeightedGraph


class Dijkstra(WeightedGraph):
    """
    A class to represent Dijkstra's algorithm.

    Attributes:
        graph (WeightedGraph): The graph on which Dijkstra's algorithm is applied.
    """

    def __init__(self):
        super().__init__()
        self._distances: dict[Node, int] = {}
        self._previous_nodes: dict[Node, Node] = {}

    def dijkstra(self, start_label: str) -> None:
        """
        Applies Dijkstra's algorithm to find the shortest path from the start node to all other nodes.

        Args:
            start_label (str): The label of the starting node.
        """
        pq = []  # Priority queue for the nodes to visit


if __name__ == "__main__":
    graph = Dijkstra()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")
    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "C", 4)
    graph.add_edge("A", "D", 2)
    graph.add_edge("B", "D", 6)
    graph.add_edge("C", "D", 1)
    graph.add_edge("B", "E", 1)
    graph.add_edge("D", "E", 5)

    print(graph)
