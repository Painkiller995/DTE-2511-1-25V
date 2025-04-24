from heapq import heappop, heappush


class Graph:
    def __init__(self, vertices=[], edges=[]):
        self._vertices = vertices if vertices else []
        self._neighbors = {vertex: [] for vertex in self._vertices}  # Adjacency list

        for edge in edges:
            if len(edge) == 3:  # Weighted edge (e.g., ('A', 'B', 5))
                self.add_edge(edge[0], edge[1], edge[2])

    def add_edge(self, from_vertex, to_vertex, weight=None):
        if from_vertex not in self._neighbors:
            self._neighbors[from_vertex] = []
        if to_vertex not in self._neighbors:
            self._neighbors[to_vertex] = []

        self._neighbors[from_vertex].append((to_vertex, weight))
        self._neighbors[to_vertex].append((from_vertex, weight))

    # Prim's Minimum Spanning Tree (MST)
    def prim_mst(self, start_node):
        visited = set() # hoder rede på besøkte noder
        mst_edges = []  # Vil holde kantene i MST (returverdi)
        total_weight = 0  # vil holde total vekt i MST (også returverdi)
        min_heap = []  # Prioritetskø for å velge den minste kanten
        visit_order = []  # Ny liste for besøksrekkefølge

        visited.add(start_node) # Marker startnode som besøkt
        # Legg alle kanter fra startnode inn i prioritetskøen (vekt, fra, til)
        for neighbor, weight in self._neighbors[start_node]: # finn  naboer via nabolista
            if weight is not None:  # Only consider weighted edges
                heappush(min_heap, (weight, start_node, neighbor)) # legg alle kanter i prioritetskøen
               
        while min_heap:
            weight, from_vertex, to_vertex = heappop(min_heap) # Hent den minste kanten
           
            if to_vertex not in visited:
                # ..da legger vi til kanten i MST (det er den minste kanten)
                # ..og markerer den som besøkt
                visited.add(to_vertex)
                mst_edges.append((from_vertex, to_vertex, weight)) # oppdaterer MST
                total_weight += weight # oppdaterer total vekt
                
                # Legg alle kanter fra to_vertex inn i prioritetskøen (vekt, fra, til)
                for neighbor, edge_weight in self._neighbors[to_vertex]:
                    if neighbor not in visited and edge_weight is not None:
                        heappush(min_heap, (edge_weight, to_vertex, neighbor))

        return mst_edges, total_weight, visit_order # visit_order er foreløpig dummy, bygg opp underveis

    # Dijkstra's Shortest Path Algorithm
    def dijkstra(self, start_node):
        distances = {vertex: float('inf') for vertex in self._vertices}
        distances[start_node] = 0
        parent_nodes = {vertex: None for vertex in self._vertices} # foreldrenoder, oppdateres underveis
        min_heap = [(0, start_node)]

        while min_heap:
            current_distance, current_node = heappop(min_heap)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self._neighbors[current_node]:
                if weight is not None:
                    new_distance = current_distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heappush(min_heap, (new_distance, neighbor))

        paths = {'A': ['A']} # dummy, bygg opp basert på parent_nodes
        return distances, paths
