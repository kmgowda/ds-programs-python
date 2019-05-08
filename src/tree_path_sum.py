from binarytree import  Node, tree, pprint


def paths_from_node(root, sum, runningsum,path):
    if root == None:
        return 0
    
    runningsum += root.value
   
    
    if runningsum == sum:
        path.append(root.value)
        return 1
    
    leftpaths  =  paths_from_node(root.left, sum, runningsum,path)
    if leftpaths:
        path.append(root.value) 
    rightpaths =  paths_from_node(root.right, sum, runningsum,path)
    if  rightpaths:
       path.append(root.value) 
    
    return leftpaths+rightpaths
     

def all_paths(root, sum, paths):
    if root == None:
        return 0
    path = list()
    rootpaths = paths_from_node(root, sum, 0,path)
    if rootpaths:
        paths.append(path)
    leftpaths = all_paths(root.left, sum,paths)
    rightpaths = all_paths(root.right, sum,paths)
    
    return rootpaths+leftpaths+rightpaths


if __name__=="__main__":
    n = int(input("what is height of tree?"))
    head = tree(n)
    print("The input binary tree is as follows")
    pprint(head)
    while True:
       sum = int(input("enter the value to find the all path sum"))
       pathlist = list()
       paths = all_paths(head, sum,pathlist)
       print("The number of paths for the sum %d are %d" %(sum, paths))
       print("The path elements are")
       for i in range(len(pathlist)):
             print(pathlist[i])
       