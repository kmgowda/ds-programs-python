import random
import math

def get_sum(a,N):
    s1 = (N*(N+1))//2
    s2 = sum(a)
    return s1-s2


def get_product(a,N):
    p1= 1
    p2 =1
    for x in range(2,N+1):
        p1*=x
    for x in a:
        if x:
           p2*=x
    return p1//p2


def find_two_values(a,N):
    s = get_sum(a,N)
    p = get_product(a,N)
    
    tmp = math.sqrt(s**2 - 4*p)
    x = (s+tmp)//2
    y = s-x
    return x,y    
    

if __name__=="__main__":
   print("Python program to find the missing number in the range 0..N")
   N=int(input("Enter the Max limit value for 1..N"))
   ar= random.sample(range(1,N+1),N-2)
   ar.sort()
   print("The input random array is")
   print(ar)
   x,y = find_two_values(ar,N)
   if x:
      print("The missing numbers are %d  and %d" %(x,y))
   else:
      print("Could not able find the missing numbers" )    
    
