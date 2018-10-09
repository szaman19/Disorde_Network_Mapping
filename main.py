from __future__ import division

import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def generate_graph(file_name):
    data = open(file_name)
    
    temp_lst = []
    graph = nx.Graph()
    for line in data:
        #Clean up the data to get the numerical values
        data_points = line.strip().split()
        data_points = " ".join(data_points).split()
        #data_points currently hold [from_site_index, to_site_index, correlation_val]
        site_i = int(data_points[0])
        site_j = int(data_points[1])
        if (site_i != site_j):
            corr = np.reciprocal(float(data_points[2]))
        else:
            corr = 0
        #Regular division is not helpful in this situation. Make sure to not add when i = j, because corr == inf

        if(site_i != site_j and site_i < 11 and site_j < 11):
            #print(site_i, site_j, corr)
            graph.add_edge(site_i,site_j, weight = corr)
        
    #adj_matrix = nx.adjacency_matrix(graph)
    #print(np.matrix(adj_matrix))
    return graph

def main():
    cwd = os.getcwd()
    #Pe-1D-Ns100-Aij-disW-0.txt

    file_name = cwd+'/data/Pe-1D-Ns100-Aij-disW-0.txt'
    graph =  generate_graph(file_name)
    #nx.draw(graph, with_labels=True)
    #plt.show()
    print(graph.number_of_nodes())
    print(graph.number_of_edges())
    print(nx.single_source_dijkstra_path(graph,1))
    print(nx.single_source_dijkstra_path_length(graph,1))
    all_path_lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    average_path = []
    j = 1
    i = 1
    steps = 0
    while (steps < 11):
        i = 1
        j = 1 +steps
        while(j < 11):
            print(i,j)
            i += 1
            j += 1

        steps +=1

main()
