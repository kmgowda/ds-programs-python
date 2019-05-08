from binarytree import Node, pprint

class dnode(Node):
    def __init__(self, val):
       Node.__init__(self, val)
       self.depth = 0
           
      
class BStree:
    def __init__(self):
      self.root = None
    
    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            cur = self.root
            prev = cur
            depth = 0
            while cur!= None:
                if node.value <= cur.value:
                    prev = cur
                    cur = cur.left
                else:
                    prev= cur
                    cur = cur.right
                depth +=1
            node.depth = depth        
            if node.value <= prev.value:
                prev.left = node
            else:
                prev.right = node
                
    def display(self, msg):
        print(msg)
        pprint(self.root)
    
    def print_tree(self, msg):
        print(msg)
        lt = list()
        lt.append(self.root)
        pd =self.root.depth
        i = 0
        while i < len(lt):
            node = lt[i]
            if node.left:
                lt.append(node.left)
            if node.right:
                lt.append(node.right)
            if pd != node.depth:
               print()    
               pd = node.depth
            print("%d " %node.value , end="") 
            i+=1                     
 
if __name__=="__main__":
   print("Python program to Binary search tree level traversal")
   N = int(input("How many elements?"))
   bst= BStree()
   for i in range(N):
       val = int(input("Enter the value for the element %d" %(i+1)))
       bst.insert(dnode(val))
   bst.display("Input Binary tree is as follows") 
   bst.print_tree("Input binary tree in level order ")     
                            