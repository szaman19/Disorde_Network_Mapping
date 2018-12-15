from __future__ import division
from multiprocessing import process
from multiprocessing import pool as Pool
from threading import Thread
import os
import copy
import networkx as nx
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cc

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
                corr = 1/float(data_points[2])
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


   # print(all_path_lengths[0])
    #while (steps < 501):
    #    i = 1
    #    j = (1 +steps ) 
    #    counter = 0
    #    total_length = 0
    #    while(j < 501):
    #        total_length += all_path_lengths[i][j]
    #        counter +=1
    #        print(i,j)
    #        i += 1
    #        j += 1
    #    if (counter != 0):
            #print(total_length/ counter)
    #        average_path.append(total_length/counter)
    #    steps +=1
    average_path = [0] * 500
    for i in range(1,501):
        for k in range(1,501):
            index = int(abs(i-k))
            average_path[index] += all_path_lengths[i][k]

    label.replace(".", "d")
    print(label)
    results = open("Shortest-Paths-"+data_file,"w")
    results.write("W = "+label + '\n')
    for num in average_path:
        results.write(str(num/500)+"\n")
    results.close()

def clustering_coefficient(graph, label):
    cc = nx.clustering(graph, weight='weight')
    label = label.replace(".","d")
    file_open = open("Pe-1D-Diffusion-CC-NoRec-W-"+label+".txt", 'w')
    file_open = open("Pe-1D-Diffusion-CC-NoRec-W-"+label+".txt", 'w')
 
    total = 0
    for key,value in cc.items():
        str_out = str(key) + "-" + str(value)+"\n"
        file_open.write(str_out)
        total += value
    file_open.close()
    total = total / 500
    out = (str(total),label)
    return out
def clustering_coeff (graph, result):
    result[1] = cc.graph_cc(graph)

def avg_path (graph,result):
    avg = nx.average_shortest_path_length(graph, weight='weight')
    result[0] = avg 
def small_world_sigma (graph, label):
    #sigma = nx.algorithms.smallworld.sigma(graph)
   
   
    results = [None]*2
    graph2 = copy.deepcopy(graph)
    thread_1 = Thread(target=clustering_coeff,args=(graph,results))
    thread_2 = Thread(target=avg_path,args=(graph2,results))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    
    sigma = results[1]/results[0]

    #label = label.replace(".","d")
    #file_open = open("Pe-1d-Diffusion-small-world-W-"+label+".txt","w")
    #label = "W=" + label + "\n"
    #file_open.write(label)
    #file_open.write("CC:\t" + str(results[1]) + "\t Shortest_Avg_Path \t" + str(results[0]))
    #print(label + "CC:\t" + str(results[1]) + "\t Shortest_Avg_Ppath \t" + str(results[0]))
    out = (str(results[1]),str(results[0]),str(1/results[0]),str(sigma),label)

    
    #label = label.replace(".","d")
    #f = "Diffusion-500-W-"+label+".txt"
    #average_path_generator(graph,label,f)
    return out
def trial():
    pool = Pool.Pool(processes=4)
    results = [pool.apply(clustering_coefficient, args=(x,x*2,)) for x in range(1,7)]
    print(results)

