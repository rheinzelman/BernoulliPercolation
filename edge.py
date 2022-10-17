import random

def draw_edge(start, end, p, g):
    probability = random.uniform(0, 1)

    if(probability < p):
        g.add_edges([(start, end)])
