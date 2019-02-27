import networkx as nx 
import matplotlib as mp
import matplotlib.pyplot as plt 
import sys
from multiprocessing import pool as Pool

def generate_graph(file_name, reciprocal = True):
    data = open(file_name)
    
    graphs = []
    labels = []
    condensates = []
    #graph = nx.DiGraph()
    #label = ''
    #condensate = ''
    max_val = 0
    max_vals=[]

    for line in data:
        #Clean up the data to get the numerical values
        data_points = line.strip().split()
        data_points = " ".join(data_points).split()
        if (data_points[0] == 'For'):
            graph = nx.Graph()
            label = str(data_points[2])
            condensate = str(data_points[4])
            graphs.append(graph)
            labels.append(label)
            condensates.append(condensate)

            if (max_val != 0):
                max_vals.append(max_val)
            max_val=0
        else:

        #data_points currently hold [from_site_index, to_site_index, correlation_val]
            site_i = int(data_points[0])
            site_j = int(data_points[1])
            
            corr = float(data_points[2])
        #Regular division is not helpful in this situation. Make sure to not add when i = j, because corr == inf

            if(site_i != site_j):
            #print(site_i, site_j, corr)
                if reciprocal:
                    corr = 1 / corr
                if (corr > max_val):
                    max_val = corr
                
                graph.add_edge(site_i,site_j, weight = corr)

    max_vals.append(max_val)
    #adj_matrix = nx.adjacency_matrix(graph)
    #print(np.matrix(adj_matrix))
    return graphs, labels, condensates, max_vals

def graph_visualize(graph,label, cond, max_val,order):
    fig = plt.figure(order)

    layout = nx.layout.circular_layout(graph)
    
    M = graph.number_of_edges()
    edge_colors = range(2,M+2)
    e = graph.edges()
    print(max_val)

    

    edge_alphas = [(graph[u][v]['weight']/max_val) for u,v in e]

    #print(edge_alphas)
    
    nodes = nx.draw_networkx_nodes(graph,layout,node_size=20,node_color='blue')

    edges = nx.draw_networkx_edges(graph,layout,arrows=True,node_size=20,edge_cmap=plt.cm.Blues,width=1,arrowsize=2,arrowstyle='->',edge_color=edge_colors)

    for i in range(M):
        edges[i].set_alpha(edge_alphas[i])

    pc = mp.collections.PatchCollection(edges,cmap=plt.cm.Blues)
    pc.set_array([max_val * i for i in edge_alphas])
    
    fig.colorbar(pc)
    ax = fig.gca()
    ax.set_axis_off()
    label = str(label).replace(".","d")
    cond = str(cond).replace(".","d")
    fig.savefig("BEC_Graph_beta="+label+"condensate="+cond+".svg",format='svg')
def cc(graph, beta, condensate):
    adjacency_matrix = nx.to_numpy_array(graph)
    c_c = 0
    val = 0
    #print(adjacency_matrix.shape[0])
    for i in range(adjacency_matrix.shape[0]):
        W = 0
        for j in range(adjacency_matrix.shape[0]):
            for k in range(adjacency_matrix.shape[0]):
                if (i != j and i != k and k != j):
                    W += adjacency_matrix[j][k]
        val += W
    c_c = val / (51 * 50 * 49)
    #print ("B="+str(beta)+" C=" + str(condensate)," \t", c_c)
    return beta,c_c
def avg_path(graph,beta,condensate):
    avg = nx.average_shortest_path_length(graph, weight='weight')
    return beta, avg

def file_reader(file_name):
    reader = open(file_name, 'r')

    for line in reader:
        print(line)
def main():
    if (len(sys.argv) < 2):
        print("Needs file name")
    else:
        file_name = sys.argv[1]
        graphs, betas, condensates, max_vals = generate_graph(file_name, reciprocal=False)

        #pool = Pool.Pool(processes=len(graphs))
        #results = [pool.apply_async(cc, args=(graphs[i],betas[i],condensates[i])) for i in range(len(graphs))]
        #output = [p.get() for p in results]

        pool = Pool.Pool(processes=len(graphs))
        avg_p = [pool.apply_async(avg_path, args=(graphs[i],betas[i],condensates[i])) for i in range(len(graphs))]
        avg_p_results = [p.get() for p in avg_p]
        #print(output)
        file_name = open('average_shortest_path_length.dat', 'w')
        for beta,clustering in avg_p_results:
            line = "L="+str(beta) + '\t' + 'C=' + str(clustering) +'\n'
            file_name.write(line)
            print (line)
main()
