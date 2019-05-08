from binarytree import  Node, tree,  pprint

def find_anscestor(root, val1, val2):
    
    if root == None:
        return None, False
    
    if root.value == val1 and root.value == val2:
        return root, True
    
    left, res = find_anscestor(root.left, val1, val2)
    if res:
        return left, res
    right, res = find_anscestor(root.right, val1, val2)
    if res:
        return right, res
    
    if left and right:
        return root, True
    elif root.value == val1 or root.value == val2:
        if left or right:
            return root, True
        else:
            return root, False
    else:
        if left:
            return left, False
        elif right:
            return right, False
        else:
            return None, False
                
 
if __name__=="__main__":
    print("Python program to find the common ancestor of a tree")
    n = int(input("what is height of tree?"))
    my_tree = tree(n)
    print("The random tree of level %d" %n)
    pprint(my_tree)
    while 1:
        val1 = int(input("enter the value 1:"))
        val2 = int(input("enter the value 2:"))
        ans, res = find_anscestor(my_tree, val1, val2)
        if res:
            print("The common anscestor of %d and %d is %d" %(val1, val2, ans.value))
        else:
            print("The common anscestor not found")    
           
    
