from binarytree import  Node, pprint
import random


class SplayTree():
    def __init__(self):
        self.root = None

    def display(self, msg):
        print(msg)
        pprint(self.root)

            
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
        cur.left = self.rightrotate(cur.left)
        return self.leftrotate(cur)
 
    def rightleftrotate(self, cur):
        cur.right = self.leftrotate(cur.right)           
        return self.rightrotate(cur)   
    
    def leftleftrotate(self, cur):
        cur = self.leftrotate(cur) 
        return self.leftrotate(cur)
    
    def rightrightrotate(self,cur):
        cur = self.rightrotate(cur)
        return self.rightrotate(cur)
        
        
    def rec_insert(self, cur, newnode):
        if cur == None:
           return newnode, 0
        else:
           if newnode.value < cur.value:
              cur.left, res = self.rec_insert(cur.left, newnode)
              if res == 0:
                  return cur, 1
              elif res == 1:
                  cur=self.leftleftrotate(cur)
                  return cur, 0
              else:
                  cur = self.leftrightrotate(cur)
                  return cur, 0
                  
           else:
              cur.right, res = self.rec_insert(cur.right, newnode)
              if res == 0:
                 return cur, -1
              elif res == -1:
                  cur=self.rightrightrotate(cur)
                  return cur, 0
              else:
                  cur = self.rightleftrotate(cur)
                  return cur, 0              
        
                
    
    def insert(self, newnode):
        self.root, res = self.rec_insert(self.root, newnode) 
        if res == 1:
            self.root = self.leftrotate(self.root)
        elif res == -1:
            self.root = self.rightrotate(self.root)
        else:
            print("res = %d , first node %d is inserted" %(res, self.root.value))                                                         
    
    
    def rec_find(self, cur, val):
        if cur == None:
            return None, -3
        if val < cur.value:
            cur.left, res = self.rec_find(cur.left, val)
            if res == 0:
               return cur, 1
            elif res == 1:
               cur=self.leftleftrotate(cur)
               return cur, 0
            else:
               cur = self.leftrightrotate(cur)
               return cur, 0
        elif val > cur.value:
            cur.right, res = self.rec_find(cur.right, val)       
            if res == 0:
               return cur, -1
            elif res == -1:
                cur=self.rightrightrotate(cur)
                return cur, 0
            else:
                cur = self.rightleftrotate(cur)
                return cur, 0
        else:
            return cur, 0                    


    def find(self,cur, val):
        cur, res = self.rec_find(cur, val) 
        if res == 1:
            cur = self.leftrotate(cur)
            res = 0
        elif res == -1:
            cur = self.rightrotate(cur)
            res = 0
        elif res == -3:
            print("res = %d , the value %d not found" %(res, val))
        return cur, res     


    def rec_find_right_max(self, cur):
        if cur.right == None:
           return cur, 0
        cur.right, res = self.rec_find_right_max(cur.right)
        if res == 0:
            return cur, -1
        else:
            cur = self.rightrightrotate(cur) 
            return cur, 0
    
    def find_right_max(self, cur):
        cur, res = self.rec_find_right_max(cur)
        if res == -1:
            cur = self.rightrotate(cur)
        return cur      


    def delete(self, val):
        self.root, res= self.find(self.root, val)
        if res != -3:
           left = self.root.left
           right = self.root.right
           del self.root
           if left:
              if right:
                 left = self.find_right_max(left)
                 self.root = left
                 self.root.right = right
              else:
                  self.root = left   
           else:
               self.root = right

         
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
    sp= SplayTree()
    for i in range(N):
        print("Inserting ... %d" %lt[i])
        bt.insert(Node(lt[i]))
        sp.insert(Node(lt[i]))
        sp.display("Splay tree at iteration %d" %i)
        print(".........................")
        print()
        #input()
 
               
    bt.display("The input Binary Tree is as follows")
    sp.display("The splay tree is as follows")

    while 1:
       item=int(input("Enter the node value to remove"))
       sp.delete(item)
       sp.display("The Splay tree afer the node removal")  

           