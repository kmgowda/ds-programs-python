import random
import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue

def generate_graph(V, E):
   G = nx.Graph()
   for i in range(V):
       G.add_node("V"+str(i+1))
   nodes=G.nodes()
   for i in range(E):
       edge = random.sample(nodes,2)
       if not G.has_edge(edge[1], edge[0]):
          w = random.randint(1, 10)    
          G.add_edge(edge[0], edge[1], weight=w)
   return G
def generate_graph_with_edges(V, E):
   G = nx.Graph()
   for i in range(V):
       G.add_node("V"+str(i+1))
   nodes=G.nodes()
   for ed in E:
       G.add_edge(ed[0], ed[1], weight=ed[2])
   return G

def create_adjaceny_matrix(G):
    N = nx.number_of_nodes(G)
    mat = list()
    for i in range(N):
        mat.append(list())
        mat[i]=[0]*N 
    
    edgeslist = G.edges()
    for edge in edgeslist:
        i= int(edge[0][1:])-1
        j = int(edge[1][1:])-1
        wd = G.get_edge_data(edge[0], edge[1])
        w = wd['weight']
        mat[i][j] = w
        # undirected weighted graph 
        mat[j][i] = w 
    return mat    
 
                   

def print_node_edges(G):
    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph with weights")
    edges = G.edges()
    i = 0
    for ed in edges:
        wd = G.get_edge_data(ed[0], ed[1])
        w = wd['weight']        
        print(ed, end=":")
        print("%d" %w, end=" ")
        i+=1
        if not i%10:
            print()
    print()    



def print_weight_graph(G, edges, title,q):
    print("print_graph")
    ncolor = ['b']*G.number_of_nodes()
    gedges = G.edges()
    ecolor = ['k']*len(gedges)
    widthlt =[0.5]*len(gedges)
    if edges:
       for tmp in edges:
           val = int(tmp[0][1:])-1
           ncolor[val] = 'r'
           val = int(tmp[1][1:])-1
           ncolor[val] = 'r'
       i = 0
       for ed in  gedges:
          for tmp in edges:
              # undirected weighted graph
              if ed == tmp or ed ==(tmp[1],tmp[0]):
                 ecolor[i]='g'
                 widthlt[i]=1.5
          i+=1
 
    elabels = nx.get_edge_attributes(G,'weight')
    layout = nx.circular_layout(G)
    nx.draw_networkx(G,  pos=layout, with_labels=True, node_color=ncolor, edge_color = ecolor, alpha = 0.5, width=widthlt, arrows=True)
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=elabels)
    q.put(None)
    plt.title(title)
    plt.axis('off')
    plt.show()
 

def show_graph(G, edges, title, q):
    p = Process(target=print_weight_graph, args=(G,edges,title, q))
    p.start()
    q.get()
    return p


def prims_spanning_tree(mat,N):
    prev = [-1]*N
    dist = [0]*N
    st = list()
    st.append(0)
    prev[0] = 0
    while len(st):
        node = st.pop(0)
        for i in range(N):
            if mat[node][i]:
               dst = dist[node]+mat[node][i]
               if prev[i] == -1 or (prev[i] != -1 and  (dst < dist[i])):
                   dist[i] = dst
                   prev[i] = node
                   st.append(i)    
    return prev                
    

def spanning_tree(G):
    mat = create_adjaceny_matrix(G)
    N = G.number_of_nodes()
    prev = prims_spanning_tree(mat,N)
    i = N-1
    edges= list()
    total = 0
    while i >= 0:
         if prev[i] != -1 and prev[i] != i:
            edges.append(("V"+str(prev[i]+1), "V"+str(i+1), mat[prev[i]][i]))
            total +=mat[prev[i]][i]
         i -= 1
    return edges, total                         
                
    

if __name__=="__main__":
    print("Python program to implement the spanning tree by prims algorithm for weighted undirected graph")
    V = int(input("How many nodes/ Vertices?"))
    E = int(input("How many edges?"))
    G = generate_graph(V,E)
    print_node_edges(G)
    q = Queue()
    p1= show_graph(G, None, "Generated graph", q)
 
 
    edges, total = spanning_tree(G)
    if not edges:
        print("No spanning tree found" )
        exit()
    print("The edges of the spanning tree are as follows")
    for i in range(len(edges)-1, -1, -1):
        print("(%s, %s):%d" %(edges[i][0], edges[i][1], edges[i][2]), end=" ")
        
    print()
    print("The Minimal spanning tree distance from node V1 is %d" %total)          
    
    G1 = generate_graph_with_edges(V, edges)
    p2 = show_graph(G1, None, "Prims algorithm for minimal spanning tree", q)
    print("waiting for plots to close")
    p1.join()
    p2.join()
    print("Its done KMG!")                          