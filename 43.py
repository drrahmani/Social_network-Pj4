import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('com-friendster.top5000.cmty.txt')

k_core_sizes = nx.core_number(G).values()
k_core_size_distribution = {}

for size in k_core_sizes:
    if size in k_core_size_distribution:
        k_core_size_distribution[size] += 1
    else:
        k_core_size_distribution[size] = 1

plt.bar(k_core_size_distribution.keys(), k_core_size_distribution.values())
plt.xlabel('K-Core Size')
plt.ylabel('Number Of Node')
plt.title('K-Core Size Distribution')
plt.show()