"""
This module is an implementation of minimum spanning tree

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

    def get_minimum_spanning_tree(self) -> WeightedGraph:
        tree_graph = WeightedGraph()
        edges = []

        start_node = next(iter(self._nodes.values()))

        for edge in start_node.list_edges():
            heapq.heappush(edges, (edge.weight, edge))

        tree_graph.add_node(start_node._label)

        while len(tree_graph._nodes) < len(self._nodes):
            _, min_edge = edges.pop()

            next_node = min_edge.to_node

            if next_node in tree_graph._nodes.values():
                continue

            tree_graph.add_node(next_node._label)
            tree_graph.add_edge(min_edge.from_node._label, next_node._label, min_edge.weight)

            for edge in next_node.list_edges():
                if edge.to_node not in tree_graph._nodes:
                    heapq.heappush(edges, (edge.weight, edge))

        print("Minimum Spanning Tree Edges:")
        for edge in tree_graph._nodes.values():
            for e in edge.list_edges():
                print(f"{edge._label} -- {e.to_node._label} (weight: {e.weight})")

        return tree_graph


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
    mst = prim.get_minimum_spanning_tree()
    print("Minimum Spanning Tree:")
