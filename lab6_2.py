import numpy as np

def floyd_warshall_verbose(edges, n):
    INF = float('inf')
    
    dist = np.full((n, n), INF)
    np.fill_diagonal(dist, 0)
    pred = np.full((n, n), -1)

    for u, v, w in edges:
        dist[u-1][v-1] = w
        dist[v-1][u-1] = w
        pred[u-1][v-1] = u - 1
        pred[v-1][u-1] = v - 1

    for k in range(n):
        changes = []
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:
                    old_value = dist[i][j]
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
                    changes.append(
                        f"dist[{i+1}][{j+1}] змінено з {old_value} на {dist[i][j]} через {k+1} (шлях {i+1} → {k+1} → {j+1})"
                    )

        print(f"\n=== КРОК k = {k+1} ===")
        if changes:
            print("Зміни:")
            for change in changes:
                print(" -", change)
        else:
            print("Без змін.")
        
        print("\nМатриця відстаней:")
        for row in dist:
            print(" ".join(f"{x:5.0f}" if x != INF else "  inf" for x in row))

        print("\nМатриця предків:")
        for row in pred:
            print(" ".join(f"{x+1:5}" if x != -1 else "  -1" for x in row))
        
        print("-" * 60)

    return dist, pred


# ----------------------------- ВХІДНІ ДАНІ -----------------------------

edges = [
    (1, 2, -1),
    (1, 4, 6),
    (1, 5, 10),
    (1, 6, 11),
    (1, 8, -5),
    (2, 3, 3),
    (2, 4, 4),
    (2, 7, 13),
    (4, 5, 11),
    (5, 6, 4),
    (6, 7, 1),
    (7, 8, -5)
]
n = 8

dist_matrix, pred_matrix = floyd_warshall_verbose(edges, n)

# ----------------------------- ОЧІКУВАНІ РЕЗУЛЬТАТИ -----------------------------

expected_dist = np.array([
    [ 0.,  8.,  8.,  5.,  6.,  8.,  9.,  7.],
    [ 8.,  0.,  6.,  9., 10.,  9.,  8., 10.],
    [ 8.,  6.,  0.,  3.,  4.,  3.,  2.,  4.],
    [ 5.,  9.,  3.,  0.,  1.,  5.,  5.,  6.],
    [ 6., 10.,  4.,  1.,  0.,  4.,  5.,  5.],
    [ 8.,  9.,  3.,  5.,  4.,  0.,  1.,  1.],
    [ 9.,  8.,  2.,  5.,  5.,  1.,  0.,  2.],
    [ 7., 10.,  4.,  6.,  5.,  1.,  2.,  0.]
])

expected_pred = np.array([
    [-1,  1,  4,  1,  4,  8,  8,  1],
    [ 2, -1,  2,  3,  4,  7,  3,  7],
    [ 4,  3, -1,  3,  4,  7,  3,  7],
    [ 4,  3,  4, -1,  4,  5,  3,  6],
    [ 4,  3,  4,  5, -1,  5,  6,  6],
    [ 8,  3,  7,  5,  6, -1,  6,  6],
    [ 8,  3,  7,  3,  6,  7, -1,  7],
    [ 8,  3,  7,  5,  6,  8,  8, -1]
])

# ----------------------------- ПЕРЕВІРКА -----------------------------

print("\n=== ПЕРЕВІРКА ФІНАЛЬНИХ МАТРИЦЬ ===")

# Порівняння ваг
weights_match = np.allclose(dist_matrix, expected_dist, atol=1e-6)

# Порівняння предків
pred_plus_1 = np.where(pred_matrix == -1, -1, pred_matrix + 1)
predecessors_match = np.array_equal(pred_plus_1, expected_pred)

if weights_match and predecessors_match:
    print("Матриці dist та pred повністю співпадають з очікуваними!")
else:
    if not weights_match:
        print("Матриця dist не співпадає з очікуваною!")
    if not predecessors_match:
        print("Матриця pred не співпадає з очікуваною!")

print("\n=== КІНЕЦЬ ПЕРЕВІРКИ ===")
