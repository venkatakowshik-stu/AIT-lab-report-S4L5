import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 7)],
    'C': [('A', 4), ('D', 3)],
    'D': [('B', 7), ('C', 3)]
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 3,
    'D': 0
}

def a_star(graph, start, goal, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))

    return None, float('inf')


# Run A* Algorithm
path, cost = a_star(graph, 'A', 'D', heuristic)

print("Optimal path:", path)
print("Total cost:", cost)


# Print nodes in the graph
print("\nNodes in the graph:")
for node in graph.keys():
    print(node)

# Print cost of every edge in the graph
print("\nCost of every edge in the graph:")
seen_edges = set()
for node in graph:
    for neighbor, weight in graph[node]:
        edge = tuple(sorted((node, neighbor)))
        if edge not in seen_edges:
            print(f"Edge {edge[0]} - {edge[1]}: {weight}")
            seen_edges.add(edge)
