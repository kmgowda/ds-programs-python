import random

def subsort(a):
    z = len(a)
    left = 0
    for i in range(z-1):
        if a[i] < a[i+1]:
            left = i+1
        else:    
            break
    right = z-1    
    for i in range(z-1, 0, -1):
        if a[i-1] <= a[i]:
            right = i
        else:    
            break 
    left1 = left    
    for i in range(left, -1,-1):
        if a[i] > a[right]:
           left1 = i
        else:   
           break
    right1 = right   
    for i in range(right, z):
        if a[right-1] <= a[i]:
            right1 = i
        else:    
            break
    return left1, right1 

if __name__=="__main__":
    print("Pyhton program to identify the subsort arrary")
    N = int(input("How many numbers?"))
    ar = [random.randint(1,7) for x in range(N)]
    l, r = subsort(ar)
    print("The input arry is :" , end="")
    print(ar)
    print("The subsort indices are %d and %d" %(l,r))           