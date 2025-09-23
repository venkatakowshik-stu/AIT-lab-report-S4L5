matrix =[
    [1 ,  2],
   [3 ,  4]
    ]
for i in matrix:
    for j in i:
     print(j,end=" ")
    print()  

graph=[
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
for row in graph:
    print(*row) 
def find_paths(graph, start, goal):
    def dfs(x, y, path):
        
        if (x, y) == goal:
            paths.append(path.copy())
            return

     
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and graph[nx][ny] == 0 and (nx, ny) not in path:
                path.append((nx, ny))
                dfs(nx, ny, path)
                path.pop()  

    paths = []
    dfs(start[0], start[1], [start])
    return paths


graph = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
start = (0, 0)
goal = (2, 1)

all_paths = find_paths(graph, start, goal)

for path in all_paths:
    print(path)
    
    

