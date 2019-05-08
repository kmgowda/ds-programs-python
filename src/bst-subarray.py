from binarytree import  Node, bst, pprint

def wavelist(left, right, wave, prefix):
    lt = len(left)
    rt = len(right)

    if lt == 0 or rt == 0:
        tmp = list()
        tmp.extend(prefix)
        for i in range(lt):
           tmp.append(left[i])
        for i in range(rt): 
           tmp.append(right[i])
        wave.extend(tmp)
        return
   
    if lt:
        first = left.pop(0)
        prefix.append(first)
        wavelist(left, right, wave, prefix)
        prefix.pop()
        left.insert(0, first)
     
    if rt:   
        first = right.pop(0)
        prefix.append(first)
        wavelist(left, right, wave, prefix)
        prefix.pop()
        right.insert(0, first)       
       


def allarry(root):
    result = list()   
    if root == None:
       return result
    
    prefix = list()
    prefix.append(root.value)
    
    left = allarry(root.left)
    right = allarry(root.right)
    wave = list()
    wavelist(left, right, wave, prefix)
    result.extend(wave)
    return result

def wavelist_list(first, second, wave, prefix):
    if first:
       fl = len(first)
    else:
        fl = 0
    
    if second:       
       sl = len(second)
    else:
        sl = 0   
    if fl == 0 or sl == 0:
        tmp = list()
        tmp.extend(prefix)
        if first:
           tmp.extend(first)
        if second:   
           tmp.extend(second)
        wave.append(tmp)
        return
    
    if fl:
        fitem = first.pop(0)
        prefix.append(fitem)
        wavelist_list(first, second, wave, prefix)
        prefix.pop()
        first.insert(0, fitem)

    if sl:
        fitem = second.pop(0)
        prefix.append(fitem)
        wavelist_list(first, second, wave, prefix)
        prefix.pop()
        second.insert(0, fitem)        
        


def allsequences(root):
    result = list()
    if root == None:
       return result
    
    prefix = list()
    prefix.append(root.value)
    
    leftseq = allsequences(root.left)
    rightseq = allsequences(root.right)
    lseq = len(leftseq)
    rseq = len(rightseq)
        
    if lseq and rseq:
        for i in range(lseq):
            for j in range(rseq):
                wave = list()
                wavelist_list(leftseq[i], rightseq[j], wave, prefix)
                for k in range(len(wave)):
                    result.append(wave[k])
   
    elif lseq:
        for i in range(lseq):
            wave = list()
            wavelist_list(leftseq[i], None, wave, prefix)
            for k in range(len(wave)):
                result.append(wave[k])

    elif rseq:
        for j in range(rseq):
            wave = list()
            wavelist_list(None, rightseq[j], wave, prefix)
            for k in range(len(wave)):
                result.append(wave[k])
    else:
        result.append(prefix) 
             
    return result
    



def find_elements(root):
    lz =rz = 0
    if root:
        if root.left:
            lz = find_elements(root.left)
        if root.right:
            rz = find_elements(root.right)
        return lz+rz+1
        
        
if __name__=="__main__":
    n = int(input("what is height of tree?"))
    my_bst = bst(n)
    pprint(my_bst)
#    size = find_elements(my_bst)
#    print("The number of elements in the array is %d " %size)
    #rootarry = list()
    #rootarry = allarry(my_bst)
    #index = 0
    #count  = 1
    #ln = len(rootarry)
    #print("The all possible array elements are")
    #while index < ln:
    #    print("set %d:" %count, rootarry[index:index+size])
    #    index +=size
    #    count +=1
    #print(rootarry)
    print("Another Method")
    seq = allsequences(my_bst)
    print("All sequences")
    for i in range(len(seq)):
        print("set %d = " %(i+1), end="")
        print(seq[i])
  
