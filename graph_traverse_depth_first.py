"""
A module for representing traversing a graph using depth-first search.
"""

from graph import Graph, Node


class GraphTraverseDepthFirst(Graph):
    """
    A class for traversing a graph using depth-first search.
    """

    def traverse_depth_first(self, root_label: str) -> None:
        """
        Traverses the graph using depth-first search.
        """
        if root_label not in self._nodes:
            raise ValueError("Node not found in the graph.")

        root = self._nodes[root_label]
        visited = set()

        self._traverse_depth_first(root, visited)

    def _traverse_depth_first(self, node: Node, visited: set) -> None:
        """
        Traverses the graph using depth-first search.
        """
        print(node._label)

        visited.add(node)

        for neighbor in self._adjacency_list[node]:
            if neighbor not in visited:
                self._traverse_depth_first(neighbor, visited)


if __name__ == "__main__":
    graph = GraphTraverseDepthFirst()
    graph.add_node("one")
    graph.add_node("two")
    graph.add_node("three")
    graph.add_node("four")
    graph.add_edge("three", "two")
    graph.add_edge("three", "four")
    graph.add_edge("two", "one")
    graph.add_edge("four", "one")
    print(graph)
    print("--" * 20)
    graph.traverse_depth_first("three")
