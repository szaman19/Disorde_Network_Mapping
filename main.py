from __future__ import division

import os
import networkx as nx
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def generate_graph(file_name):
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
                corr = np.reciprocal(float(data_points[2]))
            else:
                corr = 0
        #Regular division is not helpful in this situation. Make sure to not add when i = j, because corr == inf

            if(site_i != site_j):
            #print(site_i, site_j, corr)
                graph.add_edge(site_i,site_j, weight = corr)
        
    #adj_matrix = nx.adjacency_matrix(graph)
    #print(np.matrix(adj_matrix))
    return graph, label

def average_path_generator(graph,label,data_file):
    all_path_lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    average_path = []
    j = 1
    i = 1
    steps = 0
    while (steps < 501):
        i = 1
        j = 1 +steps
        counter = 0
        total_length = 0
        while(j < 501):
            total_length += all_path_lengths[i][j]
            counter +=1
           # print(i,j)
            i += 1
            j += 1
        if (counter != 0):
            #print(total_length/ counter)
            average_path.append(total_length/counter)
        steps +=1
    label.replace(".", "d")
    print(label)
    results = open("Shortest-Paths-"+data_file,"w")
    results.write("W = "+label)
    for num in average_path:
        results.write(str(num)+"\n")


def main():
    cwd = os.getcwd()
    #Pe-1D-Ns100-Aij-disW-0.txt
    
    data_file = 'Pe-1D-500-Diffusion-Aij-disW-0.txt'
    file_name = cwd+'/data/'+data_file
    graph,lab =  generate_graph(file_name)
    average_path_generator(graph,lab, data_file)
    data_file1 = 'Pe-1D-500-Diffusion-Aij-disW-0d0.txt'
    file_name1 = cwd+'/data/'+data_file1
    graph1,lab1 = generate_graph(file_name1)
    average_path_generator(graph1,lab1, data_file1)


    data_file2 = 'Pe-1D-500-Diffusion-Aij-disW-0d1.txt' 
    file_name2 = cwd+'/data/'+data_file2
    graph2,lab2 = generate_graph(file_name2)
    average_path_generator(graph2,lab2, data_file2)

    data_file3 = 'Pe-1D-500-Diffusion-Aij-disW-0d2.txt' 
    file_name3 = cwd+'/data/'+data_file3
    graph3,lab3 = generate_graph(file_name3)
    average_path_generator(graph3,lab3, data_file3)

    data_file4 = 'Pe-1D-500-Diffusion-Aij-disW-n0d7.txt' 
    file_name4 = cwd+'/data/'+data_file4
    graph4,lab4 = generate_graph(file_name4)
    average_path_generator(graph4,lab4, data_file4)

    data_file5 = 'Pe-1D-500-Diffusion-Aij-disW-n0d8.txt' 
    file_name5 = cwd+'/data/'+data_file5
    graph5,lab5 = generate_graph(file_name5)
    average_path_generator(graph5,lab5, data_file5)

    data_file6 = 'Pe-1D-500-Diffusion-Aij-disW-n0d9.txt' 
    file_name6 = cwd+'/data/'+data_file6
    graph6,lab6 = generate_graph(file_name6)
    average_path_generator(graph6,lab6, data_file6)
    
    data_file7 = 'Pe-1D-500-Diffusion-Aij-disW-n1d0.txt' 
    file_name7 = cwd+'/data/'+data_file7
    graph7,lab7 = generate_graph(file_name7)
    average_path_generator(graph7,lab7, data_file7)    
    
    
    
    #average_path_generator(graph, data_file)
    #average_path_generator(graph1, data_file1)
    #average_path_generator(graph2, data_file2)
    #nx.draw(graph, with_labels=True)
    #plt.show()
    #print(graph.number_of_nodes())
    #print(graph.number_of_edges())
    #print(nx.single_source_dijkstra_path(graph,1))
    #print(nx.single_source_dijkstra_path_length(graph,1))

    #all_path_lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    
    #for i in range(1,401,40):
    #    lattice_spacing = range(1-i,401-i)
    #    path =[]
    #    for j in range(1,401):
    #        path.append(all_path_lengths[i][j])
        #path = all_path_lengths[i]
    #    label = "Node " + str(i)
    #    plt.plot(lattice_spacing, path,label=label)
    #plt.title(data_file.rstrip(".txt"))
    #plt.xlabel("Lattice Spacing")
    #plt.legend()
    #plt.show()

    #lattice_spacing = range(0,100)
    #fig,ax = plt.subplots()
    #ax.plot(lattice_spacing, average_path)
    #ax.set(xlabel='Lattice Spacing', ylabel='Transition Weight', title='Shortest Paths')
    #ax.grid()
    #fig.savefig("test6.png")
    #plt.show()
main()
