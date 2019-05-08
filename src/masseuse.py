import random


def max_order(ar, index, n, order,memo):
    if index >= n:
        return 0
    if index < len(memo):
        return memo[index]
    t1 = ar[index]+max_order(ar,index+2,n,order,memo)
    t2 = max_order(ar,index+1,n,order,memo)
    if t1 > t2:
        memo.append(t1)
        if index not in order: 
           order.append(index)
        if index+1 in order:
           order.remove(index+1)    
    else:
        memo.append(t2)
        if index in order: 
           order.remove(index)
        if index+1 not in order: 
           order.append(index+1)                 
    return memo[-1] 
    


if __name__=="__main__":
    print("Python program to print the maximum service order for masseuse")
    N=int(input("How many continues requests?"))
    ar = random.sample(range(10,100),N)
    print("The input order is")
    print(ar)
    order = list()
    memo = list()
    max=max_order(ar,0,len(ar),order,memo)
    print("The max order is %d" %max)
    print("Massage sequence are")
    for index in order:
        print("%d " %ar[index], end="")
    print()    
    
    
 