from binarytree import  Node, bst, pprint, convert
import random


class knode(Node):
    def __init__(self, value):
        Node.__init__(self,value)
        self.size = 1

def get_i_node(root, index):
    if root == None:
           return None
       
    if root.left:
        size = root.left.size
    else:
        size = 1
    if index == size:
        return root.value
    elif index < size:
        get_i_node(root.left, index)
    else:
        get_i_node(root.right, index-size+1)    
        
            


class bs_tree:
    def __init__(self):
        self.root = None
    
    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            prev = cur
            while cur!= None:
                prev = cur
                prev.size+=1
                if node.value <= cur.value:
                     cur = cur.left
                else:
                     cur = cur.right
            if node.value <= prev.value:
                prev.left = node
            else:
                prev.right = node    
    
    def get_randomnode(self):
        cur = self.root
        flag = 0
        while cur:
            val = random.randint(0, cur.size)
               
            if val == cur.size and flag:
                return cur.value
            else:
                flag = 1
                left = cur.left
                if left:
                     size = left.size
                else:
                     size = 1
                          
                if val < size:
                   cur = cur.left
                else:
                   cur = cur.right
            if not cur:
                 flag = 0
                 cur = self.root
                    
        if not cur:
            print("could not generate the random number")
            return 0  
        
    def get_randomnode_1(self):    
        index = random.randint(0, self.root.size)
        while True:
            val = get_i_node(self.root, index)
            if val != None:
                return val
        
        

                      
                 
if __name__=="__main__":
    n = int(input("what is height of tree?"))
    head = bst(n)
    lt = convert(head)
    bshead = bs_tree()
    for i in range(len(lt)):
        if lt[i]:
           bshead.insert(knode(lt[i]))
    print("Input Binary tree is ")
    pprint(bshead.root)
    while True:
        input("enter key to genearte a random number")
        print("The random value = %d" %bshead.get_randomnode())
       
        
                        
