import igraph as ig

import edge


def draw_graph(x_size, y_size, p, g):
     for i in range(x_size * y_size):
        # bottom left
        if(i == 0):
            edge.draw_edge(i,i+x_size,p,g)
        # bottom right
        elif(i == x_size-1):
            edge.draw_edge(i,i+x_size,p,g)
        # top left
        elif(i == x_size*y_size - x_size):
            edge.draw_edge(i,i+1,p,g)
        # top right
        elif(i == x_size*y_size - 1):
            pass
        # bottom row
        elif (i < x_size and i != 0 and i != x_size - 1):
            if (not g.are_connected(i, i - 1)):
                edge.draw_edge(i,i-1,p,g)
            elif (not g.are_connected(i, i + 1)):
                edge.draw_edge(i, i+1, p, g)
            elif (not g.are_connected(i, i + x_size)):
                edge.draw_edge(i, i+x_size, p, g)
        # left col
        elif (i % x_size == 0 and i != 0 and i != x_size * y_size - x_size):
            if(not g.are_connected(i, i+x_size)):
                edge.draw_edge(i,i+x_size,p,g)
            elif(not g.are_connected(i, i-x_size)):
                edge.draw_edge(i,i-x_size,p,g)
        # right col
        elif(i % x_size == x_size-1):
            if (not g.are_connected(i, i + x_size)):
                edge.draw_edge(i,i+x_size,p,g)
            elif (not g.are_connected(i, i - x_size)):
                edge.draw_edge(i,i-x_size,p,g)
        # top row
        elif(i < x_size*y_size and i > x_size*y_size-x_size):
            if (not g.are_connected(i, i - 1)):
                edge.draw_edge(i, i - 1,p,g)
            elif (not g.are_connected(i, i + 1)):
                edge.draw_edge(i,i+1,p,g)
            elif (not g.are_connected(i, i - x_size)):
                edge.draw_edge(i,i+x_size,p,g)
        else:
            if(not g.are_connected(i,i+1)):
                edge.draw_edge(i,i+1, p, g)
            if(not g.are_connected(i,i-1)):
                edge.draw_edge(i,i-1, p, g)
            if(not g.are_connected(i,i+x_size)):
                edge.draw_edge(i,i+x_size, p, g)
            if(not g.are_connected(i,i-x_size)):
                edge.draw_edge(i,i-x_size, p, g)
