# File name: DSF_fn.py
# Implementasjon av DFS (Depth-First Search) i Python
# Bruker deque for å håndtere naboer i riktig rekkefølge

from collections import deque


def dfs(graph, start_node):
    visited = set()
    stack = deque([start_node])
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return order

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['A', 'B', 'E'],
    'E': ['C', 'D']
}

# Utfør DFS fra node 'A'
dfs_order = dfs(graph, 'A')
print("DFS-traversering fra node 'A':", dfs_order)