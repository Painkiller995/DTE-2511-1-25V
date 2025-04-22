"""
A module for representing topological sorting of a graph.
"""

from graph import Graph


class GraphTopologicalSorting(Graph):
    """
    A class for representing a graph and performing topological sorting.
    """

    def __init__(self):
        super().__init__()
        self._stack = []
        self._visited = set()

    def topological_sort(self) -> list:
        """
        Performs topological sorting on the graph.
        """

        for node in self._nodes.values():
            if node not in self._visited:
                self._topological_sort_util(node)

        return self._stack[::-1]  # Return in reverse order

    def _topological_sort_util(self, node) -> None:
        """
        A utility function to perform topological sorting.
        """

        if node in self._visited:
            return

        self._visited.add(node)

        for neighbor in self._adjacency_list[node]:
            self._topological_sort_util(neighbor)

        self._stack.append(node)


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

    print("Topological Sort:")
    sorted_nodes = graph.topological_sort()
    for node in sorted_nodes:
        print(node._label, end=" ")
