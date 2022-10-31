import igraph
import numpy as np
import matplotlib.pyplot as plt
import igraph as ig
import random

def generate_adjacency_matrix(rows, cols):
    n = rows * cols
    M = np.zeros((n, n))
    for r in list(range(rows)):
        for c in list(range(cols)):
            i = r * cols + c
            # Two inner diagonals
            if c > 0: M[i - 1, i] = M[i, i - 1] = 1
            # Two outer diagonals
            if r > 0: M[i - cols, i] = M[i, i - cols] = 1
    return M

def generate_adjacency_probability(rows, cols):
    n = rows * cols
    M = np.zeros((n, n))
    for r in list(range(rows)):
        for c in list(range(cols)):
            i = r * cols + c
            # Two inner diagonals
            if c > 0: M[i - 1, i] = M[i, i - 1] = random.uniform(0, 1)
            # Two outer diagonals
            if r > 0: M[i - cols, i] = M[i, i - cols] = random.uniform(0, 1)
    return M


def adjusted_matrix(adj_matrix, prob_matrix, p):
    adjusted_adj_matrix = np.zeros((len(prob_matrix), len(prob_matrix[0])))
    for i in range(len(prob_matrix)):
        for j in range(len(prob_matrix[0])):
            if (adj_matrix[i][j] == 1):
                if (prob_matrix[i][j] < p):
                    adjusted_adj_matrix[i][j] = 1
    return adjusted_adj_matrix





#p = .1

x_size = 10
y_size = 10
vertices = x_size*y_size

adj_matrix = generate_adjacency_matrix(x_size, y_size)
prob_matrix = generate_adjacency_probability(x_size, y_size)

for p in np.arange(0,1,.05):
    adjusted_adj_matrix = adjusted_matrix(adj_matrix, prob_matrix, p)
    g = ig.Graph.Adjacency(adjusted_adj_matrix, "min")

    test = ig.VertexClustering(g)
    clusters = g.connected_components()
    pal = ig.drawing.colors.ClusterColoringPalette(len(clusters))
    g.vs['color'] = pal.get_many(clusters.membership)

    fig, ax = plt.subplots(figsize=(10, 10))
    ig.plot(
        test,
        target=ax,
        layout="grid",  # print nodes in a circular layout
        vertex_size=1,
        vertex_shape='rectangle',
        vertex_frame_width=1.0,
        vertex_frame_color="white",
        vertex_label_size=7.0,
        bbox=(1024, 1024),
        margin=10
    )
    plt.savefig("fig")
    plt.show()





