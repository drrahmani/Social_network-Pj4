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

avg_neighbour_degree = {}
for node in graph.nodes():
    neighbours = list(graph.neighbors(node))
    neighbour_degrees = [graph.degree(neighbour) for neighbour in neighbours]
    avg_neighbour_degree[node] = sum(neighbour_degrees) / len(neighbour_degrees) if len(neighbour_degrees) > 0 else 0

avg_neighbour_degree_values = list(avg_neighbour_degree.values())
avg_neighbour_degree_counts = {value: avg_neighbour_degree_values.count(value) for value in set(avg_neighbour_degree_values)}

sorted_avg_neighbour_degree = sorted(avg_neighbour_degree_counts.keys())

plt.bar(sorted_avg_neighbour_degree, [avg_neighbour_degree_counts[value] for value in sorted_avg_neighbour_degree])
plt.xlabel('Average Neighbour Degree')
plt.ylabel('Frequency')
plt.title('Average Neighbour Degree Distribution')
plt.show()