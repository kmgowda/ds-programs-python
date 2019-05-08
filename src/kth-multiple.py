
def get_kth_multiples(K):
    lt = set()
    for i in range(0,K):
        pow3=3**i
        for j in range(0,K):
            pow5=5**j
            for x in range(0,K):
                pow7=7**x
                val = pow3*pow5*pow7
                lt.add(val)
    return lt


def get_kth_multi(K):
    lt = list()
    lt.append(1)
    lt.append(3)
    lt.append(5)
    lt.append(7)
    
    for i in range(K):
        val = lt[i]
        tmp = 3*val
        if tmp not in lt:
             lt.append(tmp)
        tmp = 5*val
        if tmp not in lt:
             lt.append(tmp)             
        tmp = 7*val
        if tmp not in lt:
             lt.append(tmp)            
    return lt    
 
if __name__=="__main__":
    print("Python program to print kth multiple of 3 , 5, and 7")
    K= int(input("enter the value for K"))
    lt= get_kth_multiples(K)
    tmp = sorted(lt)
    print("The Kth multiples are")
    for i in range(len(tmp)):
        print("%6d  : %d" %(i+1, tmp[i]))
    lt =  get_kth_multi(K)
    lt.sort()
    print("Method 2: The Kth multiples are")
    for i in range(len(lt)):
        print("%6d  : %d" %(i+1, lt[i]))    
       
      


            
    