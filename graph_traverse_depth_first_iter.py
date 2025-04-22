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
        stack = []
        visited = set()

        stack.append(root)

        while stack:
            node = stack.pop()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self._adjacency_list[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

            print(node._label)


if __name__ == "__main__":
    graph = GraphTraverseDepthFirst()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_edge("A", "B")
    graph.add_edge("B", "D")
    graph.add_edge("B", "D")
    graph.add_edge("D", "C")
    graph.add_edge("A", "C")
    print(graph)
    print("--" * 20)
    graph.traverse_depth_first("A")
