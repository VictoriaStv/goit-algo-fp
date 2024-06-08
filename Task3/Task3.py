import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = {}

    def add_edge(self, start, end, weight):
        self.vertices[start][end] = weight

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))

        return distances

# Створення графа
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'E', 3)
graph.add_edge('C', 'D', 2)
graph.add_edge('D', 'E', 3)

# Побудова графа 
G = nx.Graph()

# Додавання вершин
for vertex in graph.vertices:
    G.add_node(vertex)

# Додавання ребер
for start in graph.vertices:
    for end, weight in graph.vertices[start].items():
        G.add_edge(start, end, weight=weight)

# Визначення позицій вершин для відображення
pos = nx.spring_layout(G)

# Ваги ребер
labels = nx.get_edge_attributes(G, 'weight')

# Відображення графа
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=20, font_weight='bold', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=12)

plt.title('Граф')
plt.show()

# Виклик методу для знаходження найкоротших шляхів від вершини 'A'
shortest_paths_from_A = graph.dijkstra('A')
print("Найкоротші шляхи від вершини 'A':", shortest_paths_from_A)