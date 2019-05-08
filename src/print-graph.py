import networkx as nx
import matplotlib.pyplot as plt

G=nx.path_graph(7)

print("Nodes of graph: ")
print(G.nodes())
print("Edges of graph: ")
print(G.edges())
nx.draw(G, with_labels=True)
plt.show()