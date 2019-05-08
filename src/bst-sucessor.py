from binarytree import  Node, bst,  pprint, convert

class knode(Node):
      def __init__(self, val):
          Node.__init__(self, val)
          self.parent = None

def inorder(cur):
    if cur:
        inorder(cur.left)
        print("%d " %cur.value , end="")
        inorder(cur.right) 
             

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
            node.parent = prev    

    def find(self, val):
        if self.root:
            cur = self.root
            while cur:
                if cur.value == val:
                    return cur
                elif cur.value < val:
                    cur = cur.right
                else:
                    cur = cur.left 
            return cur          
        else:
            return None    

    def find_sucessor(self, cur):
        if cur:
            if cur.right:
                cur = cur.right
                while cur.left:
                    cur = cur.left
                return cur
            else:
                prev = cur.parent
                while prev and  prev.left != cur:
                      cur = prev
                      prev = prev.parent
                return prev    
        else:
            return cur     

    def display(self, msg):
        print(msg)
        pprint(self.root)
  
        
if __name__=="__main__":
    n = int(input("what is height of tree?"))
    my_bst = bst(n)
    lst = convert(my_bst)
    bt = BinarySearchTree()
    for i in range(len(lst)):
        if lst[i] != None:
           bt.insert(knode(lst[i]))
    bt.display("The input tree is ")
    print("The inoder traversal is as follows")
    inorder(bt.root)
    print()
    while 1:
        val = int(input("Enter the value to find the inorder sucessor"))
        cur = bt.find(val)
        if cur:
            nxt = bt.find_sucessor(cur)
            if nxt:
                print("The inorder successor of %d is %d" %(cur.value, nxt.value))
            else:
                print("There is No inorder successor of %d " %cur.value) 
        else:
            print("The value %d not found in the tree" %cur.value)
                       
            
    
        
        

          