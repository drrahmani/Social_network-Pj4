import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('com-friendster.all.cmty.txt')

clustering_coefficients = nx.clustering(G)

clustering_distribution = {}

for cc in clustering_coefficients.values():
    if cc in clustering_distribution:
        clustering_distribution[cc] += 1
    else:
        clustering_distribution[cc] = 1

plt.bar(clustering_distribution.keys(), clustering_distribution.values())
plt.xlabel('WCC Size Distribution')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Distribution')
plt.show()