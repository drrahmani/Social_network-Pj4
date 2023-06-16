import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist('com-friendster.top5000.cmty.txt')

path_lengths = dict(nx.all_pairs_shortest_path_length(G))
length_distribution = {}

for source, paths in path_lengths.items():
    for target, length in paths.items():
        if length in length_distribution:
            length_distribution[length] += 1
        else:
            length_distribution[length] = 1

plt.bar(length_distribution.keys(), length_distribution.values())
plt.xlabel('Path Length')
plt.ylabel('Frequency')
plt.title('Path Length Distribution')
plt.show()