import networkx as nx
import matplotlib.pyplot as plt

# Початковий список ребер з їх вагою
edges = [
    (1, 2, 8),
    (1, 4, 5),
    (1, 8, 7),
    (2, 3, 6),
    (3, 4, 3),
    (3, 7, 2),
    (4, 5, 1),
    (4, 6, 7),
    (5, 6, 4),
    (6, 7, 1),
    (6, 8, 1),
    (7, 8, 2)
]

# Створення графа
G = nx.Graph()

# Додавання ребер до графа
G.add_weighted_edges_from(edges)

# Малювання графа
pos = nx.spring_layout(G)  # Позиції для вершин (застосовує спіральну розкладку)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12)

# Додавання ваг до ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Відображення графа
plt.show()