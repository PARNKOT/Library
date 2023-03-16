#Алгоритм поиска в глубину

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


# For example:


class NodeIterator:
    def __init__(self, node):
        self.node = node
        self.count = 0

    def __next__(self):
        pass


class Node:
    def __init__(self, number, *args):
        self.number = number
        self.connected_nodes = list(args)
        self.start = 0

    def __iter__(self):
        return iter(self.connected_nodes)

    def __str__(self):
        return f'Node #{self.number}'

    def __eq__(self, other):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6, n1, n2, n3, n4, n5)
    n7 = Node(7)
    n8 = Node(8, n6, n7)
    print(DFS(n8, n2))
