import networkx as nx
import os
import numpy


def generate_graph(file_name, reciprocal = True):
    data = open(file_name)
    
    temp_lst = []
    graph = nx.Graph()
    label = ''
    for line in data:
        #Clean up the data to get the numerical values
        data_points = line.strip().split()
        data_points = " ".join(data_points).split()
        if (data_points[0] == 'For'):
            label = str(data_points[3])
        else:

        #data_points currently hold [from_site_index, to_site_index, correlation_val]
            site_i = int(data_points[0])
            site_j = int(data_points[1])

            if (site_i != site_j):
                if (reciprocal):
                    corr = 1/float(data_points[2])
                else:
                    corr = float(data_points[2])
            else:
                corr = 0
        #Regular division is not helpful in this situation. Make sure to not add when i = j, because corr == inf

            if(site_i != site_j):
            #print(site_i, site_j, corr)
                graph.add_edge(site_i,site_j, weight = corr)
        
    #adj_matrix = nx.adjacency_matrix(graph)
    #print(np.matrix(adj_matrix))
    return graph, label

def di_generate_graph(file_name, reciprocal = True):
    data = open(file_name)
    
    temp_lst = []
    graph = nx.DiGraph()
    label = ''
    # counter = 0
    for line in data:
        #Clean up the data to get the numerical values
        data_points = line.strip().split()
        data_points = " ".join(data_points).split()
        if (data_points[0] == 'For'):
            label = str(data_points[3])
        else:

        #data_points currently hold [from_site_index, to_site_index, correlation_val]
            site_i = int(data_points[0])
            site_j = int(data_points[1])

            if (site_i != site_j):
                if (reciprocal):
                    corr = 1/float(data_points[2])
                else:
                    corr = float(data_points[2])
            else:
                corr = 0
        #Regular division is not helpful in this situation. Make sure to not add when i = j, because corr == inf

            if(site_i != site_j and (site_j % 10) ==0 and (site_i % 10) ==0):
            #print(site_i, site_j, corr)
                graph.add_edge(site_i,site_j, weight = corr)
                graph.add_edge(site_j,site_i, weight = corr)
            # counter +=1

        
    #adj_matrix = nx.adjacency_matrix(graph)
    #print(np.matrix(adj_matrix))
    return graph, label

