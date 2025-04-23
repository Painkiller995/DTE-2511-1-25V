from collections import deque


class Graph:
    def __init__(self, vertices=None, edges=None):
        self.vertices = vertices if vertices else []
        self.neighbors = self.get_adjacency_list(edges if edges else [])

    def get_adjacency_list(self, edges):
        neighbors = {v: [] for v in self.vertices}
        for u, v in edges:
            neighbors[u].append(v)
            # neighbors[v].append(u)  # assuming undirected graph
        return neighbors

    def get_size(self):
        return len(self.vertices)

    def get_vertices(self):
        return self.vertices

    def get_degree(self, v):
        return len(self.neighbors[v])

    def print_edges(self):
        for u in self.vertices:
            print(f"{u}: {self.neighbors[u]}")

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.neighbors[vertex] = []

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.neighbors[u].append(v)
            self.neighbors[v].append(u)

    def dfs(self, start_node):
        visited = set()
        stack = deque([start_node])
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbor in reversed(self.neighbors[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in self.neighbors[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def is_connected(self):
        if not self.vertices:
            return True
        visited = self.dfs(self.vertices[0])
        return len(visited) == len(self.vertices)

    def bfs_all_shortest_paths(self, start_node):
        visited = {start_node: None}
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            for neighbor in self.neighbors[node]:
                if neighbor not in visited:
                    visited[neighbor] = node
                    queue.append(neighbor)

        paths = {}
        for v in self.vertices:
            if v not in visited:
                paths[v] = None
                continue
            path = []
            current = v
            while current is not None:
                path.append(current)
                current = visited[current]
            paths[v] = path[::-1]

        return paths
