import heapq

# Graph represented as adjacency list
# graph[node] = [(neighbor, cost), ...]
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4)],
    'B': [('C', 4), ('E', 5)],
    'C': [],
    'D': [('E', 2)],
    'E': [('F', 4)],
    'F': [('G', 3.5)],
    'G': []
}

# Heuristic values h(n)
heuristic = {
    'S': 11.5,
    'A': 10.1,
    'B': 5.8,
    'C': 3.4,
    'D': 9.2,
    'E': 7.1,
    'F': 3.5,
    'G': 0
}

def a_star(start, goal):
    # Priority queue: (f(n), g(n), node, path)
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return path, g

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (f_new, g_new, neighbor, path + [neighbor])
                )

    return None, float('inf')


# Run A* Search
path, cost = a_star('S', 'G')

print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)
