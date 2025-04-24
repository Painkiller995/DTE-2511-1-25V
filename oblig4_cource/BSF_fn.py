# File name: BSF_fn.py
# Implementasjon av BFS (Breadth-First Search) i Python
# Returnerer besøksrekkefølgen til nodene i grafen

from collections import deque


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node]) # Bruker deque som kø
    visited.add(start_node)
    result = []

    while queue:
        node = queue.popleft() # popleft får queue til å oppføre seg som en kø
        result.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['A', 'B', 'E'],
    'E': ['C', 'D']
}

# Utfør BFS startende fra node 'A'
bfs_result = bfs(graph, 'A')
print("BFS-traversering fra node 'A':", bfs_result)