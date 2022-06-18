from graph import *

my_graph = Graph()
v1 = Vertex("first vertex")
v2 = Vertex("second vertex")

my_graph.add_vertex(v1)
my_graph.add_vertex(v2)

my_graph.add_edge(v1, v2, 23.4)

print("the weight: ", my_graph.get_weight(v1, v2))
