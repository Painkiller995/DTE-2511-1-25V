"""
This module is an implementation of Dijkstra's algorithm.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""

import heapq
import itertools

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

        start_node = self._nodes[start_label]

        if start_node is None:
            raise ValueError(f"Node {start_label} not found in the graph.")

        pq = []

        self._distances[start_node] = 0
        heapq.heappush(pq, (0, start_node))

        visited = set()

        while pq:
            current_weight, current_node = heapq.heappop(pq)

            for edge in current_node.list_edges():
                neighbor = edge.to_node
                weight = edge.weight

                if neighbor in visited:
                    continue

                new_distance = current_weight + weight

                print(f"New distance for {neighbor._label} starting from {current_node._label} is {new_distance}")

                if new_distance < self._distances.get(neighbor, 1000):
                    self._distances[neighbor] = new_distance
                    self._previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (edge.weight, edge.to_node))

            visited.add(current_node)

    def print_table(self) -> None:
        """
        Prints the table of distances and previous nodes.
        """
        print("Node\tDistance\tPrevious Node")
        for node in self._nodes.values():
            distance = self._distances.get(node, float("inf"))
            previous = self._previous_nodes.get(node, None)
            previous_label = previous._label if previous else "None"
            print(f"{node._label}\t{distance}\t\t{previous_label}")


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
    graph.dijkstra("A")
    graph.print_table()
