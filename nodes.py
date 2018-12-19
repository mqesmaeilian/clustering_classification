import networkx as nx
import matplotlib.pyplot as plt


g = nx.Graph()
g.add_node(1)
nx.draw_random(g)
plt.show()
