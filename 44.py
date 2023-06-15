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

avg_friends_of_friends = {}
for node in graph.nodes():
    friends = set(graph.neighbors(node))
    friends_of_friends = set()
    for friend in friends:
        friends_of_friends.update(graph.neighbors(friend))
    friends_of_friends -= friends
    avg_friends_of_friends[node] = len(friends_of_friends) / len(friends) if len(friends) > 0 else 0

avg_friends_of_friends_values = list(avg_friends_of_friends.values())
avg_friends_of_friends_counts = {value: avg_friends_of_friends_values.count(value) for value in set(avg_friends_of_friends_values)}

sorted_avg_friends_of_friends = sorted(avg_friends_of_friends_counts.keys())

plt.bar(sorted_avg_friends_of_friends, [avg_friends_of_friends_counts[value] for value in sorted_avg_friends_of_friends])
plt.xlabel('Average Friends-of-Friends')
plt.ylabel('Frequency')
plt.title('Average Friends-of-Friends Distribution')
plt.show()
