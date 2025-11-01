import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):  # ✅ Fixed double underscores
        self.name = name
        self.parent = parent
        self.g = g  # cost from start node
        self.h = h  # heuristic cost to goal
        self.f = g + h  # total cost

    def __lt__(self, other):  # ✅ Fixed double underscores
        return self.f < other.f


def astar(graph, heuristics, start, goal):
    open_list = []
    closed_list = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]  # reverse path

        closed_list.add(current.name)

        for neighbor, cost in graph[current.name].items():
            if neighbor in closed_list:
                continue

            g = current.g + cost
            h = heuristics[neighbor]
            node = Node(neighbor, current, g, h)
            heapq.heappush(open_list, node)

    return None


# Define the graph
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 5},
    'D': {'G': 2},
    'E': {'G': 4},
    'F': {'G': 1},
    'G': {}
}

# Define heuristic values (estimated cost to goal)
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

# Run A* algorithm
path = astar(graph, heuristics, 'A', 'G')
print("Shortest path:", path)
