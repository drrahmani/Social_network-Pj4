import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_edgelist ('com-friendster.top5000.cmty.txt')

average_neighbour_degrees = {}

for node in G.nodes ():
    neighbours = G.neighbors (node)
    neighbour_degrees = [G.degree (neighbour) for neighbour in neighbours]

    if len (neighbour_degrees) > 0:
        avg_neighbour_degree = sum (neighbour_degrees) / len (neighbour_degrees)
        average_neighbour_degrees[node] = avg_neighbour_degree

avg_neighbour_degree_distribution = {}

for avg_neighbour_degree in average_neighbour_degrees.values ():
    if avg_neighbour_degree in avg_neighbour_degree_distribution:
        avg_neighbour_degree_distribution[avg_neighbour_degree] += 1
    else:
        avg_neighbour_degree_distribution[avg_neighbour_degree] = 1

plt.bar (avg_neighbour_degree_distribution.keys (), avg_neighbour_degree_distribution.values ())
plt.xlabel ('Average Neighbour Degree')
plt.ylabel ('Number Of Node')
plt.title ('Average Neighbour Degree Distribution')
plt.show ()