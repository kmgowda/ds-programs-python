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


def create_sort_edges(G):
    edges = G.edges()
    d = dict()
    for ed in edges:
        wd = G.get_edge_data(ed[0], ed[1])
        w = wd['weight']
        if not d.get(w):
            d[w] = list()
        d[w].append((ed[0], ed[1], w))
    lt =list()          
    for key in sorted(d.keys()):
        for item in d[key]:
            lt.append(item)
    return lt           

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


def kruskal_spanning_tree(edges , N):
    k_edges=list()
    sets = [None]*N
    for i in range(N):
        sets[i] = set()
        sets[i].add(i)       
    total = 0
    for ed in edges:
        i= int(ed[0][1:])-1
        j = int(ed[1][1:])-1
        
        for index in range(N):
            if i in sets[index]:
                i_pos = index
            if j in sets[index]:
                j_pos = index    
        if i_pos == j_pos:
            continue    
        else:
            sets[i_pos] |= sets[j_pos]
            sets[j_pos].clear() 
            k_edges.append((ed[0],ed[1],ed[2]))
            total +=ed[2]
    return k_edges, total        
            


def spanning_tree(G):
    edges = create_sort_edges(G)
    N = G.number_of_nodes()
    edges, total = kruskal_spanning_tree(edges,N)
    return edges, total                         
                
    

if __name__=="__main__":
    print("Python program to implement the spanning tree by kruskal's algorithm for weighted undirected graph")
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
        if not i%10:
            print()
        
    print()
    print("The Minimal spanning tree distance is %d" %total)          
    
    G1 = generate_graph_with_edges(V, edges)
    p2 = show_graph(G1, None, "krushkals's algorithm for minimal spanning tree", q)
    print("waiting for plots to close")
    p1.join()
    p2.join()
    print("Its done KMG!")                          