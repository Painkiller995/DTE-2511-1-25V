"""
A module for representing traversing a graph using breadth-first search.
"""

from collections import deque

from graph import Graph


class GraphTraverseBreadthFirst(Graph):
    """
    A class for traversing a graph using breadth-first search.
    """

    def traverse_breadth_first(self, root_label: str) -> None:
        """
        Traverses the graph using breadth-first search.
        """
        if root_label not in self._nodes:
            raise ValueError("Node not found in the graph.")

        root = self._nodes[root_label]
        queue = deque()
        visited = set()

        queue.append(root)

        while queue:
            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)

            for neighbor in self._adjacency_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

            print(node._label)


if __name__ == "__main__":
    graph = GraphTraverseBreadthFirst()
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
    graph.traverse_breadth_first("A")
