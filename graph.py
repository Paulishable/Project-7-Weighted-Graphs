import sys
from queue import  *

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

    def __str__(self):
        return self.adjacency_list[0][0]

    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        print(self.adjacency_list[new_vertex])

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


    def breadth_first_search(graph, start_vertex):
        """Breadth-first search function"""
        distances = dict()
        discovered_set = set()
        frontier_queue = Queue()
        visited_list = []

        # start_vertex has a distance of 0 from itself
        distances[start_vertex] = 0

        frontier_queue.enqueue(start_vertex)  # Enqueue start_vertex in frontier_queue
        discovered_set.add(start_vertex)  # Add start_vertex to discovered_set

        while frontier_queue.list.head is not None:
            current_vertex = frontier_queue.dequeue()
            visited_list.append(current_vertex)
            for adjacent_vertex in graph.adjacency_list[current_vertex]:
                if adjacent_vertex not in discovered_set:
                    frontier_queue.enqueue(adjacent_vertex)
                    discovered_set.add(adjacent_vertex)

                    # Distance of adjacent_vertex is 1 more than current_vertex
                    distances[adjacent_vertex] = distances[current_vertex] + 1

        return visited_list


    def depth_first_search(graph, start_vertex, visit_function):
        """ Depth-first search function """
        vertex_stack = [start_vertex]
        visited_set = set()

        while len(vertex_stack) > 0:
            current_vertex = vertex_stack.pop()
            if current_vertex not in visited_set:
                visit_function(current_vertex)
                visited_set.add(current_vertex)
                for adjacent_vertex in graph.adjacency_list[current_vertex]:
                    vertex_stack.append(adjacent_vertex)


