from binarytree import  Node, pprint
import random


# 0 means read, 1 means black
class RBnode(Node):
    def __init__(self, val):
        Node.__init__(self,val)
        self.col=0


class RBTree():
    def __init__(self):
        self.root = None

    def preorder(self, cur):
        if cur:
            print("%d[%d] " %(cur.value, cur.col),  end="")
            self.preorder(cur.left)
            self.preorder(cur.right)        

    def print_preorder(self, msg):
        print(msg)
        self.preorder(self.root)
        print()


    def display(self, msg):
        print(msg)
        pprint(self.root)
        self.print_preorder("Red Black tree in preorder with colors")
            
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
        if x.right and x.right.col == 0:
           cur.left = self.rightrotate(x)
        return self.leftrotate(cur)
    
    def rightleftrotate(self, cur):
        x= cur.right
        if x.left and x.left.col == 0:
           cur.right = self.leftrotate(x)           
        return self.rightrotate(cur)   
    
    def get_black_height_rec(self, cur):
        if cur == None:
           return 0
        inc = 0
        if cur.left and cur.left.col == 1:
           inc = 1
        left = self.get_black_height_rec(cur.left)+inc
 
        inc = 0
        if cur.right and cur.right.col == 1:
           inc = 1  
        right = self.get_black_height_rec(cur.right)+inc
        
        if left != right:
            print("RB tree imbalance at %d [%d]" %(cur.value, cur.col))
            
        if left > right:
            return left
        else:
            return right
    
    def get_black_height(self):
        return self.get_black_height_rec(self.root)
     
        
    def rec_insert(self, cur, newnode):
        if cur == None:
           return newnode, 2
        else:
           if newnode.value < cur.value:
              cur.left, res = self.rec_insert(cur.left, newnode)
              if res == 2:
                 if cur.col == 0 and cur.left.col == 0:
                    return cur, 3
                 else:
                    return cur, 2
              else:
                  # double red problem
                  if cur.right and cur.right.col == 0:
                     cur.right.col = 1
                     cur.left.col = 1
                     cur.col = 0
                     return cur, 2  
                  else:
                      cur = self.leftrightrotate(cur)
                      cur.col = 1
                      cur.right.col = 0
                      if cur.left: 
                          cur.left.col = 0
                      return cur, 2      
           else:
              cur.right, res = self.rec_insert(cur.right, newnode)
              if res == 2:
                 if cur.col == 0 and cur.right.col == 0:
                    return cur, 3
                 else:
                    return cur, 2
              else:
                  # double red problem
                  if cur.left and cur.left.col == 0:
                     cur.right.col = 1
                     cur.left.col = 1
                     cur.col = 0
                     return cur, 2  
                  else:
                      cur = self.rightleftrotate(cur)
                      cur.col = 1
                      cur.left.col = 0
                      if cur.right: 
                          cur.right.col = 0
                      return cur, 2      
                       
    
    def insert(self, newnode):
        self.root, res = self.rec_insert(self.root, newnode)
        if self.root:
            self.root.col = 1                                  
    
 
    def sib_red(self, parent, sib):
        if sib and sib.col == 0:
           parent.col = 0
           sib.col = 1 
           if parent.left == sib:
              return self.leftrotate(parent)
           else:
              return self.rightrotate(parent)              
        else:
            return None     
      
 
    def sib_black_all(self, parent, sib):
        if sib and sib.col == 1:
           left = sib.left
           right = sib.right
           if left:
               lcol = left.col
           else:
               lcol = 1
           if right:
               rcol = right.col
           else:
               rcol = 1
           
           if lcol and rcol:
               sib.col = 0 
               if parent.col == 0:
                   parent.col = 1
                   return 1                
               else:
                   return 2
           else:
               return 0      
        elif sib == None:
            # consider it as black
            if parent.col == 0:
                parent.col = 1
                return 1
            else:
                return 2
        else:
            return 0
  
 
    def right_sib_black_left_red(self, sib):
        if sib and sib.col == 1:
           left = sib.left
           if left:
               lcol = left.col
           else:
               lcol = 1
            
           if lcol == 0:
               sib.col = 0
               left.col = 1
               return self.leftrotate(sib)
        else:
            return None    
         
    def right_sib_black_right_red(self, parent):
        sib = parent.right
        if sib and sib.col == 1:
           right = sib.right
           if right:
               rcol = right.col
           else:
               rcol = 1
           if rcol == 0:
              sib.col = parent.col
              parent.col = 1
              right.col = 1
              return self.rightrotate(parent)
        else:
            return None      
             
    def left_sib_black_right_red(self, sib):
        if sib and sib.col == 1:
           right = sib.right
           if right:
               rcol = right.col
           else:
               rcol = 1
            
           if rcol == 0:
               sib.col = 0
               right.col = 1
               return self.rightrotate(sib)
        else:
            return None    
 
 
    def left_sib_black_left_red(self, parent):
        sib = parent.left
        if sib and sib.col == 1:
           left = sib.left
           if left:
               lcol = left.col
           else:
               lcol = 1
           if lcol == 0:
              sib.col = parent.col
              parent.col = 1
              left.col = 1
              return self.leftrotate(parent)
        else:
            return None      
    
    def left_balance(self, cur):
        tmp = self.sib_red(cur, cur.right)
        if tmp:
           cur = tmp
           parent = cur.left
        else:
           parent = cur
             
        ret = self.sib_black_all(parent, parent.right)
              
        if ret == 0:
           tmp1 = self.right_sib_black_right_red(parent)
           if tmp1:
              parent = tmp1
           else:   
              parent.right = self.right_sib_black_left_red(parent.right)
              parent = self.right_sib_black_right_red(parent)
               
        if tmp:
           cur.left = parent
        else:
           cur = parent 
              
        if ret == 2:
           return cur, 1       
           
        return cur, 0
 
        
    def right_balance(self, cur):
        tmp = self.sib_red(cur, cur.left)
        if tmp:
           cur = tmp
           parent = cur.right
        else:
           parent = cur
             
        ret = self.sib_black_all(parent, parent.left)

        if ret == 0:
           tmp1 = self.left_sib_black_left_red(parent)
           if tmp1:
              parent = tmp1
           else:   
              parent.left = self.left_sib_black_right_red(parent.left)
              parent = self.left_sib_black_left_red(parent)
  
        if tmp:
           cur.right = parent
        else:
           cur = parent 
              
        if ret == 2:
           return cur, 1       
           
        return cur, 0           
 
    def rec_delete(self, cur,val):
        if cur == None:
            return None, 3
        
        if val < cur.value:
           cur.left, res =  self.rec_delete(cur.left, val)
           if res == 1:
              cur, res = self.left_balance(cur)
           return cur, res   
        elif val > cur.value:
           cur.right, res = self.rec_delete(cur.right, val)
           if res == 1:
              cur, res = self.right_balance(cur)
           return cur, res   
        else:
            res = cur.col
            if cur.left == None and cur.right == None:
                del cur
                return None, res
            elif cur.left == None:
                tmp = cur.right
                if cur.col == 1  and tmp.col == 0:
                   tmp.col = 1
                   res = 0 
                del cur
                return tmp, res
            elif cur.right == None:
                tmp = cur.left
                if cur.col == 1  and tmp.col == 0:
                   tmp.col = 1
                   res = 0 
                del cur
                return tmp, res
            else:
                tmp = cur.right
                while tmp.left != None:
                      tmp = tmp.left
                cur.value = tmp.value
                cur.right, res = self.rec_delete(cur.right, tmp.value)
                if res == 1:
                   cur, res = self.right_balance(cur)
                return cur, res   

    def delete(self, val):
        if self.root == None:
            print("Empty Tree")
            return 
        self.root, res= self.rec_delete(self.root, val)
        if res == 3:
            print("The input value %d is not found in the tree" %val)    
        if self.root and self.root.col == 0:
            print("root showing red color ,changeing it black")
            self.root.col = 1 
 
 

         
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
    rb= RBTree()
    for i in range(N):
        #print("Inserting ... %d" %lt[i])
        bt.insert(Node(lt[i]))
        rb.insert(RBnode(lt[i]))
        #rb.display("Red Black tree at iteration %d" %i)
        #print(".........................")
        #print()
 
               
    bt.display("The input Binary Tree is as follows")
    rb.display("The Read Back tree is as follows")
    height = rb.get_black_height()
    print("The Black height of the tree is %d" %height)
    while 1:
       item=int(input("Enter the node value to remove"))
       rb.delete(item)
       rb.display("The Red Black tree afer the node removal")
       height = rb.get_black_height()
       print("The Black height of the tree is %d" %height)    
