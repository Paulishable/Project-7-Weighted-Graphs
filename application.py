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
out = str(my_graph)
print(out)

print("Starting BFS with Vertex A")
for vertex_label in my_graph.bfs("A"):
    print(vertex_label, end="")
print()

print("Starting DFS with Vertex A")
for vertex_label in my_graph.dfs("A"):
    print(vertex_label, end="")
print()

print("get weight:", my_graph.get_weight("B", "A"))




