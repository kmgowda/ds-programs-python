import random

def heapify(a,N):
    min = a[0]
    pos = 0
    for i in range(N//2,-1,-1):
        c = i*2+1
        if c+1 < N and a[c+1] < a[c]:
            t = c+1
        else:
            t = c
        if t < N and a[t] < min:
            pos = t
            min = a[pos]
  
    a[pos] = a[0]
    a[0] = min
    
def small_k_heap(a, N, k):
    for i in range(N, N-k,-1):
         heapify(a, i)
         tmp = a[0]
         a[0]= a[i-1]
         a[i-1]=tmp 

def print_bottom_k(a,N,k):
    print("The smallest %d numbers are " %k)
    for i in range(N-1, N-k-1,-1):
        print("%d " %(a[i]), end="")
    print()    

def print_top_k(a,N,k):
    print("The smallest %d numbers are " %k)
    for i in range(0, k):
        print("%d " %(a[i]), end="")
    print()    


def partition(a,l,h):
    i = l
    j = h
    while i < j:
        while i < h and a[l] >= a[i]:
            i+=1
        while j > l and a[j] > a[l]:
            j-=1
        if i < j:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
    tmp = a[l]
    a[l] = a[j]
    a[j] = tmp 
    return j

def small_quick(a, l,h, k):
    if  l < h:
        p =  partition(a,l,h)
#        print("pivot : %d " %p , end="")
#        print(a)
        if k > p:
           small_quick(a, p+1, h, k)
           
def partial_quick(a, n, k):
    l = -1
    while  l < k and l < n:
        l =  partition(a,l+1,n-1)
 
                

if __name__ =="__main__":
    print("Python program to print the first k smallest numbers")
    N=int(input("How many numbers?"))
    ar= random.sample(range(1,1000),N)
    print("The input numbers are")
    print(ar)
    a=ar[:]
    b=ar[:]
    d=ar[:]
    K=int(input("How many smallest numbers"))
    if K > N:
        print("Invalid entry")
        exit()
    print("The sorted numbers are ")
    ar.sort()
    print(ar)    
    small_k_heap(a,N,K)
    print_bottom_k(a,N,K)
    print("The quick sort method")
    small_quick(b,0,N-1,K)
    print_top_k(b,N,K)
    c=b[:K]
    c.sort()
    print("The sorted %d numbers are" %K)
    print(c)
    print("The iterative partial quick sort method")
    partial_quick(d, N, K)
    print_top_k(d,N,K)
    c=d[:K]
    c.sort()
    print("The sorted %d numbers are" %K)
    print(c)              
                                      
