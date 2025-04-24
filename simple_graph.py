class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)
        return visited

    def _dfs_recursive(self, node, visited):
        visited.add(node)
        for neighbor in self.adj.get(node, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
