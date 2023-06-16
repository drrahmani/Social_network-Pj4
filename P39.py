#Muhammad Rahmani Pj-39-46
import networkx as nx
import matplotlib.pyplot as plt

with open('com-friendster.top5000.cmty.txt','r') as file:

    lines =  file.readline()
    edges = [line.strip().split('\t') for line in lines]
    G = nx.Graph()
    for edge in edges:
        if not edge:
            continue
            source_node =  edge[0]
            target_nodes = edge [1:]
            for target_node in target_nodes :
                G.add_edge(source_node,target_node)
                num_runs = 10
                degree_dist={}
                for _ in range(num_runs):
                    degree_sequence =  [degree for node,degree in G.degree()]
                    degree_sequence = sorted(degree_sequence,reverse=True)

                    for degree in degree_sequence :
                        if degree in degree_dist :
                            degree_dist[degree] += 1
                        else :
                            degree_dist[degree] = 1
                            total_nodes = G.number_of_nodes()
                            degree_dist_normalized = {degree: count / (num_runs * total_nodes) for degree,count in degree_dist.items()}
                            sorted_degree_dist =  sorted(degree_dist_normalized.items())
                            degree,fractions = zip(*sorted_degree_dist)


                            plt.plot(degrees , fractions,marker='0')
                            plt.xlabel('Degree')
                            plt.ylable('Number Of Node')
                            plt.title('Degree Distributaion')
                            plt.show()

