import matplotlib.pyplot as plt 
import graph_util 
import networkx as nx
import os 

CWD = os.getcwd()
FILE_DIR = CWD + '/500_Diffusion_data/'
def visualizer(file_name):
	file_name = FILE_DIR + file_name

	graph, label = graph_util.di_generate_graph(file_name, reciprocal=False)
	

	layout = nx.layout.circular_layour(graph)

	print("graph generated")
	# options = {
 #        'node_color': 'black',
 #        'node_size': 2,
 #        'line_color': 'grey',
 #        'linewidths': 0,
 #        'width': 0.001,
 #    }

 	M = graph.number_of_edges()
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

	nx.draw_circular(graph, **options)
	plt.tight_layout()
	# plt.show()
	plt.savefig(label+".svg",format='svg')


def main():
	file_name = 'w-0-E-0-diffusion-500.txt'
	file_name2 = 'w-1-5-E-0-diffusion-500.txt'

	pool = Pool.Pool(processes=2)
	p1 = pool.apply_async(visualizer, args=(file_name, ))
	p2 = pool.apply_async(visualizer, args=(file_name2, ))
	p1.get()
	p2.get()
main()