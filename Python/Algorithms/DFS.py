Алгоритм поиска в глубину

def DFS(start_node, key):
    next_nodes = []
    seen_nodes = set()

    next_nodes.append(start_node)
    seen_nodes.add(start_node)

    while next_nodes:
        node = next_nodes.pop()
        if node == key:
            return node
        for n in node:
            if n not in seen_nodes:
                next_nodes.append(n)
                seen_nodes.add(n)
    return None
