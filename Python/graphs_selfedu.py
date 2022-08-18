def print_dict(toprint):
    for key, value in toprint.items():
        print(f'{key}: {value}')


def path_on_graph(graph, start_node, end_node):
    nodes_weights = {}
    closest_nodes = {}

    for key in graph.vertex:
        nodes_weights[key] = None
        closest_nodes[key] = start_node
    nodes_weights[start_node] = 0

    next_nodes = [start_node]
    seen_nodes = set()

    while next_nodes:
        current_node = next_nodes.pop()
        for n in current_node:
            if n not in seen_nodes:
                new_weight = nodes_weights[current_node] + graph.get_link_by_2vertex(current_node, n)
                if nodes_weights[n] is None or new_weight < nodes_weights[n]:
                    nodes_weights[n] = new_weight
                    closest_nodes[n] = current_node
                next_nodes.append(n)
        seen_nodes.add(current_node)

    if nodes_weights[end_node]:
        path = [end_node]
        #current_node = closest_nodes[end_node]
        for i in range(len(closest_nodes)-1):
            if closest_nodes[path[i]] == start_node:
                path.append(start_node)
                path.reverse()
                return path
            path.append(closest_nodes[path[i]])

    return None

    #print_dict(nodes_weights)
    #print_dict(closest_nodes)


class Vertex:
    id = 0

    def __init__(self):
        self._links = []
        Vertex.id += 1
        self.id = Vertex.id

    def __iter__(self):
        return iter(self._links)

    def __repr__(self):
        return f'Vertex {self.id}'

    def __str__(self):
        return f'Vertex {self.id}'

    @property
    def links(self):
        return self._links


class Link:
    id = 0

    def __init__(self, v1: Vertex, v2: Vertex, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

        v1.links.append(v2)
        v2.links.append(v1)

    def __eq__(self, other):
        return any([self._v1 == other._v1 and self._v2 == other._v2,
                    self._v1 == other._v2 and self._v2 == other._v1])

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value


class LinkedGraph:
    def __init__(self):
        self._links = [] # Возможно стоит сделать set
        self._vertex = []

    @property
    def vertex(self):
        return self._vertex

    def is_link_in_list(self, link: Link):
        for inner_link in self._links:
            if inner_link == link:
                return True
        return False

    def get_link_by_2vertex(self, v1: Vertex, v2: Vertex):
        for link in self._links:
            if link.v1 in (v1, v2) and link.v2 in (v1, v2):
                return link.dist

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        if not self.is_link_in_list(link):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def find_path(self, start_v: Vertex, stop_v: Vertex):
        return path_on_graph(self, start_v, stop_v)


if __name__ == '__main__':
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    map = LinkedGraph()
    map.add_link(Link(v1, v2))
    map.add_link(Link(v2, v3))
    #map.add_link(Link(v1, v3))
    map.add_link(Link(v3, v2))
    map.add_link(Link(v3, v4))
    map.add_vertex(v5)

    print(map.find_path(v4, v2))





