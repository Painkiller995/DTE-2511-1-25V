
# gjør import fra din egen Graph_xx.py fil
# Endret fra første versjon ved at kallene til bfs og dfs jobber på naboliste som 
# lages i __init__ metoden i Graph klassen, se lysbildene for en tilstrekkelig implementasjon
# av ei naboliste som bfs og dfs kan jobbe på.
cities = ["London", "Paris", "Berlin", "Madrid", "Rome", "Vienna", "Amsterdam", "Prague"]

edges = [
    ("London", "Madrid"),
    ("London", "Vienna"),
    ("London", "Prague"),
    ("London", "Paris"),
    ("Paris", "Madrid"),
    ("Berlin", "Prague"),
    ("Berlin", "Paris"),
    ("Rome", "London"),
    ("Rome", "Vienna"),
    ("Rome", "Prague"),
    ("Vienna", "Amsterdam"),
    ("Vienna", "Prague"),
    ("Vienna", "Madrid"),
    ("Vienna", "Paris"),
    ("Amsterdam", "Prague")
]

graph1 = Graph(cities, edges) # Create graph1
print("The vertices in graph1: " + str(graph1.get_vertices()))
print("The number of vertices in graph1: " + str(graph1.get_size()))

print("The degree for London is " + str(graph1.get_degree("London")))
print("The edges for graph1:")
graph1.print_edges()
    
print("adding a new vertex: Oslo")
graph1.add_vertex("Oslo") # Add a new vertex
print("Adding new edges: Oslo-London, Oslo-Paris")
graph1.add_edge("Oslo", "London")
graph1.add_edge("Oslo", "Paris")
print("\nThe edges for graph1 after adding a new vertex and 2 new edges:")
graph1.print_edges()

# test bfs
print("\nBFS traversal from London:")
bfs_result = graph1.bfs("London")  
print(bfs_result)
# test dfs
print("\nDFS traversal from London:")
dfs_result = graph1.dfs("London")
print(dfs_result)
# test is_connected
print("Is graph1 connected? " + str(graph1.is_connected()))

vertice2 = ['A', 'B', 'C', 'D', 'E']
edges2 = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('C', 'E'), ('D', 'E')]
graph2 = Graph(vertice2, edges2) # Create graph2
print("\nThe vertices in graph2: " + str(graph2.get_vertices()))
print("The number of vertices in graph2: " + str(graph2.get_size()))
print("The degree for A is " + str(graph2.get_degree("A")))
print("The edges for graph2:")
graph2.print_edges()
print("Is graph2 connected? " + str(graph2.is_connected()))
print("\nBFS traversal from A:")
bfs_result = graph2.bfs("A")
print(bfs_result)
print("\nBFS (all shortest path) traversal from A:")
bfs_result = graph2.bfs_all_shortest_paths("A")
print(bfs_result)
print("\nDFS traversal from A:")
dfs_result = graph2.dfs("A")
print(dfs_result)