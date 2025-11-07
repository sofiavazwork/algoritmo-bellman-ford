class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            #self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bellman_ford(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        distances[start_vertex] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.adj_matrix[u][v] != 0:
                        if distances[u] + self.adj_matrix[u][v] < distances[v]:
                            distances[v] = distances[u] + self.adj_matrix[u][v]
                            print(f"Relaxing edge {self.vertex_data[u]}->{self.vertex_data[v]}, Updated distance to {self.vertex_data[v]}: {distances[v]}")

        return distances

g = Graph(5)

g.add_vertex_data(0, 'S')
g.add_vertex_data(1, 'A')
g.add_vertex_data(2, 'B')
g.add_vertex_data(3, 'C')
g.add_vertex_data(4, 'D')

#S
g.add_edge(0, 1, 3)  # S -> A, weight 3
g.add_edge(0, 2, 5)  # S -> B, weight 5

#A
g.add_edge(1, 4, 8)  # A -> D, weight 8
g.add_edge(1, 3, -5)  # A -> C, weight -5

#B
g.add_edge(2, 1, 6)  # B -> A, weight 6
g.add_edge(2, 3, 8)  # B -> C, weight 8
g.add_edge(2, 4, -9)  # B -> D, weight -9

#C
g.add_edge(3, 4, -3)  # C -> D, weight -3

#D
g.add_edge(4, 0, 2)  # D -> S, weight 2


# Running the Bellman-Ford algorithm from D to all vertices
print("\nThe Bellman-Ford Algorithm starting from vertex D:")
distances = g.bellman_ford('D')
for i, d in enumerate(distances):
    print(f"Distance from D to {g.vertex_data[i]}: {d}")
    
#Python
