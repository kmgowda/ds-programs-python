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
          G.add_edge(edge[0], edge[1])
   return G

def print_node_edges(G):
    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph with weights")
    edges = G.edges()
    i = 0
    for ed in edges:
        print(ed, end=" ")
        i+=1
        if not i%10:
            print()
    print()    

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
        mat[i][j] = 1
        # undirected weighted graph 
        mat[j][i] = 1
    return mat    

def print_graph(G, edges, title,q):
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
 
    layout = nx.circular_layout(G)
    nx.draw_networkx(G,  pos=layout, with_labels=True, node_color=ncolor, edge_color = ecolor, alpha = 0.5, width=widthlt, arrows=True)
    q.put(None)
    plt.title(title)
    plt.axis('off')
    plt.show()
 
def show_graph(G, edges, title, q):
    p = Process(target=print_graph, args=(G,edges,title, q))
    p.start()
    q.get()
    return p

def all_path_src_dst(mat, N, src,dst, path, all):
    if src == dst:
        return path, True
    path.append("V"+str(src))
    for i in range(N):
        if mat[src][i] and ("V"+str(mat[src][i]+1) not in path):
            p , ret =  all_path_src_dst(mat, N, i, dst, path, all)
            if ret:
                all.append(p)
    return all, False            


def all_path_src_dst_itr(mat, N, src,dst, path, allp):
    st =list()
    path.append(src)
    st.append(path)
    while (len(st)):
          path = st.pop()
          last = path[-1]
          if last == dst:
              tmp = list()
              for v in path:
                  tmp.append(str(v+1))
              allp.append(tmp)
          else:
              for i in range(N):
                  if mat[last][i] and (i not in path):
                       newpath = path[:]
                       newpath.append(i)
                       st.append(newpath)
    return allp, False 
  

            
def print_all_paths(G,src,dst):
    mat = create_adjaceny_matrix(G)
    N = nx.number_of_nodes(G)    
    paths , ret =  all_path_src_dst_itr(mat, N, src-1,dst-1, list(), list())
    if ret:
       print("both source %s and destination %s are same" %("V"+str(src+1), "V"+str(dst+1)))        
       return
    elif len(paths):
       print("Number of paths found : %d" %(len(paths)))         
       for i in range(len(paths)):
           print("%d" %(i+1), end=":")
           print(paths[i]) 
    else:
       print("No path found from %s to %s" %("V"+str(src+1), "V"+str(dst+1)))


if __name__=="__main__":
    print("Python program to implement all paths from source to destination for undirected graph")
    V = int(input("How many nodes/ Vertices?"))
    E = int(input("How many edges?"))
    G = generate_graph(V,E)
    print_node_edges(G)
    q = Queue()
    p1= show_graph(G, None, "Generated graph", q)
    src = int(input("Enter the source node number (Example : V1 as 1)"))
    dst = int(input("Enter the destination node number (Example : V1 as 1)")) 
    print_all_paths(G, src, dst)    
    print("waiting for plot to close")
    p1.join()
    print("Its done KMG!")                          