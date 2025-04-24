from Ex_change_prims_dijkstra_start import Graph

# Small graph
vertices_small = ['A', 'B', 'C', 'D', 'E']
edges_small = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 6),
    ('C', 'D', 3),
    ('C', 'E', 5),
    ('D', 'E', 2)
]
graph_small = Graph(vertices_small, edges_small)

# Apply Prim's MST on the small graph
mst_edges_small, total_weight_small, visit_order_small = graph_small.prim_mst('A')
print("Prim's MST (Small Graph):")
print("Edges:", mst_edges_small)
print("Total Weight:", total_weight_small)
print("Visit Order:", visit_order_small)

# Apply Dijkstra's algorithm on the small graph
distances_small, paths_small = graph_small.dijkstra('A')
print("\nDijkstra's Shortest Paths (Small Graph):")
print("Distances:", distances_small)
print("Paths:")
for vertex, path in paths_small.items():
    print(f"  {vertex}: {path}")

# Larger graph (from TestWeightedGraph.py)
vertices_large = ["Seattle", "San Francisco", "Los Angeles",
                  "Denver", "Kansas City", "Chicago", "Boston", "New York",
                  "Atlanta", "Miami", "Dallas", "Houston"]
edges_large = [
    ("Seattle", "San Francisco", 807), ("Seattle", "Denver", 1331), ("Seattle", "Chicago", 2097),
    ("San Francisco", "Seattle", 807), ("San Francisco", "Los Angeles", 381), ("San Francisco", "Denver", 1267),
    ("Los Angeles", "San Francisco", 381), ("Los Angeles", "Denver", 1015), ("Los Angeles", "Kansas City", 1663), ("Los Angeles", "Dallas", 1435),
    ("Denver", "Seattle", 1331), ("Denver", "San Francisco", 1267), ("Denver", "Los Angeles", 1015), ("Denver", "Kansas City", 599), ("Denver", "Chicago", 1003),
    ("Kansas City", "Los Angeles", 1663), ("Kansas City", "Denver", 599), ("Kansas City", "Chicago", 533), ("Kansas City", "New York", 1260),
    ("Kansas City", "Atlanta", 864), ("Kansas City", "Dallas", 496),
    ("Chicago", "Seattle", 2097), ("Chicago", "Denver", 1003), ("Chicago", "Kansas City", 533), ("Chicago", "Boston", 983), ("Chicago", "New York", 787),
    ("Boston", "Chicago", 983), ("Boston", "New York", 214),
    ("New York", "Kansas City", 1260), ("New York", "Chicago", 787), ("New York", "Boston", 214), ("New York", "Atlanta", 888),
    ("Atlanta", "Kansas City", 864), ("Atlanta", "New York", 888), ("Atlanta", "Miami", 661), ("Atlanta", "Dallas", 781), ("Atlanta", "Houston", 810),
    ("Miami", "Atlanta", 661), ("Miami", "Houston", 1187),
    ("Dallas", "Los Angeles", 1435), ("Dallas", "Kansas City", 496), ("Dallas", "Atlanta", 781), ("Dallas", "Houston", 239),
    ("Houston", "Atlanta", 810), ("Houston", "Miami", 1187), ("Houston", "Dallas", 239)
]
graph_large = Graph(vertices_large, edges_large)

# Apply Prim's MST on the large graph
mst_edges_large, total_weight_large, visit_order_large = graph_large.prim_mst("Seattle")
print("\nPrim's MST (Larger Graph):")
print("Edges:", mst_edges_large)
print("Total Weight:", total_weight_large)
print("Visit Order:", visit_order_large)

# Apply Dijkstra's algorithm on the large graph
distances_large, paths_large = graph_large.dijkstra("Seattle")
print("\nDijkstra's Shortest Paths (Larger Graph):")
print("Distances:", distances_large)
print("Paths:")
for vertex, path in paths_large.items():
    print(f"  {vertex}: {path}")
