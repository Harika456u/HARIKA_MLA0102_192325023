from collections import deque

# Graph Input
graph = {
    1: [2, 7],
    2: [3, 6],
    3: [4, 5],
    4: [],
    5: [],
    6: [],
    7: [8, 10],
    8: [9],
    9: [],
    10: []
}

# DFS (Recursion - Stack / LIFO)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# BFS (Queue - FIFO)
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Function Calls
print("DFS Traversal:")
dfs(graph, 1)

print("\n\nBFS Traversal:")
bfs(graph, 1)
