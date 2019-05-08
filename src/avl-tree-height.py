from binarytree import  Node, pprint
import random


class AVLnode(Node):
    def __init__(self, val):
        Node.__init__(self,val)
        self.height=1


class AVLTree():
    def __init__(self):
        self.root = None

    def get_bfactor(self, cur):
        if cur.left:
           lh = cur.left.height
        else:
           lh = 0
            
        if cur.right:
           rh = cur.right.height
        else:
           rh = 0            
        
        return lh-rh
     
    def update_height_bfactor(self, cur):
        if cur.left:
           lh = cur.left.height
        else:
           lh = 0
            
        if cur.right:
           rh = cur.right.height
        else:
           rh = 0
           
        if lh > rh:
            cur.height = lh+1
        else:
            cur.height = rh+1
        return lh-rh                                   

    def preorder(self, cur):
        if cur:
            print("%d[%d] " %(cur.value, cur.height),  end="")
            bfactor = self.get_bfactor(cur)
            if bfactor != 0 and bfactor != 1 and bfactor != -1:
               print("AVL tree imbalance at %d [%d]" %(cur.value, cur.height)) 
            self.preorder(cur.left)
            self.preorder(cur.right)        

    def print_preorder(self, msg):
        print(msg)
        self.preorder(self.root)
        print()


    def display(self, msg):
        print(msg)
        pprint(self.root)
        self.print_preorder("AVL Tree in preorder with bfactors")
            
    def leftrotate(self, cur):
        x = cur.left
        cur.left = x.right
        x.right = cur
        self.update_height_bfactor(cur)
        self.update_height_bfactor(x)
        return x
    
    def rightrotate(self, cur):
        x = cur.right 
        cur.right = x.left
        x.left = cur
        self.update_height_bfactor(cur)
        self.update_height_bfactor(x)
        return x           

    def leftrightrotate(self, cur):
        x = cur.left
        x_bfactor = self.get_bfactor(x)        
        if x_bfactor == -1:
           cur.left = self.rightrotate(x)
        return self.leftrotate(cur)
 
    def rightleftrotate(self, cur):
        x= cur.right
        x_bfactor = self.get_bfactor(x)
        if x_bfactor == 1:
           cur.right = self.leftrotate(x)           
        return self.rightrotate(cur)   
    
    def get_height_rec(self, cur):
        if cur == None:
           return 0
        left = self.get_height_rec(cur.left)+1
        right = self.get_height_rec(cur.right)+1
        bfactor = left-right
        if bfactor != 0 and bfactor != 1 and bfactor != -1:
            print("AVL tree imbalance at %d [%d]" %(cur.value, cur.height))
            
        if left > right:
            return left
        else:
            return right
    
    def get_height(self):
        return self.get_height_rec(self.root)
    
    
    def balance_tree(self, cur): 
        bfactor = self.update_height_bfactor(cur)
        if bfactor == 0:
           return cur, False
        elif bfactor == 2:
           cur = self.leftrightrotate(cur)
           return cur, False
        elif bfactor == -2:
           cur = self.rightleftrotate(cur)
           return cur, False
        return cur, True 
 
        
        
    def rec_insert(self, cur, newnode):
        if cur == None:
           return newnode, True
        else:
           if newnode.value < cur.value:
              cur.left, res = self.rec_insert(cur.left, newnode)
           else:
              cur.right, res = self.rec_insert(cur.right, newnode)
           
           if res:
              cur, res = self.balance_tree(cur)
           return cur, res 
         
                
    
    def insert(self, newnode):
        self.root, res = self.rec_insert(self.root, newnode)                                  
    

    def rec_delete(self, cur,val):
        if cur == None:
            return None
        if val != cur.value:
            if val < cur.value:
               cur.left =  self.rec_delete(cur.left, val)
            elif val > cur.value:
               cur.right = self.rec_delete(cur.right, val)
            cur, res = self.balance_tree(cur)
 
            return cur
        else:
            #print("Found the node with value %d" %cur.value)
            if cur.left == None and cur.right == None:
                del cur
                return None
            elif cur.left == None:
                tmp = cur.right
                del cur
                return tmp
            elif cur.right == None:
                tmp = cur.left
                del cur
                return tmp
            else:
                tmp = cur.right
                while tmp.left != None:
                      tmp = tmp.left
                cur.value = tmp.value
                cur.right = self.rec_delete(cur.right, tmp.value)
                cur, res = self.balance_tree(cur) 
                return cur

    def delete(self, val):
        self.root= self.rec_delete(self.root, val) 

         
class BinarySearchTree:
    def __init__(self):
        self.root = None 
    
    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            prev = cur
            while cur!= None:
                if node.value <= cur.value:
                    prev = cur
                    cur = cur.left
                else:
                    prev= cur
                    cur = cur.right
            if node.value <= prev.value:
                prev.left = node
            else:
                prev.right = node
     
    def remove(self, val):
        cur = self.root
        prev = self.root
        while cur != None and prev!= None:
            if cur.value == val:
               # found the node to be deleted  
               tmp = cur
               
               # balance the tree
               if tmp.left != None:
                  cur = tmp.left 
                  nxt = cur
                  while nxt.right != None:
                      nxt = nxt.right
                  nxt.right = tmp.right
               else:
                   cur = tmp.right
                      
               if tmp == self.root:
                   if self.root.left:
                       self.root = self.root.left
                   else:
                       self.root = self.root.right
               elif tmp == prev.left:
                   prev.left = cur
               else:
                   prev.right = cur      
               del tmp
               prev = None
            elif cur.value < val:
                prev = cur
                cur = cur.right
            else:
                prev = cur
                cur = cur.left
        return prev 
                
    def display(self, msg):
        print(msg)
        pprint(self.root)
        
if __name__=="__main__":
    print("program to generate the AVL trees")
    N = int(input("How many numbers?"))
    lt = random.sample(range(1, 1000), N)
    print(lt)
    bt = BinarySearchTree()
    av= AVLTree()
    for i in range(N):
        #print("Inserting ... %d" %lt[i])
        bt.insert(Node(lt[i]))
        av.insert(AVLnode(lt[i]))
        #av.display("AVL tree at iteration %d" %i)
        #print(".........................")
        #print()
 
               
    bt.display("The input Binary Tree is as follows")
    av.display("The AVL tree is as follows")
    height = av.get_height()
    print("The height of the tree is %d" %height)
    while 1:
       item=int(input("Enter the node value to remove"))
       av.delete(item)
       av.display("The AVL tree afer the node removal")  
       height = av.get_height()
       print("The height of the tree is %d" %height)  
           