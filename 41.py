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


# problem 41 :
# 41 WCC size distribution
# Find the weakly connected components
wcc_sizes = [len(wcc) for wcc in nx.weakly_connected_components(graph)]

# Plot the WCC size distribution
plt.hist(wcc_sizes, bins=30, edgecolor='black')
plt.xlabel('WCC Size')
plt.ylabel('Frequency')
plt.title('WCC Size Distribution')
plt.show()
