from graph import *

my_graph = Graph()
a_vertex = Vertex("A")
b_vertex = Vertex("B")
c_vertex = Vertex("C")
d_vertex = Vertex("D")
e_vertex = Vertex("E")
f_vertex = Vertex("F")

my_graph.add_vertex(a_vertex)
my_graph.add_vertex(b_vertex)
my_graph.add_vertex(c_vertex)
my_graph.add_vertex(d_vertex)
my_graph.add_vertex(e_vertex)
my_graph.add_vertex(f_vertex)

my_graph.add_directed_edge(a_vertex, f_vertex, 9.0)
my_graph.add_directed_edge(a_vertex, b_vertex, 2.0)
my_graph.add_directed_edge(b_vertex, f_vertex, 6.0)   # assume B to F only
my_graph.add_directed_edge(b_vertex, d_vertex, 15.0)
my_graph.add_directed_edge(b_vertex, c_vertex, 8.0)
my_graph.add_directed_edge(f_vertex, e_vertex, 3.0)
my_graph.add_directed_edge(c_vertex, d_vertex, 1.0)
my_graph.add_directed_edge(e_vertex, c_vertex, 7.0)
my_graph.add_directed_edge(e_vertex, d_vertex, 3.0)

print("the weight: ", my_graph.get_weight(a_vertex, f_vertex))

print()




print("starting BFS with vertex A")
for vertex in my_graph.breadth_first_search(a_vertex):
    print(vertex.label, end = "")
print()





# A -> B[label="2.0",weight="2.0"];
# A -> F[label="9.0",weight="9.0"];
# B -> C[label="8.0",weight="8.0"];
# B -> D[label="15.0",weight="15.0"];
# B -> F[label="6.0",weight="6.0"];
# C -> D[label="1.0",weight="1.0"];
# E -> C[label="7.0",weight="7.0"];
# E -> D[label="3.0",weight="3.0"];
# F -> B[label="6.0",weight="6.0"]; F -> E[label="3.0",weight="3.0"];