"""
This module is an implementation of a weighted graph.

This implementation could be improved in the feature please check github for the latest version.
https://github.com/Painkiller995/DTE-2511-1-25V

"""


class Node:
    """
    A class representing a node in a graph.
    """

    def __init__(self, label: str):
        self._label = label


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
        self._adjacency_list = {}

    def add_node(self, label: str):
        new_node = Node(label)
        self._nodes[label] = new_node
        self._adjacency_list[new_node] = []

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

        if from_node not in self._adjacency_list:
            raise ValueError("Something to write here 3")

        if to_node not in self._adjacency_list:
            raise ValueError("Something to write here 3")

        from_edges = self._adjacency_list[from_node]
        to_edges = self._adjacency_list[to_node]

        new_from_edge = Edge(from_node=from_node, to_node=to_node, weight=weight)
        new_to_edge = Edge(from_node=to_node, to_node=from_node, weight=weight)

        from_edges.append(new_from_edge)
        to_edges.append(new_to_edge)
