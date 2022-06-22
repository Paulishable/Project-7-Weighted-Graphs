import operator
from graph import Graph, Vertex


def dijkstra_shortest_path(g, start_vertex_label):
    start_vertex = g.get_vertex(start_vertex_label)
    # Put all vertices in an unvisited queue.
    unvisited_queue = []
    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex.label, adj_vertex.label)]
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex


def get_shortest_path(start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
    path = ''
    current_vertex = end_vertex
    while current_vertex is not start_vertex:
        path = ' -> ' + str(current_vertex.label) + path
        current_vertex = current_vertex.pred_vertex
    path = start_vertex.label + path
    return path


# Program to find shortest paths from vertex A.
g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")
g.add_vertex("G")

g.add_undirected_edge("A", "B", 8)
g.add_undirected_edge("A", "C", 7)
g.add_undirected_edge("A", "D", 3)
g.add_undirected_edge("B", "E", 6)
g.add_undirected_edge("C", "D", 1)
g.add_undirected_edge("C", "E", 2)
g.add_undirected_edge("D", "F", 15)
g.add_undirected_edge("D", "G", 12)
g.add_undirected_edge("E", "F", 4)
g.add_undirected_edge("F", "G", 1)


def dict_dsp_all(source):
    # Sort the vertices by the label for convenience; display shortest path for each vertex
    # from vertex.label = source
    for v in sorted(g.adjacency_list, key=operator.attrgetter("label")):
        if v.pred_vertex is None and v is not g.get_vertex(source):
            print("A to %s: no path exists" % v.label)
        else:
            print("A to %s: %s (total weight: %g)" % (v.label, get_shortest_path(g.get_vertex(source), v), v.distance))

# Run Dijkstra's algorithm first.
dijkstra_shortest_path(g, "A")

dict_dsp_all("A")
