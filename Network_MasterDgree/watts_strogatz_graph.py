import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.watts_strogatz_graph(100, 4, 0.2)
plt.figure(1)
nx.draw_random(G)
plt.show()

degree_sequence=sorted(nx.degree(G).values(), reverse=True)
dmax = max(degree_sequence)
kukan = range(0, dmax+4)
hist, kukan=np.histogram(degree_sequence, kukan, normed=True)
plt.figure(2)
plt.plot(hist)
plt.xlabel('degree')
plt.ylabel('frequency')
plt.title('degree frequency(Watts Strogatz small world network : n = 100, 4,  0.2)')
plt.grid(True)
plt.show()