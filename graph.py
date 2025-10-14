nodes = ['A', 'B', 'C', 'D']
edges = {
    ('A', 'B'): 2,
    ('B', 'C'): 3,
    ('C', 'D'): 1,
    ('D', 'A'): 4
}

print("Nodes in the graph:")
for node in nodes:
    print(node)

print("Cost of every edge in the graph:")
for edge, cost in edges.items():
    print(f"Edge {edge[0]}->{edge[1]}: {cost}")

path_one = [('A', 'B'), ('B', 'C'), ('C', 'D')]
path_one_cost = sum(edges[edge] for edge in path_one)
print("In path one: A->B->C->D")
print(f"Total cost for path one: {path_one_cost}")

path_two = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
path_two_cost = sum(edges[edge] for edge in path_two)
print("In path two: A->B->C->D->A")
print(f"Edges in path two: {path_two}")
print(f"Total cost for path two: {path_two_cost}")

total_cost = sum(edges.values)
