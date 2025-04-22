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
        self._all = set()
        self._visiting = set()
        self._visited = set()

    def has_cycle(self):
        # Add all nodes to the _all set
        self._all = set(self._nodes)

        # Check each node for cycles
        for node in self._nodes.values():
            if self._has_cycle(node):
                print("Graph has a cycle")
                return

        print("Graph does not have a cycle")

    def _has_cycle(self, node):
        if node in self._visiting:
            print(f"Cycle detected at node: {node._label}")
            return True

        if node in self._visited:
            return False

        self._visiting.add(node)

        for neighbor in self._adjacency_list[node]:
            if self._has_cycle(neighbor):
                return True

        self._visiting.remove(node)
        self._visited.add(node)

        return False


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
    # graph.add_edge("P", "X")  # This creates a cycle
    print(graph)
    print("--" * 20)
    graph.has_cycle()
