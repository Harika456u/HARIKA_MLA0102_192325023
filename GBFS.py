import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))

    visited = set()
    parent = {start: None}

    while priority_queue:
        h, current = heapq.heappop(priority_queue)

        if current == goal:
            break

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    # Reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    return path


# -------- GRAPH DEFINITION --------
graph = {
    'A': ['D', 'C', 'B'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'F'],
    'E': ['B', 'H'],
    'F': ['D', 'C', 'G'],
    'H': ['E', 'G'],
    'G': []
}

# -------- HEURISTIC VALUES --------
heuristic = {
    'A': 40,
    'B': 32,
    'C': 25,
    'D': 35,
    'E': 19,
    'F': 17,
    'H': 10,
    'G': 0   # Goal
}

# -------- RUN GBFS --------
start = 'A'
goal = 'G'

path = greedy_best_first_search(graph, heuristic, start, goal)
print("Greedy Best First Search Path:", path)
