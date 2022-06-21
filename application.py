from graph import *

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")
my_graph.add_vertex("F")

my_graph.add_directed_edge("A", "B", 2.0)
my_graph.add_directed_edge("A", "F", 9.0)
my_graph.add_directed_edge("B", "F", 6.0)
my_graph.add_directed_edge("B", "D", 15.0)
my_graph.add_directed_edge("B", "C", 8.0)
my_graph.add_directed_edge("C", "D", 1.0)
my_graph.add_directed_edge("E", "C", 7.0)
my_graph.add_directed_edge("E", "D", 3.0)
my_graph.add_directed_edge("F", "B", 3.0)
my_graph.add_directed_edge("F", "E", 3.0)

print()
# out = str(my_graph)
# print(out)

# print("Starting BFS with Vertex A")
# for vertex_label in my_graph.bfs("A"):
#     print(vertex_label, end="")
# print()
#
# print("Starting DFS with Vertex A")
# for vertex_label in my_graph.dfs("A"):
#     print(vertex_label, end="")
# print()
#
# print("get weight:", my_graph.get_weight("B", "A"))

g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edge("A", "B", 1.0)
g.add_edge("A", "C", 1.0)

g.add_edge("B", "D", 1.0)

g.add_edge("C", "E", 1.0)

g.add_edge("E", "F", 1.0)

output = str(g)
print(output)


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



# Run Dijkstra's algorithm first.
# g.dijkstra_shortest_path("A")

print(g.dsp("A", "E"))
# g.dict_dsp_all("A")