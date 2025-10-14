import random

D = [
    [0, 2, 2, 5],
    [2, 0, 3, 4],
    [2, 3, 0, 1],
    [5, 4, 1, 0]
]

N = len(D)
pher = [[1] * N for _ in range(N)]
a, b = 1, 2
evap = 0.5
pc = 1
best_path, best_dist = None, float('inf')

def probs(c, visited):
    p = [
        (pher[c][i] ** a) * ((1 / D[c][i]) ** b)
        if i not in visited and D[c][i] > 0 else 0
        for i in range(N)
    ]
    s = sum(p)
    if s == 0:
        p = [1 if i not in visited else 0 for i in range(N)]
        s = sum(p)
    return [x / s for x in p]

def wchoice(choices, weights):
    r = random.random() * sum(weights)
    for c, w in zip(choices, weights):
        r -= w
        if r <= 0:
            return c
    return choices[-1]

for _ in range(100):
    paths, dists = [], []
    for _ in range(4):
        visited = [random.randint(0, N - 1)]
        while len(visited) < N:
            next_city = wchoice(range(N), probs(visited[-1], visited))
            visited.append(next_city)
        visited.append(visited[0])
        dist = sum(D[visited[i]][visited[i + 1]] for i in range(N))
        paths.append(visited)
        dists.append(dist)
        if dist < best_dist:
            best_dist, best_path = dist, visited
    for i in range(N):
        for j in range(N):
            pher[i][j] *= (1 - evap)
    for path, dist in zip(paths, dists):
        for i in range(len(path) - 1):
            pher[path[i]][path[i + 1]] += pc / dist

print("Best Path:", best_path)
print("Best Distance:", best_dist)
