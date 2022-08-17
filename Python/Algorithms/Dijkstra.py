class Node:
    def __init__(self, number, *args):
        self.number = number
        self.connected_nodes = list(args)
        self.start = 0

    def connect(self, node):
        node.connected_nodes.append(self)
        self.connected_nodes.append(node)

    def __iter__(self):
        return iter(self.connected_nodes)

    def __str__(self):
        return f'Node #{self.number}'

    def __eq__(self, other):
        return self.number == other.number

    def __hash__(self):
        return hash(self.number)


def print_dict(toprint):
    for key, value in toprint.items():
        print(key, value)


weight_stub = 1


def path_on_graph(graph, start_node, end_node):
    nodes_weights = {}
    for key in graph:
        nodes_weights[key] = None
    nodes_weights[start_node] = 0

    next_nodes = [start_node]
    seen_nodes = set()

    while next_nodes:
        current_node = next_nodes.pop()
        for n in current_node:
            if n not in seen_nodes:
                new_weight = nodes_weights[current_node] + weight_stub
                if nodes_weights[n] is None or new_weight < nodes_weights[n]:
                    nodes_weights[n] = new_weight
                next_nodes.append(n)
        seen_nodes.add(current_node)

    print_dict(nodes_weights)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.connect(n2)
    n1.connect(n5)
    n1.connect(n3)
    n1.connect(n4)
    n2.connect(n4)
    n3.connect(n4)
    n5.connect(n3)
    n5.connect(n4)

    graph = [n1, n2, n3, n4, n5]
    path_on_graph(graph, n2, n5)