def main():
    cwd = os.getcwd()
    
    cwd += '/500_Diffusion_data/'
    graphs = []
    labels = []

    data_file = 'w-0-0-E-0-diffusion-500.txt'
    file_name = cwd+data_file
    graph,lab =  generate_graph(file_name)
    #average_path_generator(graph,lab, data_file)
     
    graphs.append(graph)
    labels.append(lab)
    
    data_file1 = 'w-0-1-E-0-diffusion-500.txt'
    file_name1 = cwd+data_file1
    graph1,lab1 = generate_graph(file_name1)
    #average_path_generator(graph1,lab1, data_file1)
    
    graphs.append(graph1)
    labels.append(lab1)

    data_file2 = 'w-0-2-E-0-diffusion-500.txt' 
    file_name2 = cwd+data_file2
    graph2,lab2 = generate_graph(file_name2)
    #average_path_generator(graph2,lab2, data_file2)
    graphs.append(graph2)
    labels.append(lab2)
    
    data_file3 = 'w-0-3-E-0-diffusion-500.txt' 
    file_name3 = cwd+data_file3
    graph3,lab3 = generate_graph(file_name3)
    #average_path_generator(graph3,lab3, data_file3)
    graphs.append(graph3)
    labels.append(lab3)
    
    data_file4 = 'w-0-4-E-0-diffusion-500.txt' 
    file_name4 = cwd+data_file4
    graph4,lab4 = generate_graph(file_name4)
    #average_path_generator(graph4,lab4, data_file4)
    graphs.append(graph4)
    labels.append(lab4)

    data_file5 = 'w-0-5-E-0-diffusion-500.txt' 
    file_name5 = cwd+data_file5
    graph5,lab5 = generate_graph(file_name5)
    #average_path_generator(graph5,lab5, data_file5)
    graphs.append(graph5)
    labels.append(lab5)

    data_file6 = 'w-0-6-E-0-diffusion-500.txt' 
    file_name6 = cwd+data_file6
    graph6,lab6 = generate_graph(file_name6)
    #average_path_generator(graph6,lab6, data_file6)
    graphs.append(graph6)
    labels.append(lab6)
    
    data_file7 = 'w-0-7-E-0-diffusion-500.txt' 
    file_name7 = cwd+data_file7
    graph7,lab7 = generate_graph(file_name7)
    #average_path_generator(graph7,lab7, data_file7)    
    graphs.append(graph7)
    labels.append(lab7)
    
    data_file8='w-0-8-E-0-diffusion-500.txt'
    file_name8 = cwd+data_file8
    graph8,lab8 = generate_graph(file_name8)
    #average_path_generator(graph8,lab8,data_file8)
    graphs.append(graph8)
    labels.append(lab8)

    data_file9 = 'w-0-9-E-0-diffusion-500.txt'
    file_name9 = cwd+data_file9
    graph9,lab9 = generate_graph(file_name9)
    #average_path_generator(graph9,lab9,data_file9)
    graphs.append(graph9)
    labels.append(lab9)

    data_file10 = 'w-1-0-E-0-diffusion-500.txt'
    file_name10 = cwd + data_file10
    graph10,lab10 = generate_graph(file_name10)
    #average_path_generator(graph10,lab10,data_file10)
    graphs.append(graph10)
    labels.append(lab10)
    

    data_file11 = 'Pe-1D-500-Diffusion-Aij-disW-0d1.txt'
    file_name11 = cwd + data_file11
    graph11,lab11 = generate_graph(file_name11)

    graphs.append(graph11)
    labels.append(lab11)

    data_file12 = 'Pe-1D-500-Diffusion-Aij-disW-0d2.txt'
    file_name12 = cwd + data_file12
    graph12,lab12 = generate_graph(file_name12)

    graphs.append(graph12)
    labels.append(lab12)
    
    
    data_file13 = 'w-1-1-E-0-diffusion-500.txt'
    file_name13 = cwd + data_file13
    graph13,lab13 = generate_graph(file_name13)
    #average_path_generator(graph10,lab10,data_file10)
    graphs.append(graph13)
    labels.append(lab13)

    
    data_file14 = 'w-1-2-E-0-diffusion-500.txt'
    file_name14 = cwd + data_file14
    graph14,lab14 = generate_graph(file_name14)
    #average_path_generator(graph10,lab10,data_file10)
    graphs.append(graph14)
    labels.append(lab14)

    
    data_file15 = 'w-1-3-E-0-diffusion-500.txt'
    file_name15 = cwd + data_file15
    graph15,lab15 = generate_graph(file_name15)
    #average_path_generator(graph10,lab10,data_file10)
    graphs.append(graph15)
    labels.append(lab15)

    data_file16 = 'w-1-4-E-0-diffusion-500.txt'
    file_name16 = cwd + data_file16
    graph16,lab16 = generate_graph(file_name16)
    #average_path_generator(graph10,lab10,data_file10)
    graphs.append(graph16)
    labels.append(lab16)


    data_file17 = 'w-1-5-E-0-diffusion-500.txt'
    file_name17 = cwd + data_file17
    graph17,lab17 = generate_graph(file_name17)
    #average_path_generator(graph10,lab10,data_file10)
    graphs.append(graph17)
    labels.append(lab17)
    
    pool = Pool.Pool(processes=len(graphs))
    results = [pool.apply_async(small_world_sigma, args=(graphs[x],labels[x])) for x in range(len(graphs))]
    output = [p.get() for p in results]
    print(output)

    file_output = open("Small-World-Sigma-Self-Generated.txt",'w')
    file_output.write("CC \t ASP \t Eff \t Sigma \t W \n")
    for i in output:
        s='\t'.join(i)
        s+= '\n'
        file_output.write(s)
    file_output.close()
    
main()
#trial()
