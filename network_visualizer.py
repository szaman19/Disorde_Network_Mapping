import matplotlib.pyplot as plt 
import graph_util 
import networkx as nx
import os 

CWD = os.getcwd()
FILE_DIR = CWD + '/500_Diffusion_data/'
def visualizer(file_name):
	file_name = FILE_DIR + file_name

	graph, label = graph_util.generate_graph(file_name)
	

	options = {
        'node_color': 'black',
        'node_size': 2,
        'line_color': 'grey',
        'linewidths': 0,
        'width': 0.001,
    }

	nx.draw_spectral(graph, **options)
	plt.show()

def main():
	file_name = 'w-0-E-0-diffusion-500.txt'
	visualizer(file_name)
main()