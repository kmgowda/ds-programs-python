import random
import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue

def generate_graph(V, E):
   G = nx.DiGraph()
   for i in range(V):
       G.add_node("V"+str(i+1))
   nodes=G.nodes()
   for i in range(E):
       edge = random.sample(nodes,2)
       if G.has_edge(edge[1], edge[0]):
           wd = G.get_edge_data(edge[1], edge[0])
           w = wd['weight']
       else:
           w = random.randint(1, 10)    
       G.add_edge(edge[0], edge[1], weight=w)
   return G

def create_adjaceny_list(G):
    N = nx.number_of_nodes(G)
    adlist = list()
    for i in range(N):
        adlist.append(list())
        adlist[i] = list()
    
    edgeslist = G.edges()
    for edge in edgeslist:
        index= int(edge[0][1:])-1
        dest = int(edge[1][1:])-1
        if dest not in adlist[index]:
            adlist[index].append(dest)
    return adlist    
 
def convert_adjlist_adjmat(adlist, N):
    mat = list()
    for i in range(N):
        mat.append(list())
        mat[i]=[0]*N 
    
    for i in range(len(adlist)):
        for v in adlist[i]:
            mat[i][v] = 1
            # The below one is for undirected graph
            #mat[v][i] = 1   
    return mat        
            
                      

def print_node_edges(G):
    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())    



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
              if ed == tmp:
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



def shortest_path(G, src, dst):
    adlist = create_adjaceny_list(G)
    N = G.number_of_nodes()
    mat = convert_adjlist_adjmat(adlist, N)
    prev = [-1]*N
    st = list()
    st.append(src)
    prev[src]= src
    while len(st):
        node = st.pop(0)
        if node == dst:
           break 
        for i in range(N):
            if mat[node][i]  and prev[i] == -1:
               st.append(i)
               prev[i]=node
    edges = list()             
    i = dst
    while prev[i] != -1 and prev[i] != src:
          edges.append(("V"+str(prev[i]+1), "V"+str(i+1)))
          i = prev[i]
    if prev[i] == -1:
        return None
    else:
        edges.append(("V"+str(src+1), "V"+str(i+1)))
        return edges                         
                
    

if __name__=="__main__":
    print("Python program draw the weighted directed graph")
    V = int(input("How many nodes/ Vertices?"))
    E = int(input("How many edges?"))
    G = generate_graph(V,E)
    print_node_edges(G)
    q = Queue()
    p1= show_graph(G, None, "Generated graph", q)
#    src = int(input("Enter the source node number (Example : V1 as 1)"))
#    dst = int(input("Enter the destination node number (Example : V1 as 1)"))
 
    print("Waiting for the plot to close")
    p1.join()
 
#    edges = shortest_path(G, src-1, dst-1)
    
#    print("The edges of the shortest path are as follows")
#    for i in range(len(edges)-1, -1, -1):
#        print(edges[i], end=" ")
#    print()          
    
#    p2 = show_graph(G, edges, "Shortest path", q)
#    print("waiting for plot close")
#    p2.join()
    print("Its done KMG!")                          