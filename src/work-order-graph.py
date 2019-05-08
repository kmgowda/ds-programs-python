import random,copy
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
       if not G.has_edge(edge[1], edge[0]):
          G.add_edge(edge[0], edge[1])
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
        mat[i][j] = 1
        # undirected unweighted graph 
        #mat[j][i] = 1
    return mat    
 
                   

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


def create_work_order_list(mat, N):
    visited=[False]*N
    lt =list()
    for i in range(N):
        flag = True
        for j in range(N):
            if mat[j][i]:
               flag = False
               break
        if flag:
            visited[i] = True
            lt.append(i+1)
    index = 0
    while index < len(lt):
        k = lt[index]-1
        for j in range(N):
            mat[k][j] = 0
        for i in range(N):
            if not visited[i]:
                flag = True
                for j in range(N):
                    if mat[j][i]:
                        flag = False
                        break
                if flag:
                    visited[i] = True
                    lt.append(i+1)
        index+=1            
    return lt                                

def print_adjacency_matrix(mat):
    print("The Adjacency matrix is as follow")
    for i in range(len(mat)):
        print("%d" %(i+1), end="")
        print(mat[i])                            

def work_order(G):
    mat = create_adjaceny_matrix(G)
    print_adjacency_matrix(mat)
    return create_work_order_list(mat[:], G.number_of_nodes())

def create_work_order_dfs(mat, N):
    visited = [0]*N
    st = list()
    st.append(0)
    visited[0] = 1
    build = list()
    while len(st):
        v = st[-1]
        flag = True
        tmp = list()
        for i in range(N):
            if mat[v][i]:
               if visited[i] == 0:
                  tmp.append(i)
                  visited[i] = 1
                  flag = False
               elif visited[i] == 1:
                  flag = False   
        if flag:
            build.append(v+1)
            st.pop()
            visited[v] = 2
        else:
            for item in tmp:
                st.append(item)    
    return build                
                
                
        

if __name__=="__main__":
    print("Python program to implement order of the work with dependency graph")
    V = int(input("How many nodes/ Vertices?"))
    E = int(input("How many edges?"))
    G = generate_graph(V,E)
    print_node_edges(G)
    q = Queue()
    p1= show_graph(G, None, "Generated graph", q)
    mat = create_adjaceny_matrix(G)
    print_adjacency_matrix(mat)
    N = G.number_of_nodes()
    tmp = copy.deepcopy(mat)
    lt = create_work_order_list(tmp, N)
    if len(lt):
        print("The order of nodes/ projects to carried out are as follows")
        print(lt)
    else:
        print("No order of works")
    lt = create_work_order_dfs(mat, N)
    if len(lt):
        print("The order of nodes/ projects to carried out are as follows")
        print(lt)
    else:
        print("No order of works")            
 
    print("Waiting for the plot to close")
    p1.join()
    print("Its done KMG!")                          