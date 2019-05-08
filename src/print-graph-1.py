import networkx as nx
import matplotlib.pyplot as plt


G = nx.cubical_graph()
nx.draw(G) # default spring_layout
nx.draw(G, pos=nx.spectral_layout(G), nodecolor='r', edge_color='b')
plt.show()
#input("Press Any key")
nx.draw(G, pos=nx.circular_layout(G), nodecolor='r', edge_color='b')
plt.show()
#input("Press Any key")
nx.draw(G, pos=nx.random_layout(G), nodecolor='r', edge_color='b')
plt.show()
