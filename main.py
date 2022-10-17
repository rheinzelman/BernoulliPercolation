import igraph as ig
import matplotlib.pyplot as plt
import generate

p = .1

x_size = 10
y_size = 10
n_vertices = x_size * y_size

g = ig.Graph(n_vertices)

generate.draw_graph(x_size,y_size, p, g)

fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    g,
    target=ax,
    layout="grid", # print nodes in a circular layout
    vertex_size=0.1,
    vertex_frame_width=4.0,
    vertex_frame_color="white",
    vertex_label_size=7.0,
)

plt.show()