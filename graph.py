import sys

if __name__ == '__main__':
    if len(sys.argv) != 1:
        Hello = str(sys.argv[1])
        print(Hello)


class Vertex:
    def __init__(self, label):
        if not isinstance(label, str):
            raise ValueError("Label is not a string")
        self.label = label


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight=1.0):
        """needed for assignment - assume the edge is not directed """
        if not isinstance(from_vertex, Vertex):
            raise ValueError("Label is not a Vertex")
        if not isinstance(to_vertex, Vertex):
            raise ValueError("Label is not a Vertex")
        if not isinstance(weight, float):
            raise ValueError("Label is not a float")

        self.add_undirected_edge(from_vertex, to_vertex, weight)

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        """add an edge but it is directed"""
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        """add an edge that is undirected"""
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def get_weight(self, from_vertex, to_vertex):
        """return the weight for an edge"""
        # -----------add checks for  validity here-------

        return self.edge_weights[(from_vertex, to_vertex)]
