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
    'A': ['B1', 'B2', 'B3'],  
    'B1': [12, 10, 3], 
    'B2': [5, 8, 10],   
    'B3': [11, 2, 12]   
}


optimal_value, optimal_path = minimax('A', 0, True, tree)


print("Optimal Value:", optimal_value)
print("Optimal Path:", " -> ".join(map(str, optimal_path)))
