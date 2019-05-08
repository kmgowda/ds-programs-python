from binarytree import  Node, bst, pprint, convert
import random

def bst_min_insert(a, min, max):
    if min <= max:
       mid = (min+max)//2
       n = Node(a[mid])
       n.left = bst_min_insert(a, min, mid-1)
       n.right = bst_min_insert(a, mid+1, max)
       return n
    else:
        return None

if __name__=="__main__":
    print("Create the Binary try with minimal for sorted array/list")
    N = int(input("How many numbers?"))
    a = random.sample(range(100), N)
    a.sort()
    print("The sorted %d random numbers are " %N)
    print(a)
    bst = convert(a)
    min = bst_min_insert(a, 0, len(a)-1)
    print("The Binary search tree")
    pprint(bst)
    print("The binary search tree with minimal height")
    pprint(min)
