class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    def __init__(self, v1: Vertex, v2: Vertex, dist=1):
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

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

    def is_link_in_list(self, link: Link):
        for inner_link in self._links:
            if inner_link == link:
                return True
        return False

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        if not self.is_link_in_list(link):
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def find_path(self, start_v: Vertex, stop_v: Vertex):
        pass


if __name__ == '__main__':
    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    map = LinkedGraph()
    map.add_link(Link(v1, v2))
    map.add_link(Link(v2, v3))
    map.add_link(Link(v1, v3))
    map.add_link(Link(v3, v2))

