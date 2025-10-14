graph = {
    0: [1, 2],
    1: [3, 4],
    2: [],
    3: [],
    4: []
}

def dfs_iterative(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))
dfs_iterative(0)
