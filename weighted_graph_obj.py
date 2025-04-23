"""
This module is an implementation of a weighted undirected graph.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


class Node:
    """
    A class representing a node in a graph.
    """

    def __init__(self, label: str):
        self._label = label
        self._edges: list["Edge"] = []

    def add_edge(self, target_node: "Node", weight: int) -> None:
        """
        Adds an edge to the node.
        """
        edge = Edge(from_node=self, to_node=target_node, weight=weight)
        self._edges.append(edge)

    def list_edges(self) -> list["Edge"]:
        """
        Returns a list of edges connected to this node.
        """
        return self._edges


class Edge:
    """
    A class representing an edge in a graph.
    """

    def __init__(self, from_node: Node, to_node: Node, weight: int):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


class WeightedGraph:
    """
    A class to represent a weighted graph.

    Attributes:
        vertices (list): A list of vertices in the graph.
        edges (dict): A dictionary where keys are vertices and values are lists of tuples (neighbor, weight).
    """

    def __init__(self):
        self._nodes = {}

    def add_node(self, label: str):
        new_node = Node(label)
        self._nodes[label] = new_node
        return new_node

    def add_edge(self, from_label: str, to_label: str, weight: int) -> None:
        """
        Adds an edge between two nodes in the graph.
        """

        if from_label not in self._nodes:
            raise ValueError("Something to write here 1")

        if to_label not in self._nodes:
            raise ValueError("Something to write here 2")

        from_node = self._nodes[from_label]
        to_node = self._nodes[to_label]

        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node, weight)

    def __str__(self) -> str:
        result = ""
        for node in self._nodes.values():
            edges = ", ".join(f"({node._label} --> {edge.to_node._label}, weight: {edge.weight})" for edge in node.list_edges())
            result += f"{node._label}: {edges}\n"
        return result.strip()


if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "C", 2)

    print(graph)
