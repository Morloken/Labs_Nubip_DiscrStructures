import numpy as np

def floyd_warshall(edges, n):  #функція 
    INF = float('inf')
    
    # створення матриці відстаней
    dist = np.full((n, n), INF)
    np.fill_diagonal(dist, 0)
    
    # створення матриці предків
    pred = np.full((n, n), -1)
    
    # Заповнення матриці згідно зі списком ребер (зменшуємо номери вершин на 1)
    for u, v, w in edges:
        dist[u - 1][v - 1] = w
        dist[v - 1][u - 1] = w  # бо граф неорієнтований
        pred[u - 1][v - 1] = u - 1
        pred[v - 1][u - 1] = v - 1
    
    # Алгоритм Флойда-Воршалла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:  # перевірка, чи можна поліпшити шлях
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    return dist, pred

# список ребер
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
n = 8  # Кількість вершин

shortest_paths, predecessors = floyd_warshall(edges, n)

# Виведення матриці відстаней
print("Матриця відстаней:")
print(shortest_paths)

# Виведення матриці предків з +1, де це не -1
print("\nМатриця предків:")
pred_plus_one = np.where(predecessors == -1, -1, predecessors + 1)
print(pred_plus_one)
