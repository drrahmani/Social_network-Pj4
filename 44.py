import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_edgelist ('com-friendster.all.cmty.txt')

average_friends_of_friends = {}

for node in G.nodes ():
    friends = set (G.neighbors (node))
    friends_of_friends = set ()

    for friend in friends:
        friends_of_friends.update (G.neighbors (friend))

    friends_of_friends.discard (node)

    if len (friends_of_friends) > 0:
        avg_friends_of_friends = len (friends_of_friends) / len (friends_of_friends)
        average_friends_of_friends[node] = avg_friends_of_friends

avg_fof_distribution = {}

for avg_fof in average_friends_of_friends.values ():
    if avg_fof in avg_fof_distribution:
        avg_fof_distribution[avg_fof] += 1
    else:
        avg_fof_distribution[avg_fof] = 1

plt.bar (avg_fof_distribution.keys (), avg_fof_distribution.values ())
plt.xlabel ('Average Friends-of-Friends')
plt.ylabel ('Number Of Node')
plt.title ('Average Friends-of-Friends Distribution')
plt.show ()