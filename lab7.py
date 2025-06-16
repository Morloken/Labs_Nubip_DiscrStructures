import matplotlib.pyplot as plt
import networkx as nx
import random

# Матриця пропускних спроможностей
capacity_matrix = [
    [0, 12, 0, 8, 0, 7, 0],
    [0, 0, 0, 11, 0, 0, 14],
    [0, 5, 0, 0, 12, 0, 6],
    [0, 0, 10, 0, 0, 0, 5],
    [0, 8, 0, 0, 0, 11, 0],
    [0, 0, 9, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Матриця потоків
flow_matrix = [
    [0, 3, 0, 2, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 3],
    [0, 1, 0, 0, 3, 0, 3],
    [0, 0, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0],
    [0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Імена вершин
nodes = ['x0', '1', '2', '3', '4', '5', 'z']

# Створення графу
G = nx.DiGraph()

# Додаємо ребра з підписами у вигляді «потік/пропускна здатність»
for i in range(len(capacity_matrix)):
    for j in range(len(capacity_matrix[i])):
        cap = capacity_matrix[i][j]
        flow = flow_matrix[i][j]
        if cap > 0:
            G.add_edge(nodes[i], nodes[j], label=f"{flow}/{cap}")

# Функція для малювання графа

def draw_random_layout():
    pos = {node: (random.uniform(-1, 1), random.uniform(-1, 1)) for node in G.nodes()}

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='#86C5D8')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Транспортна мережа: Потік / Пропускна здатність")
    plt.axis('off')
    plt.show()

# Викликаємо малювання
draw_random_layout()