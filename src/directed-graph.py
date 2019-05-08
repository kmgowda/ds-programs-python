import random
import networkx as nx
import matplotlib.pyplot as plt
from multiprocessing import Process

def generate_graph(V, E):
   G = nx.DiGraph()
   for i in range(V):
       G.add_node("V"+str(i+1))
   nodes=G.nodes()
   for i in range(E):
       edges = random.sample(nodes,2)
       G.add_edge(edges[0], edges[1])
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
            
 
         
def dfs(mat,N):
    visit = [0]*N
    st = list()
    nodest = list()
    st.append(0)
    edges = set()
    while len(st):
        node = st.pop()
        if not visit[node]:
           visit[node] = 1 
           nodest.append("V"+str(node+1))
           for i in range(N-1, 0, -1):
               if mat[node][i] and not visit[i]:
                  st.append(i)
                  edges.add(("V"+str(node+1), "V"+str(i+1)))
    return nodest, edges


def bfs(mat,N):
    visit = [0]*N
    st = list()
    nodest = list()
    st.append(0)
    edges = set()
    while len(st):
        node = st.pop(0)
        if not visit[node]:
           visit[node] = 1 
           nodest.append("V"+str(node+1))
           for i in range(N):
               if mat[node][i] and not visit[i]:
                  st.append(i)
                  edges.add(("V"+str(node+1), "V"+str(i+1)))
    return nodest, edges               
                            

def print_node_edges(G):
    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())    
#    print("Adjaceny matrix")
#    al=nx.adjacency_matrix(G)
#    print(al)
#    print("Adjacency list")
#    for line in nx.generate_adjlist(G):
#        print(line)
#    ncolor = [random.choice(['b','g','r','c','m','y','k']) for x in range(G.number_of_nodes())]



def print_graph(G, edges, title):
    ncolor = ['b']*G.number_of_nodes()
    for tmp in edges:
        val = int(tmp[0][1:])-1
        ncolor[val] = 'r'
        val = int(tmp[1][1:])-1
        ncolor[val] = 'r'
    gedges = G.edges()
    ecolor = ['k']*len(gedges)
    widthlt =[0.5]*len(gedges)
    i = 0
    for ed in  gedges:
        for tmp in edges:
            if ed == tmp:
               ecolor[i]='g'
               widthlt[i]=1.5
        i+=1
    plt.title(title)    
    nx.draw(G, with_labels=True,node_color=ncolor, edge_color = ecolor, alpha = 0.5, width=widthlt,arrows=True)
    plt.show()

def show_graph(G, edges, title):
    t = Process(target=print_graph, args=(G,edges,title,))
    t.start()
    return t




if __name__=="__main__":
    print("Python program to generate the graph and print the same")
    V = int(input("How many nodes/ Vertices?"))
    E = int(input("How many edges?"))
    G = generate_graph(V,E)
    adlist = create_adjaceny_list(G)
    print("The Adjacency list is as follows")
    print(adlist)
    mat = convert_adjlist_adjmat(adlist, G.number_of_nodes())
#    print("The Adjacency matrix is as follow")
#    for i in range(len(mat)):
#        print("%d" %(i+1), end="")
#        print(mat[i])
    dflist, dedges = dfs(mat, G.number_of_nodes())
    print("The DFS list is as follows")
    print(dflist)
    bflist, bedges = bfs(mat, G.number_of_nodes())
    print("The BFS list is as follows")
    print(bflist)     
    print_node_edges(G)    
    t1= show_graph(G, dedges, "DFS") 
    t2 = show_graph(G, bedges, "BFS")
    print("waiting for plots close")
    t1.join()
    t2.join()
    print("Its done KMG!")                          
