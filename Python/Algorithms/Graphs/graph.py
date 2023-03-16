import typing


class Node:
    def __init__(self, id: typing.Union[str, int, float], node_name="Node", *args):
        self.id = id
        self.connected_nodes = set(args)
        self.node_name = node_name

    def connect_node(self, node: 'Node'):
        self.connected_nodes.add(node)

    def __iter__(self):
        return iter(self.connected_nodes)

    def __str__(self):
        return f'{self.node_name} {self.id}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


class Vertex:
    def __init__(self, node1: Node, node2: Node, weight=1):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

        self.node1.connect_node(node2)
        self.node2.connect_node(node1)

    def new_pair(self, node1: Node, node2: Node):
        self.node1 = node1
        self.node2 = node2

        self.node1.connect_node(node2)
        self.node2.connect_node(node1)

    def nodes(self):
        return self.node1, self.node2

    def __eq__(self, other: 'Vertex'):
        return self.node1 == other.node1 and self.node2 == other.node2

    def __str__(self):
        return f"Vertex: {self.node1} <-- {self.weight} --> {self.node2}"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.nodes())

    def __iter__(self):
        return iter(self.nodes())


class Graph:
    def __init__(self, *args):
        self.__nodes: typing.Set[Node] = set()
        self.__vertexes: typing.Set[Vertex] = set()

        for vertex in args:
            self.add_vertex(vertex)

    def __iter__(self):
        return iter(self.__vertexes)

    def add_vertex(self, vertex: Vertex):
        for node in vertex.nodes():
            self.__nodes.add(node)
        self.__vertexes.add(vertex)

    def get_vertexes_for_node(self, node: Node):
        return [vertex for vertex in self.__vertexes if node in vertex]

    @property
    def nodes(self):
        return self.__nodes

    @property
    def vertexes(self):
        return self.__vertexes


if __name__ == "__main__":
    n1 = Node("Москва", node_name="Город")
    n2 = Node("Сургут", node_name="Город")
    n3 = Node("Новосибирск", node_name="Город")
    n4 = Node("Тверь", node_name="Город")
    n5 = Node("Рязань", node_name="Город")
    n6 = Node("Воронеж", node_name="Город")

    vertex1 = Vertex(n1, n2, weight=3000)
    vertex2 = Vertex(n2, n3, weight=1500)
    vertex3 = Vertex(n1, n4, weight=200)
    vertex4 = Vertex(n1, n5, weight=300)
    vertex5 = Vertex(n1, n6, weight=500)

    graph = Graph(vertex1, vertex2, vertex3, vertex4, vertex5)
    #graph.add_vertex(vertex1)
    #graph.add_vertex(vertex2)

    print("Graph")
    for v in graph.vertexes:
        print(v)

    for n in graph.nodes:
        print(n.id, n.connected_nodes)

    print(graph.get_vertexes_for_node(n2))

