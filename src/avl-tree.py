from binarytree import  Node, pprint
import random


class AVLnode(Node):
    def __init__(self, val):
        Node.__init__(self,val)
        self.bfactor=0


class AVLTree():
    def __init__(self):
        self.root = None

    def preorder(self, cur):
        if cur:
            print("%d[%d] " %(cur.value, cur.bfactor),  end="")
            if cur.bfactor != 0 and cur.bfactor != 1 and cur.bfactor != -1:
               print("AVL tree imbalance at %d [%d]" %(cur.value, cur.bfactor)) 
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
        return x
    
    def rightrotate(self, cur):
        x = cur.right 
        cur.right = x.left
        x.left = cur
        return x           

    def leftrightrotate(self, cur):
        x = cur.left
        if x.bfactor == -1:
           cur.left = self.rightrotate(x)
        return self.leftrotate(cur)
 
    def rightleftrotate(self, cur):
        x= cur.right
        if x.bfactor == 1:
           cur.right = self.leftrotate(x)           
        return self.rightrotate(cur)   
    
    def get_height_rec(self, cur):
        if cur == None:
           return 0
        left = self.get_height_rec(cur.left)+1
        right = self.get_height_rec(cur.right)+1
        cur.bfactor = left-right
        if cur.bfactor != 0 and cur.bfactor != 1 and cur.bfactor != -1:
            print("AVL tree imbalance at %d [%d]" %(cur.value, cur.bfactor))
            
        if left > right:
            return left
        else:
            return right
    
    def get_height(self):
        return self.get_height_rec(self.root)
     
        
    def rec_insert(self, cur, newnode):
        if cur == None:
           return newnode, True
        else:
           if newnode.value < cur.value:
              cur.left, res = self.rec_insert(cur.left, newnode)
              if res:
                 if cur.bfactor == 0:
                    cur.bfactor = 1
                 elif cur.bfactor == -1:
                      cur.bfactor = 0
                      res = False
                 else:
                      #self.display("Invoking leftrightrotate at node %d" %cur.value)
                      cur = self.leftrightrotate(cur)
                      self.get_height_rec(cur)
                      res = False
           else:
              cur.right, res = self.rec_insert(cur.right, newnode)
              if res:
                 if cur.bfactor == 0:
                    cur.bfactor = -1
                 elif cur.bfactor == 1:
                      cur.bfactor = 0
                      res = False
                 else:
                      #self.display("Invoking rightleftrotate at node %d" %cur.value)
                      cur = self.rightleftrotate(cur) 
                      self.get_height_rec(cur)                  
                      res = False
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
 
            h = self.get_height_rec(cur)
            if cur.bfactor != 0 and cur.bfactor != 1 and cur.bfactor != -1:
               print("AVL tree is imbalance at %d [%d]" %(cur.value, cur.bfactor))
               if cur.bfactor < -1:
                  #self.display("Invoking rightlefrotate at node %d [%d]" %(cur.value, cur.bfactor)) 
                  cur = self.rightleftrotate(cur)
               else:
                  #self.display("Invoking leftrightrotate at node %d [%d]" %(cur.value, cur.bfactor)) 
                  cur = self.leftrightrotate(cur)
               #self.display("AVL tree after the rotation")       
               h = self.get_height_rec(cur)
               
               if cur.bfactor != 0 and cur.bfactor != 1 and cur.bfactor != -1:
                  print("AVL tree is imbalance even after rotation at %d [%d]" %(cur.value, cur.bfactor))
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
                h = self.get_height_rec(cur)
                if cur.bfactor != 0 and cur.bfactor != 1 and cur.bfactor != -1:
                   print("1 AVL tree is imbalance at %d [%d]" %(cur.value, cur.bfactor))
                   if cur.bfactor < -1:
                      #self.display("1 Invoking rightlefrotate at node %d [%d]" %(cur.value, cur.bfactor)) 
                      cur = self.rightleftrotate(cur)
                   else:
                      #self.display("1 Invoking leftrightrotate at node %d [%d]" %(cur.value, cur.bfactor)) 
                      cur = self.leftrightrotate(cur)    
                      
                   #self.display("1 AVL tree after the rotation")
                   h = self.get_height_rec(cur)
                  
                   if cur.bfactor != 0 and cur.bfactor != 1 and cur.bfactor != -1:
                      print("1 AVL tree is imbalance even after rotation at %d [%d]" %(cur.value, cur.bfactor))
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
#    height = av.get_height()
#    print("The height of the tree is %d" %height)
    while 1:
       item=int(input("Enter the node value to remove"))
       av.delete(item)
       av.display("The AVL tree afer the node removal")  
       height = av.get_height()
       print("The height of the tree is %d" %height)  
           