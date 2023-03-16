# Алгоритм Прима поиска минимального остова графа
import collections
import math

from graph import Graph, Vertex, Node

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


def prima(graph: Graph, base_node: Node) -> Graph:
    ostov = Graph()

    nodes_to_check = {base_node}

    temp = base_node
    for node in nodes_to_check:
        min_vertex = min(graph.vertexes(), key=lambda v: v.weight if \
        (v.node1 not in nodes_to_check and v.node2 not in nodes_to_check) else None, default=None)

        if min_vertex is None:
            pass

    return ostov


if __name__ == "__main__":
    min_vertex = min(graph.get_vertexes_for_node(n1), key=lambda v: v.weight)
    print(min_vertex)
    #nt = collections.namedtuple("Point", ["x", "y", "z"])(x=1, z=2, y=3)
    #print(nt.x)
