import random


def rotate(a):
    n = len(a)
    tmp = a[n-1]
    for i in range(N-2,-1, -1):
        a[i+1]=a[i]
    a[0] = tmp

def rotate_multi(a,t):
    if t > len(a):
         return
    for i in range(t):
        rotate(a)


def binary_search(a,l,h,item):
    if l > h:
        return -1
   
    m = (l+h)//2
    if a[m] == item:
        return m
    elif a[m] > item:
        return binary_search(a,l,m-1,item)
    else:
        return binary_search(a,m+1,h,item)    
        

def find(a,item):
    pos = 0
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            pos = i
            break
    if a[pos] == item:
        return pos
    elif item > a[len(a)-1]:
        return binary_search(a,0,pos,item)
    else:
        return binary_search(a,pos+1,len(a)-1,item)


def search(a, item):
    l = 0
    h = len(a)-1
    
    while l < h:
        m = (l+h)//2
        if a[m] == item:
            return m
        else:
            if a[l] <= a[m]:
                if item > a[l] and item < a[m]:
                    h = m-1
                else:
                    l =m+1
            elif a[m] < a[h]:
                if item > a[m] and item <= a[h]:
                    l = m+1
                else:
                    h = m-1
    return -1 

                    
                                

if __name__=="__main__":
    print("Python program for Array rotation and binary search")
    N = int(input("How many numbers?"))
    a = random.sample(range(1,1000), N)
    print("The input numbers are")
    a.sort()
    print(a)
    r = random.randint(1,N)
    rotate_multi(a,r)
    print("The input numbers after %d rototations" %r)
    print(a)
    item= int(input("Enter the number to search ?"))
    pos = search(a,item)
    if pos == -1:
        print("The number %d not found in the array " %item)
    else:
        print("The number %d found at the position in the array at postition %d" %(item, pos+1))    
    
                     
                    