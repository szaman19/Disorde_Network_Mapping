from multiprocessing import process
from multiprocessing import pool as Pool
import os
import copy
import networkx as nx
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import graph_util
from decimal import Decimal
CWD = os.getcwd()
FILE_DIR = CWD + "/500_Diffusion_data/"

def average_shortest_path(file_name, bc = 'periodic'):
    graph,label = graph_util.generate_graph(FILE_DIR+file_name)
    all_path_lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    average_path = []
    if (bc == 'periodic'):

        average_path = [0] * 251
        for i in range(1,501):
            for k in range(1,501):
                distance = int(abs(i-k))
                if(distance < 250):
                    index = distance 
                    average_path[index] += all_path_lengths[i][k]
                else:
                    index = 500 - distance
                    average_path[index] += all_path_lengths[i][k]
        file_name = 'sp-'+file_name
        writer = open(file_name,"w")
        writer.write("W = " + label + '\n')
        for vals in average_path:
            writer.write(str(vals/500)+'\n')
        writer.close()
        return label
    else:
        return "invalid argument"
        
def trial(f):
    print(f)
def generate_shortest_paths(files):
    for x in files:
        print(x)
    pool = Pool.Pool(processes=len(files))
    results = [pool.apply_async(average_shortest_path, args=(x,)) for x in files]
    output = [p.get() for p in results]
    print(output)

def visualize_paths(files):
    File_Dir = CWD + '/Avg_Paths/'
    x_vals = range(251)
    for each in files:
        file_name = File_Dir+'sp-'+each
        avg_path_data = []
        file_read = open(file_name,'r')
        label = 0
        for lines in file_read:
            if (len(lines.split()) > 1):
                label = "%.2f" % float(lines.split()[2])
            else:
                avg_path_data.append(float(lines))
        plt.plot(x_vals,avg_path_data,label=label)
        plt.xlabel('Lattic Distance (a)', fontsize=20)
        plt.ylabel('Graph Distance (l)', fontsize=20)
    plt.legend()
    plt.show()


def main():
    files = ['w-0-E-0-diffusion-500.txt',
    'w-0-1-E-0-diffusion-500.txt',
    'w-0-2-E-0-diffusion-500.txt',
    'w-0-3-E-0-diffusion-500.txt',
    'w-0-4-E-0-diffusion-500.txt',
    'w-0-5-E-0-diffusion-500.txt',
    'w-0-6-E-0-diffusion-500.txt', 
    'w-0-7-E-0-diffusion-500.txt',
    'w-0-8-E-0-diffusion-500.txt', 
    'w-0-9-E-0-diffusion-500.txt',
    'w-1-0-E-0-diffusion-500.txt',
    'w-1-1-E-0-diffusion-500.txt',
    'w-1-2-E-0-diffusion-500.txt',
    'w-1-3-E-0-diffusion-500.txt',
    'w-1-4-E-0-diffusion-500.txt',
    'w-1-5-E-0-diffusion-500.txt']
    visualize_paths(files)
    

main()
