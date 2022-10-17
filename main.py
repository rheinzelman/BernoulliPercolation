import igraph as ig
import matplotlib.pyplot as plt
import generate

p = .8

x_size = 30
y_size = 30
n_vertices = x_size * y_size

g = ig.Graph(n_vertices)

generate.draw_graph(x_size,y_size, p, g)

clusters = g.connected_components()

i = g.community_infomap()
pal = ig.drawing.colors.ClusterColoringPalette(len(i))
g.vs['color'] = pal.get_many(i.membership)


fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    g,
    target=ax,
    layout="grid", # print nodes in a circular layout
    vertex_size=1,
    vertex_shape='rectangle',
    vertex_frame_width=4.0,
    vertex_frame_color="white",
    vertex_label_size=7.0,
)

plt.show()