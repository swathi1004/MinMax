def minimax(node, depth, maximizing_player, tree):
    if node not in tree:
        return node, [node]

    if maximizing_player:
        best_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, depth + 1, False, tree)
            if value > best_value:
                best_value = value
                best_path = [node] + path
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, path = minimax(child, depth + 1, True, tree)
            if value < best_value:
                best_value = value
                best_path = [node] + path
        return best_value, best_path


tree = {
    3: [3, 1],  
    3: [3, 8],  
    1: [1, 4],  
    3: [-1, 3],  
    8: [-5, 8],  
    1: [1, -4],  
    4: [4, -3],  
    -1: [5, -1],  
    3: [4, 3],  
    -5: [-2, -5],  
    8: [9, 8],  
    1: [6, 1],  
    -4: [-1, -4],  
    4: [2, 4],  
    -3: [7, -3]  
}

optimal_value, optimal_path = minimax(3, 0, True, tree)

print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(map(str, optimal_path)))
