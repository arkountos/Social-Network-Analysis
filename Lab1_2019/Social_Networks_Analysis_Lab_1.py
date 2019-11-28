import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


n = 110

G = nx.watts_strogatz_graph(n, 4, 0)
pos_fr = nx.fruchterman_reingold_layout(G)
# nx.draw(G, pos=pos_fr, with_labels="True", node_size=300)
nx.draw_circular(G, node_size=300)
plt.show()
