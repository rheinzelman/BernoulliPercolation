import igraph as ig
import matplotlib.pyplot as plt

x_size = 10
y_size = 10
n_vertices = x_size * y_size

edges = [(0, 1), (1, 2), (1, 3)]
g = ig.Graph(n_vertices)
#g.delete_edges([(0,1)])

for i in range(x_size * y_size):
    # bottom left
    if(i == 0):
        g.add_edges([(i, i+x_size),(i,i+1)])
    # bottom right
    elif(i == x_size-1):
        g.add_edges([(i,i+x_size)])
    # top left
    elif(i == x_size*y_size - x_size):
        g.add_edges([(i,i+1)])
    # top right
    elif(i == x_size*y_size - 1):
        g.add_edges([(i,i-1)])
    # bottom row
    elif (i < x_size and i != 0 and i != x_size - 1):
        if (not g.are_connected(i, i - 1)):
            g.add_edges([(i, i - 1)])
        elif (not g.are_connected(i, i + 1)):
            g.add_edges([(i, i + 1)])
        elif (not g.are_connected(i, i + x_size)):
            g.add_edges([(i, i + x_size)])
    # left col
    elif (i % x_size == 0 and i != 0 and i != x_size * y_size - x_size):
        if(not g.are_connected(i, i+x_size)):
            g.add_edges([(i, i + x_size)])
        elif(not g.are_connected(i, i-x_size)):
            g.add_edges([(i, i - x_size)])
    # right col
    elif(i % x_size == x_size-1):
        if (not g.are_connected(i, i + x_size)):
            g.add_edges([(i, i + x_size)])
        elif (not g.are_connected(i, i - x_size)):
            g.add_edges([(i, i - x_size)])
    # top row
    elif(i < x_size*y_size and i > x_size*y_size-x_size):
        pass
    else:
        if(not g.are_connected(i,i+1)):
            g.add_edges([(i,i+1)])
        if(not g.are_connected(i,i-1)):
            g.add_edges([(i,i-1)])
        if(not g.are_connected(i,i+x_size)):
            g.add_edges([(i,i+x_size)])
        if(not g.are_connected(i,i-x_size)):
            g.add_edges([(i,i-x_size)])



    # left column
    #if(i % x_size == 0):
    #    g.add_edges([(i,i+x_size),(i,i-x_size),(i,i+1)])
# Plot in matplotlib
# Note that attributes can be set globally (e.g. vertex_size), or set individually using arrays (e.g. vertex_color)
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

# Save the graph as an image file
#fig.savefig('social_network.png')
#fig.savefig('social_network.jpg')
#fig.savefig('social_network.pdf')

# Export and import a graph as a GML file.
#g.save("social_network.gml")
#g = ig.load("social_network.gml")