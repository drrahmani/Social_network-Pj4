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

clustering_coefficients = nx.clustering(graph)

plt.hist(list(clustering_coefficients.values()), bins=30, edgecolor='black')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Distribution')
plt.show()
