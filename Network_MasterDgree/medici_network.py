import matplotlib.pyplot as plt
import networkx as nx

#initial task
G = nx.Graph()
nod = range(0,15)
e = [(3,5), (4,5), (5, 10), (5, 11), (5, 13), (5, 6)] #list of edge
G.add_nodes_from(nod) #add nod nodes
G = nx.Graph(e) #create e graph
e1=[(0,1),(0,2), (0,4),(1,4), (1,7),(1,2), (2,3),(3,6),(11,12), (13,14),(6,8),(8,13), (8,9),(13,14)]
G.add_edges_from(e1) #add e1 edges



pos = nx.spring_layout(G) #position for all nodes

#draw nodes of G
nx.draw_networkx_nodes(G, pos, 
                        nodelist=[0,1,2,4,7,8,9,10,12,14],
                        node_color='b',
                        node_size=15,
                        alpha=0.8)
nx.draw_networkx_nodes(G,pos,
                       nodelist=[3,4,5,6,10,11,13],
                       node_color='r',
                       node_size=15,
                       alpha=0.8)

#draw edges of G
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos, edgelist=e, width=1.0, alpha=0.5, edge_color='r')
nx.draw_networkx_edges(G, pos, edgelist=e1, width=1.0, alpha=0.5, edege_color='b')

#math labels
labels={}
labels[0]= 'Castellan'
labels[1]='Peruzzi'
labels[2]='Strozzi'
labels[3]='Ridolfi'
labels[4]='Barbadori'
labels[5]='Medici'
labels[6]='Tornabuorn'
labels[7]='Bischeri'
labels[8]='Guadagni'
labels[9]='Lambertertes'
labels[10]= 'Acciaiuol'
labels[11]='Salviati'
labels[12]='Pazzi'
labels[13]='Albizzi'
labels[14]='Ginori'

#computing the mesures of network
print('the clustering coefficient for nodes = ',nx.clustering(G))
print('degeree sequence = ',G.degree().values())
print('degree histogram = ', nx.degree_histogram(G))
print('degree centrality = ',nx.degree_centrality(G))
print('betweenness centrality = ', nx.betweenness_centrality(G))

#nx.draw_spring(G)
nx.draw_networkx_labels(G,pos,labels,font_size=12)

plt.axis('off')
plt.title('Fifteen-century Florentine marriages network')    

plt.savefig("medici.png") # save as png
plt.show() 


