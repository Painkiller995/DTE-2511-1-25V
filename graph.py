"""
A module for representing and manipulating graphs.
"""


class Node:
    """
    A class representing a node in a graph.
    """

    def __init__(self, label: str):
        self._label = label


class Graph:
    """
    Graph
    """

    def __init__(self):
        self._nodes = {}
        self._adjacency_list = {}

    def add_node(self, label: str) -> Node:
        """
        Adds a node to the graph.
        """
        node = Node(label)
        self._nodes[label] = node
        self._adjacency_list[node] = []
        return node

    def add_edge(self, from_label: str, to_label: str) -> None:
        """
        Adds an edge between two nodes in the graph.
        """

        if from_label not in self._nodes:
            raise ValueError("Something to write here 1")

        if to_label not in self._nodes:
            raise ValueError("Something to write here 2")

        from_node = self._nodes[from_label]
        to_node = self._nodes[to_label]

        if from_node not in self._adjacency_list:
            raise ValueError("Something to write here 3")

        edges = self._adjacency_list[from_node]

        edges.append(to_node)

    def remove_node(self, label: str) -> None:
        """
        Removes a node and all edges connected to it.
        """
        if label not in self._nodes:
            return

        node = self._nodes[label]

        for neighbors in self._adjacency_list.values():
            if node in neighbors:
                neighbors.remove(node)

        del self._adjacency_list[node]
        del self._nodes[label]

    def remove_edge(self, from_label: str, to_label: str) -> None:
        """
        Removes an edge from one node to another in the graph.
        """
        if from_label not in self._nodes or to_label not in self._nodes:
            return

        from_node = self._nodes[from_label]
        to_node = self._nodes[to_label]

        if to_node in self._adjacency_list.get(from_node, []):
            self._adjacency_list[from_node].remove(to_node)

    def __str__(self) -> str:
        lines = []
        for source, connections in self._adjacency_list.items():
            if connections:
                conn_str = ", ".join(conn._label for conn in connections)
                lines.append(f"{source._label} -> {conn_str}")
            else:
                lines.append(f"{source._label} -> (no connections)")
        return "\n".join(lines)


if __name__ == "__main__":
    test = Graph()
    test.add_node("one")
    test.add_node("two")
    test.add_node("three")
    test.add_edge("three", "two")
    test.remove_edge("one", "two")
    print(test)
