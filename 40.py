import urllib.request
import gzip
import networkx as nx
import matplotlib.pyplot as plt

url = "https://snap.stanford.edu/data/bigdata/communities/com-friendster.ungraph.txt.gz"
dataset_path = "com-friendster.ungraph.txt.gz"

urllib.request.urlretrieve(url, dataset_path)

with gzip.open(dataset_path, "rb") as file_in:
    with open("com-friendster.ungraph.txt", "wb") as file_out:
        file_out.write(file_in.read())

graph = nx.read_edgelist("com-friendster.ungraph.txt")


print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())


path_lengths = dict(nx.all_pairs_shortest_path_length(graph))

all_lengths = [length for source_lengths in path_lengths.values() for length in source_lengths.values()]

plt.hist(all_lengths, bins=30, edgecolor='black')
plt.xlabel('Path Length')
plt.ylabel('Frequency')
plt.title('Path Length Distribution')
plt.show()