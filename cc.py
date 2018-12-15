from matplotlib import pyplot 
import numpy as np
import scipy 
import networkx as nx
import graph_util
from multiprocessing import process
from multiprocessing import pool as Pool
from threading import Thread
import os

CWD = os.getcwd()
CWD+='/500_Diffusion_data/'

def per_graph_cc(file_name):
    file_name = CWD + file_name
    graph,label = graph_util.generate_graph(file_name)


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
            'Pe-1D-500-Diffusion-Aij-disW-0d1.txt'
            'w-1-3-E-0-diffusion-500.txt',
            'w-1-4-E-0-diffusion-500.txt',
            'w-1-5-E-0-diffusion-500.txt',
            'Pe-1D-500-Diffusion-Aij-disW-0d1.txt'
            ]
    pool = Pool.Pool(processes=len(files))
    results = [pool.apply_async(per_graph_cc, args=(files[x])) for x in range(len(files))]
    output = [p.get() for p in results]
    print(output)

    file_output = open("clustering_coefficient_per_disorder.txt",'w')
    for i in output:
        s='\t'.join(i)
        file_output.write(s)
    file_output.close()
main()
