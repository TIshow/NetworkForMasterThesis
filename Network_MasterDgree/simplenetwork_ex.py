import netwrkx as nx 
import numpy as np 
import matplotlib.pyplot as plt 

G=nx.watts_strogatz_graph(100,4,0.2) 

degree_sequence=sorted(nx.degree(G).values(),reverse=True) 
print ("Degree sequence = ", degree_sequence) 
dmax=max(degree_sequence) 
dmin =min(degree_sequence) #not necessary 
kukan=range(0,dmax+2) 
hist, kukan=np.histogram(degree_sequence,kukan,normed=True) 

# drawing the degree histogram 
plt.figure() 
plt.plot(hist) 
plt.xlabel('degree') 
plt.ylabel('relative frequency') 
plt.title('degree frequency') 
plt.grid(True) 
plt.savefig('degree_hist.png') 
plt.show() 