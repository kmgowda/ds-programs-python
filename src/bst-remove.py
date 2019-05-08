from binarytree import Node, pprint
import random

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
    
    def rec_delete(self, cur,val):
        if cur == None:
            return None
        if val < cur.value:
            cur.left =  self.rec_delete(cur.left, val)
            return cur
        elif val > cur.value:
            cur.right = self.rec_delete(cur.right, val)
            return cur
        else:
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
                return cur
               
     
    def delete(self, val):
        return self.rec_delete(self.root, val) 
               
    def display(self, msg):
        print(msg)
        pprint(self.root)
    
    def rec_inorder(self, cur, lt):
        if cur != None:
            self.rec_inorder(cur.left, lt)
            lt.append(cur.value)
            self.rec_inorder(cur.right, lt)
                
    def inorder(self, msg):
        print(msg)
        lt = list()
        self.rec_inorder(self.root, lt)
        size = len(lt)
        for i in range(size-1):
            print("%d->" %lt[i], end="")
        print("%d" %lt[-1])    
    
    def rec_preorder(self, cur):
        if cur != None:
            print("%d " %cur.value, end="")
            self.rec_preorder(cur.left)
            self.rec_preorder(cur.right)
            
    def preorder(self, msg):
        print(msg)            
        self.rec_preorder(self.root)
        print()
        
    
    def rec_postorder(self, cur):
        if cur != None:
            self.rec_postorder(cur.left)
            self.rec_postorder(cur.right)
            print("%d " %cur.value, end="")
   
    
    def postporder(self, msg):
        print(msg)     
        self.rec_postorder(self.root)
        print() 
                                                      
     
    def print_tree(self, msg):
        print(msg)
        lt = list()
        lt.append(self.root)
        i = 0
        while i < len(lt):
            node = lt[i]
            if node.left:
                lt.append(node.left)
            if node.right:
                lt.append(node.right)
            print(node.value)    
            i+=1

if __name__=="__main__":
    print("program to generate the AVL trees")
    N = int(input("How many numbers?"))
    lt = random.sample(range(1, 1000), N)
    print(lt)
    bt1 = BinarySearchTree()
    bt2 = BinarySearchTree()
    for i in range(N):
        bt1.insert(Node(lt[i]))
        bt2.insert(Node(lt[i]))
             
    bt1.display("The input Binary Tree is as follows")
    val = int(input("Enter the node value to remove"))
    bt1.remove(val)
    bt1.display("Method 1 : Binary Tree after the node removal")
    bt2.delete(val)
    bt2.display("Method 2 : Binary Tree after the node removal")
   
            