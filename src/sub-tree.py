from binarytree import  Node, bst, pprint, convert


def preorder(root, lt):
    if root == None:
        lt.append(None)
    else:
        lt.append(root.value)
        preorder(root.left, lt)
        preorder(root.right, lt)    

def lt_comp(lt1, lt2):
    l1 = len(lt1)
    l2 = len(lt2)
     
    for i in range(l1-l2+1):
        for j in range(l2-1, -1, -1):
            if lt1[i+j]!= lt2[j]:
               break
        if not j:
            return i 
    return -1 


def is_sub_tree(root1, root2):
    lt1 = list()
    preorder(root1, lt1)
    lt2 = list()
    preorder(root2, lt2)
    res= lt_comp(lt1, lt2)
    if res != -1:
        return True
    else:
        return False


def match_tree(root1, root2):
    if root1 == None and root2 == None:
       return True
    if root1.value != root2.value:
        return False
    else:
        return  match_tree(root1.left, root2.left) and match_tree(root1.right, root2.right)
    

def rec_is_subtree(root1, root2):
    if root2 == None or root1 == None:
        return False
    if root1.value == root2.value:
        return True and  match_tree(root1.right, root2.right)
    else:
        return rec_is_subtree(root1.left, root2) or rec_is_subtree(root1.right, root2)
    

class BStree:
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

if __name__=="__main__":
    n = int(input("what is height of tree?"))
    head1 = bst(n)
    pprint(head1)
    size = int(input("Enter the number of elements to create a subtree"))
    subt = BStree()
    for i in range(size):
        val =int(input("enter the node %d value" %(i+1)))
        subt.insert(Node(val))
    
    print("The input sub stree is")
    pprint(subt.root)
    if is_sub_tree(head1, subt.root):
        print("The tree headed %d is sub tree of the tree headed %d" %(subt.root.value, head1.value))
    else:
        print("The tree headed %d is NOT a sub tree of the tree headed %d" %(subt.root.value, head1.value)) 
    if rec_is_subtree(head1, subt.root):
        print("Recursion: The tree headed %d is sub tree of the tree headed %d" %(subt.root.value, head1.value))
    else:
        print("Recursion: The tree headed %d is NOT a sub tree of the tree headed %d" %(subt.root.value, head1.value)) 
        
               