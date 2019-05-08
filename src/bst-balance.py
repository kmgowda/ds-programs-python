from binarytree import  Node, bst,  pprint


def find_height_bal(cur):
    left = 0
    right = 0

    if cur.left:
        left, bal = find_height_bal(cur.left)
        if bal:
            return left, bal
    if cur.right:
        right, bal = find_height_bal(cur.right)
        if bal:
            return right, bal

    if abs(left-right)  > 1:
        bal = 1
    else:
        bal = 0    
    
    if left > right:
       return left+1, bal
    else:
       return right+1, bal 
 
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

    def display(self, msg):
        print(msg)
        pprint(self.root)



if __name__=="__main__":
    print("Python program to create the Binary search Tree")
    N= int(input("How many elements?"))
    bst = BinarySearchTree()
    for i in range(N):
        val = int(input("Enter element %d " %(i+1)))
        bst.insert(Node(val))
    bst.display("Tree elements are")
    height, bal  = find_height_bal(bst.root)
    if bal:
        print("the tree is imbalance at level %d" %height)
    else:
        print("The tree is a balanced tree and height is %d" %height)              