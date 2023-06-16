import  networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('com-friendster.top5000.cmty.txt')

wccs = list(nx.weakly_connected_components(G))
wcc_sizes = [len(wcc) for wcc in wccs]

wcc_size_distribution = {}

for size in wcc_sizes:
    if size in wcc_size_distribution:
        wcc_size_distribution[size] += 1
    else:
        wcc_size_distribution[size] = 1

plt.bar(wcc_size_distribution.keys(), wcc_size_distribution.values())
plt.xlabel('WCC Size')
plt.ylabel('WCC Frequency ')
plt.title('WCC Size Distribution')
plt.show()