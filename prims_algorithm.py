"""
This module is an implementation of Prim's algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import heapq

from weighted_graph_obj import Edge, Node, WeightedGraph


class Prim(WeightedGraph):
    """
    A class to represent Prim's algorithm.

    Attributes:
        graph (WeightedGraph): The graph on which Prim's algorithm is applied.
    """

    def __init__(self):
        super().__init__()

    def prim(self, start_label: str) -> list[Edge]:
        if start_label not in self._nodes:
            raise ValueError(f"Node {start_label} not found in the graph.")

        start_node = self._nodes[start_label]
        visited = set()
        tree = set()
        self._prim(start_node, visited, tree)
        tree.add((0, start_label))
        # print(tree)

    def _prim(self, node: Node, visited: set, tree: set):
        available_edges = []

        visited.add(node)

        for edge in node.list_edges():
            if edge.to_node in visited:
                continue
            heapq.heappush(available_edges, (-edge.weight, edge))

        if available_edges:
            weight, shortest_edge = available_edges.pop()
            next_node = shortest_edge.to_node
            print((-weight, next_node._label))
            print(f"Ignore {available_edges}")
            tree.add((-weight, next_node._label))
            self._prim(next_node, visited, tree)


if __name__ == "__main__":
    prim = Prim()
    prim.add_node("A")
    prim.add_node("B")
    prim.add_node("C")
    prim.add_node("D")

    prim.add_edge("A", "C", 1)
    prim.add_edge("B", "C", 2)
    prim.add_edge("A", "B", 3)
    prim.add_edge("B", "D", 4)
    prim.add_edge("C", "D", 5)

    # Call Prim's algorithm here
    mst = prim.prim("A")
