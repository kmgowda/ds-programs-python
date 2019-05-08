from binarytree import  Node, bst, heap, pprint


def find_height(cur):
    left = 0
    right = 0
    if cur.left:
        left = find_height(cur.left)
    if cur.right:
        right = find_height(cur.right)
    if left > right:
        return left+1
    else:
        return right+1        
 
 
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



 
def find_height_it(cur):
    lt = list()
    lt.append(cur)
    height = 0
    while len(lt):
        size = len(lt)
        for i in range(size):
            tmp = lt.pop(0)
            if tmp.left:
                lt.append(tmp.left)
            if tmp.right:
                lt.append(tmp.right)
        height+=1
    return height                    
 
def level_traversal(cur):
    lt = list()
    lt.append(list())
    level = 0
    lt[level].append(cur)
    while len(lt[level]):
        size = len(lt[level])
        level +=1
        lt.append(list())
        for i in range(size):
            tmp = lt[level-1][i]
            if tmp:
               if tmp.left:
                  lt[level].append(tmp.left)
               if tmp.right:
                  lt[level].append(tmp.right)
    print("%s : level = %d" %(level_traversal.__name__, level)) 
    return lt 


def level_traversal_rec(cur, lt, level):
    if cur:
       lt[level].append(cur)
       if cur.left or cur.right:
          lt.append(list()) 
          level_traversal_rec(cur.left, lt, level+1)
          level_traversal_rec(cur.right, lt, level+1)
 
if __name__=="__main__":
    n = int(input("what is height of tree?"))
    my_bst = bst(n)
    pprint(my_bst)
    height = find_height(my_bst) 
    print("recursive : height of the tree is %d" %height)
    height = find_height_it(my_bst)
    print("iterative : height of the tree is %d" %height)
    lt= level_traversal(my_bst)
    print("Level traversal of the tree")
    for i in range(len(lt)):
        for j in range(len(lt[i])):
            print("%d " %lt[i][j].value, end="")
        print()  
    lt = list()
    lt.append(list())
    level_traversal_rec(my_bst, lt, 0)
    print("Level traversal of the tree recursive")
    for i in range(len(lt)):
        for j in range(len(lt[i])):
            print("%d " %lt[i][j].value, end="")
        print()
 
    height, bal  = find_height_bal(my_bst)
    if bal:
        print("the tree is imbalance at level %d" %height)
    else:
        print("The tree is a balanced tree and height is %d" %height)    
                                