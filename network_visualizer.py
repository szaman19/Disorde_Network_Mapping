import matplotlib.pyplot as plt 
import graph_util 
import networkx as nx
import matplotlib as mp
import os 
from multiprocessing import pool as Pool
from matplotlib.pyplot import figure
figure(num=None,figsize=(3.5,3.5),dpi=200,facecolor='w',edgecolor='k')

CWD = os.getcwd()
FILE_DIR = CWD + '/500_Diffusion_data/'
def visualizer(file_name, order):
        file_name = FILE_DIR + file_name
        fig = plt.figure(num=order,figsize=(3.5,3.5),dpi=200,facecolor='w',edgecolor='k')
        graph, label = graph_util.di_generate_graph(file_name, reciprocal=False)
        layout = nx.layout.circular_layout(graph)
        print("graph generated")
        M = graph.number_of_edges()
        max_val=1
        edge_colors = range(2,M+2)
        e = graph.edges()
        edge_alphas = [(graph[u][v]['weight']/max_val) for u,v in e]
        nodes = nx.draw_networkx_nodes(graph,layout,node_size=20,node_color='blue')
        edges = nx.draw_networkx_edges(graph,layout,arrows=True,node_size=20,edge_cmap=plt.cm.Blues,width=1,arrowsize=2,arrowstyle='->',edge_color=edge_colors)
        for i in range(M):
            edges[i].set_alpha(edge_alphas[i])
        pc = mp.collections.PatchCollection(edges,cmap=plt.cm.Blues)
        pc.set_array([max_val * i for i in edge_alphas])
        fig.colorbar(pc)
        ax = fig.gca()
        ax.set_axis_off()
        #nx.draw_circular(graph, **options)
        plt.tight_layout()
	# plt.show()
        plt.savefig(label+".svg",format='svg')
        plt.savefig(label+".png",format='png')

def main():
	file_name = 'w-0-E-0-diffusion-500.txt'
	file_name2 = 'w-1-5-E-0-diffusion-500.txt'

	pool = Pool.Pool(processes=2)
	p1 = pool.apply_async(visualizer, args=(file_name,1, ))
	p2 = pool.apply_async(visualizer, args=(file_name2,2, ))
	p1.get()
	p2.get()
main()
