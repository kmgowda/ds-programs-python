from binarytree import  Node, pprint,bst
import random


def merge_list(left,root,right):
    if 0:
       if left:
          l = left.value
       else:
          l = 0
       if root:
          r = root.value
       else:
          r = 0 
       if right:
          rh = right.value
       else:
          rh =0
       print("%d %d %d" %(l,r,rh))                       

    if left:
       first = left
       tmp = first
       while tmp.right:
           tmp = tmp.right
       if root:
          tmp.right = root 
          root.left = tmp
          root.right = right
          tmp = root
       else:
          tmp.right = right
 
       if right:
           right.left = tmp      
    elif root:
         first = root    
         root.right = right
         if right:
            right.left = root   
    else:
        first = right
            
    return first


def convert_ll(root):
    if root:
       left = convert_ll(root.left)
       right = convert_ll(root.right)
       first = merge_list(left,root,right)
       return first
    else:
       return root 


def merge_list_1(lf, ll, rf, rl, root):
    if 0:
       if lf:
          l1 = lf.value
       else:
          l1 = 0
       if ll:
          l2 = ll.value
       else:
          l2 = 0 
       if rf:
          r1 = rf.value
       else:
          r1 = 0
       if rl:
          r2 = rl.value
       else:
          r2 = 0        
       if root:
          r = root.value
       else:
          r = 0 
       print("lf= %d , ll=%d , root = %d  , rf = %d , rl =%d" %(l1,l2, r, r1,r2))               
    
    if not lf:
        if not ll:
            lf = root
            ll = lf
        else:
            lf = ll
    elif not ll:
        ll = lf
    
    if lf == root:
        root.left = None
    else:
        ll.right = root
        root.left = ll
        
    root.right = rf
    
    if rf :
        rf.left = root
    else:
        rf = root    
    
    if not rl:
        rl = rf
    return lf, rl        
                
 
def convert_ll_1(root):
    if root:
        lf, ll = convert_ll_1(root.left)
        rf, rl = convert_ll_1(root.right)
        first, last = merge_list_1(lf,ll,rf,rl, root)
        return first, last
    else:
        return root,root   
                 

if __name__=="__main__":
    print("program to generate the doubly linked list from the binary search trees")
    ht = int(input("Enter the height of the binary search tree"))
    root = bst(ht)
    print("Input binary search tree")
    pprint(root)
    if 0:
       first = convert_ll(root)
    else:
        first , last =  convert_ll_1(root)  
    if not first:
        print("None is returned as first")
    print("The doubly linked list is as follows")
    tmp = first
    last = tmp
    while tmp:
        if tmp.right:
            print("%d ->" %tmp.value, end="")
        else:
            print("%d" %tmp.value)
        last = tmp    
        tmp = tmp.right
        
    print("The doubly linked list from last")
    tmp = last    
    while tmp:
        if tmp.left:
            print("%d ->" %tmp.value, end="")
        else:
            print("%d" %tmp.value)
        tmp = tmp.left                 
    