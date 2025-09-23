import heapq

def path1(graph, start, end):
    
    priority_queue = [(0, start)]
    min_cost = {node: float('inf') for node in graph}
    min_cost[start] = 0

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            return current_cost
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return float('inf')  
graph = {
    'A': [('B', 2), ('D', 4)],
    'B': [('B', 3)],
    'C': [('D', 1)],
    'D': []
}


start_node = 'A'
end_node = 'D'
shortest_cost = path1(graph, start_node, end_node)
print(f"The shortest path cost from {start_node} to {end_node} is: {shortest_cost}")
def path2(graph, start, end):
    priority_queue = [(0, start)]
    min_cost = {node: float('inf') for node in graph}
    min_cost[start] = 0

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == end:
            return current_cost
        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))

    return float('inf')  
graph = {
    'A': [('B', 2), ('D', 4)],
    'B': [('B', 3)],
    'C': [('D', 1)],
    'D': []
}


start_node = 'A'
end_node = 'A'
shortest_cost = path1(graph, start_node, end_node)
print(f"The shortest path cost from {start_node} to {end_node} is: {shortest_cost}")
