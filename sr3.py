
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

G = nx.DiGraph()
edges = [
  (1,4,6),
  (4,2,2),
  (2,1,3),
  (3,1,4),
  (3,4,9),
  (4,5,7),
  (3,9,12),
  (3,6,1),
  (6,7,15),
  (4,7,3),
  (7,5,16),
  (5,11,8),
  (5,8,9),
  (9,6,8),
  (7,10,2),
  (7,11,15),
  (8,11,10),
  (9,10,9),
  (10,11,9),
  (12,9,16),
  (12,10,12),
  (13,10,1),
  (12,13,4),
]

G.add_weighted_edges_from(edges)

pos = {
    1: (-2.00, 2.00), 2: (-1.00, 2.00),

    3: (-2.00, 1.00), 4: (-1.00, 1.00), 5: (-0.50, 1.00), 

    6: (-1.50, 0.50), 7: (-1.00, 0.50), 8: (0.00, 0.50),

    9: (-2.00, 0.00), 10: (-1.00, 0.00), 11: (-0.50, 0.00),

    12: (-2.00, -1.00), 13: (-1.00, -1.00)
}

def path_weight(path):
    return sum(G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))

max_weight = 0
longest_paths = []

nodes = list(G.nodes)

for u in nodes:
    for v in nodes:
        if u != v:
            try:
                paths = list(nx.all_simple_paths(G, source=u, target=v))
                for path in paths:
                    w = path_weight(path)
                    if w > max_weight:
                        max_weight = w
                        longest_paths = [path]
                    elif w == max_weight:
                        longest_paths.append(path)
            except nx.NetworkXNoPath:
                continue

plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
nx.draw_networkx_labels(G, pos)

all_path_edges = {(path[i], path[i + 1]) for path in longest_paths for i in range(len(path) - 1)}
other_edges = [e for e in G.edges() if e not in all_path_edges]

edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color='gray',
                       arrows=True, arrowstyle='-|>', arrowsize=20)

colors = cm.rainbow(np.linspace(0, 1, len(longest_paths)))

for path, color in zip(longest_paths, colors):
    edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color=[color],
                           width=2.5, arrows=True, arrowstyle='-|>', arrowsize=20)

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.axis('off')
plt.title(f"Найдовші шляхи в графі (довжина: {max_weight})", fontsize=14)
plt.tight_layout()
plt.show()

print(f"Максимальна довжина шляху в графі: {max_weight}")
for i, path in enumerate(longest_paths, 1):
    print(f"{i}) Шлях: {path}")
