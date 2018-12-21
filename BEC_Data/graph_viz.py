import networkx as nx 
import matplotlib as mp
import matplotlib.pyplot as plt 
import sys 

def generate_graph(file_name):
    data = open(file_name)
    
    temp_lst = []
    graph = nx.DiGraph()
    label = ''
    condenstae = ''
    for line in data:
        #Clean up the data to get the numerical values
        data_points = line.strip().split()
        data_points = " ".join(data_points).split()
        if (data_points[0] == 'For'):
            label = str(data_points[2])
            condensate = str(data_points[4])
        else:

        #data_points currently hold [from_site_index, to_site_index, correlation_val]
            site_i = int(data_points[0])
            site_j = int(data_points[1])
            
            corr = float(data_points[2])
        #Regular division is not helpful in this situation. Make sure to not add when i = j, because corr == inf

            if(site_i != site_j):
            #print(site_i, site_j, corr)
                graph.add_edge(site_i,site_j, weight = corr)
        
    #adj_matrix = nx.adjacency_matrix(graph)
    #print(np.matrix(adj_matrix))
    return graph, label, condensate

def graph_visualize(graph,label):
    layout = nx.layout.spring_layout(graph)
    node_size = [3 + 10 * i for i in range(len(graph))]
    M = graph.number_of_edges()
    edge_colors = range(2,M+2)
    edge_alphas = [(5+i)/(M+4) for i in range(M)]
    
    nodes = nx.draw_networkx_nodes(graph,layout,node_size=node_size,node_color='blue')
    edges = nx.draw_networkx_edges(graph,layout,arrows=True,node_size=node_size,edge_cmap=plt.cm.Blues,width=2,arrowsize=2,arrowstyle='->',edge_color=edge_colors)

    for i in range(M):
        edges[i].set_alpha(edge_alphas[i])

    pc = mp.collections.PatchCollection(edges,cmap=plt.cm.Blues)
    pc.set_array(edge_colors)
    plt.colorbar(pc)
    ax = plt.gca()
    ax.set_axis_off()
    plt.savefig("BEC_Graph.png",format='png')

def file_reader(file_name):
    reader = open(file_name, 'r')

    for line in reader:
        print(line)
def main():
    if (len(sys.argv) < 2):
        print("Needs file name")
    else:
        file_name = sys.argv[1]
        #file_reader(file_name)
        graph, beta, condenstate = generate_graph(file_name)
        graph_visualize(graph,beta)
main()
