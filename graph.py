import sys
from queue import *
import math


def main():
    pass


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
        string = "digraph G {\n"
        for item in self.adjacency_list:
            for subitem in self.adjacency_list[item]:

                weight = self.get_weight(item.label, subitem.label)

                string += f"{item.label}  ->  {subitem.label}[label=\"{weight}\",weight=\"{weight}\"]\n"

        string += "}"

        return string

    def get_vertex(self, vertex_label):
        """get the vertex in the graph that matched the label"""
        for item in self.adjacency_list:
            if item.label == vertex_label:
                return item
            for subitem in self.adjacency_list[item]:
                if subitem.label == vertex_label:
                    return subitem
        return None

    def edge_does_not_exist(self, from_vertex_label, to_vertex_label):
        """get the vertex in the graph that matched the label"""
        for item in self.adjacency_list:
            if item.label == from_vertex_label:
                for subitem in self.adjacency_list[item]:
                    if subitem.label == to_vertex_label:
                        print("here in tester-from", item.label)
                        print("here in tester-to", subitem.label)
                        return False
        return True

    def add_vertex(self, new_vertex_label):
        """take a label, make it into a Vertex and save it"""

        self.adjacency_list[Vertex(new_vertex_label)] = []
        return self

    def add_edge(self, from_vertex_label, to_vertex_label, weight=1.0):
        """needed for assignment - assume the edge is not directed """
        if not isinstance(from_vertex_label, str):
            raise ValueError("Label is not a Vertex")
        if not isinstance(to_vertex_label, str):
            raise ValueError("Label is not a Vertex")
        if not isinstance(weight, float):
            raise ValueError("Label is not a float")

        from_vertex = self.get_vertex(from_vertex_label)
        to_vertex = self.get_vertex(to_vertex_label)
        if from_vertex is None or to_vertex is None:
            raise ValueError("Not a vertex in the graph")

        self.edge_weights[(from_vertex_label, to_vertex_label)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
        return self

    def add_directed_edge(self, from_vertex_label, to_vertex_label, weight=1.0):
        """add an edge but it is directed"""

        from_vertex = self.get_vertex(from_vertex_label)
        to_vertex = self.get_vertex(to_vertex_label)

        self.edge_weights[(from_vertex_label, to_vertex_label)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
        return self

    def add_undirected_edge(self, vertex_a_label, vertex_b_label, weight=1.0):
        """add an edge that is undirected"""
        vertex_a = self.get_vertex(vertex_a_label)
        vertex_b = self.get_vertex(vertex_b_label)

        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
        return self

    def get_weight(self, from_vertex_label, to_vertex_label):
        """return the weight for an edge"""
        print("----------GETTING WEIGHT-----------", from_vertex_label, to_vertex_label)

        if not isinstance(from_vertex_label, str):
            raise ValueError("Label is not a string")
        if not isinstance(to_vertex_label, str):
            raise ValueError("Label is not a string")

        from_vertex = self.get_vertex(from_vertex_label)
        to_vertex = self.get_vertex(to_vertex_label)
        if from_vertex is None or to_vertex is None:
            raise ValueError("This vertex is not in the graph")

        if self.edge_does_not_exist(from_vertex_label, to_vertex_label):
            print("edge doesn't  exist")
            return math.inf

        return float(self.edge_weights[(from_vertex_label, to_vertex_label)])

    def bfs(self, start_vertex_label):
        """Breadth-first search function"""
        start_vertex = self.get_vertex(start_vertex_label)

        if not isinstance(start_vertex, Vertex):
            raise ValueError("Label is not a Vertex")

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
            visited_list.append(current_vertex.label)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in discovered_set:
                    frontier_queue.enqueue(adjacent_vertex)
                    discovered_set.add(adjacent_vertex)

                    # Distance of adjacent_vertex is 1 more than current_vertex
                    distances[adjacent_vertex] = distances[current_vertex] + 1

        return visited_list

    def dfs(self, start_vertex_label):
        """ Depth-first search function """
        start_vertex = self.get_vertex(start_vertex_label)

        if not isinstance(start_vertex, Vertex):
            raise ValueError("Label is not a Vertex")

        the_DFS_list = []

        vertex_stack = [start_vertex]
        visited_set = set()

        while len(vertex_stack) > 0:
            current_vertex = vertex_stack.pop()
            if current_vertex not in visited_set:
                the_DFS_list.append(current_vertex.label)
                visited_set.add(current_vertex)
                for adjacent_vertex in self.adjacency_list[current_vertex]:
                    vertex_stack.append(adjacent_vertex)

        return the_DFS_list
