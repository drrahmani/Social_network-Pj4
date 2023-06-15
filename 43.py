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

k_cores = nx.core_number(graph)

core_sizes = list(k_cores.values())
core_size_counts = {core_size: core_sizes.count(core_size) for core_size in set(core_sizes)}

sorted_core_sizes = sorted(core_size_counts.keys())

plt.bar(sorted_core_sizes, [core_size_counts[core_size] for core_size in sorted_core_sizes])
plt.xlabel('K-Core Size')
plt.ylabel('Frequency')
plt.title('K-Core Size Distribution')
plt.show()
