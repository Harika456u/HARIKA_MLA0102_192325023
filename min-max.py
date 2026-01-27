import math

# Terminal node values (INPUT)
values = [2, 3, 5, 9, 0, 1, 7, 5]

def minimax(depth, node_index, is_max_player):
    # If leaf node reached, return its value
    if depth == tree_height:
        return values[node_index]

    if is_max_player:
        return max(
            minimax(depth + 1, node_index * 2, False),
            minimax(depth + 1, node_index * 2 + 1, False)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True),
            minimax(depth + 1, node_index * 2 + 1, True)
        )

# Height of the game tree
tree_height = int(math.log2(len(values)))

# Calling minimax from root (MAX player starts)
optimal_value = minimax(0, 0, True)

print("Optimal value using Minimax:", optimal_value)
