def greedy_colouring(graph):
    colour_assignment = {}
    for node in graph:
        used_colours = {colour_assignment[neighbour] for neighbour in graph[node] if neighbour in colour_assignment}
        colour = 1
        while colour in used_colours:
            colour += 1
        colour_assignment[node] = colour
    return colour_assignment

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

colour_result = greedy_colouring(graph)
print("colouring_result =", colour_result)
