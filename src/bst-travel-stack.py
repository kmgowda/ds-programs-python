from binarytree import Node, bst,pprint

def inorder(cur):
    if cur:
        inorder(cur.left)
        print("%d " %cur.value, end="")
        inorder(cur.right)

def print_inorder(cur, msg):
    print(msg)
    inorder(cur)
    print()

def preorder(cur):
    if cur:
       print("%d " %cur.value, end="") 
       preorder(cur.left)
       preorder(cur.right)        

def print_preorder(cur, msg):
    print(msg)
    preorder(cur)
    print()
    
def postorder(cur):
    if cur:
        postorder(cur.left)
        postorder(cur.right)
        print("%d " %cur.value, end="") 


def print_postorder(cur, msg):
    print(msg)
    postorder(cur)
    print()
    
def preorder_it(cur):
    st = list()
    st.append(cur)
    while len(st):
        top = st.pop()
        print("%d " %top.value , end="")
        if top.right:
            st.append(top.right)
        if top.left:
            st.append(top.left)
                
  
def print_preorder_it(cur, msg):
    print(msg)
    preorder_it(cur)
    print() 


def inorder_it(cur):
    st = list()
    st.append(cur)
    while len(st):
        top = st.pop()
 
        if top.left:
           st.append(top)
           st.append(top.left)
        else:
            print("%d " %top.value, end="")
            while top.right == None and len(st):
                  top = st.pop()
                  print("%d " %top.value, end="")
            if top.right:
               st.append(top.right)      
 
def inorder_it_notworking(cur):
    st = list()
    st.append(cur)
    visited = None
    while len(st):
        top = st.pop()
        if top.left == visited or top.left == None or (len(st) == 0 and visited != None): 
            print("%d " %top.value, end="")
            visited = top
            if top.right:
                st.append(top.right)
                visited = None
        else:
            st.append(top)         
            st.append(top.left)
        print(st)
        input()    

               

def print_inorder_it(cur, msg):
    print(msg)
    inorder_it(cur)
    print() 
    
    
def postorder_it(cur):
    st = list()
    st.append(cur)
    visited = None
    while len(st):
          top = st.pop()
          if top.left == None and top.right == None:
              print("%d " %top.value, end="")
              visited = top
          else:
              if (top.left == visited or top.right == visited) and visited != None:
                  print("%d " %top.value, end="")
                  visited = top
              else:
                  st.append(top)
                  if top.right:
                      st.append(top.right)
                  if top.left:
                      st.append(top.left)
       
 
def print_postorder_it(cur, msg):
    print(msg)
    postorder_it(cur)
    print()                 
                
                        
if __name__=="__main__":
    print("Python program  Binary search Tree traversal")
    n = int(input("what is height of tree?"))
    head = bst(n)
    print("The input binary tree is as follows")
    pprint(head)
    print_preorder(head, "Recusion: The pre order traversal is as follows")
    print_preorder_it(head, "Iteration: The pre order traversal is as follows")
    print_inorder(head, "Recusion: The inorder order traversal is as follows")
    print_inorder_it(head, "Iteration: The in order traversal is as follows")
    print_postorder(head, "Recursion: The post order traversal is as follows ")
    print_postorder_it(head, "Iteration: The post order traversal is as follows")
            
                 
                                                   