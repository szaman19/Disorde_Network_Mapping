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

def efficiency(file_name):
	graph,label = graph_util.generate_graph(FILE_DIR+file_name)
	all_path_lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
	total = 0
	for i in range(1,501):
		for k in range (1,501):
			if (i != k):
				total += 1/all_path_lengths[i][k]
	return label, total / (500 * 499)
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
            'w-1-5-E-0-diffusion-500.txt'
            ]
    pool = Pool.Pool(processes=len(files))
    results = [pool.apply_async(efficiency, args=(files[x],)) for x in range(len(files))]
    output = [p.get() for p in results]
    print(output)

    file_output = open("efficiency.dat",'w')
    for label, clustering in output:
        line = "W="+str(label) + '\t' + 'S=' + str(clustering) +'\n'
        file_output.write(line)
    file_output.close()

main()