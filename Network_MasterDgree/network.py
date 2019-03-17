import networkx as nx
import matplotlib.pyplot as plt

G = nx.erdos_renyi_graph(5, 1)
nx.draw(G)
plt.show()

degdist = nx.degree_histogram(G)
plt.plot(degdist, 'o')
G = nx.barabasi_albert_graph(100, 5)
plt.clf()
nx.draw_spectral(G)