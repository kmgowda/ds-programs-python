import random

def get_missing_number(a,N):
    s1 = (N*(N+1))//2
    s2 = sum(a)
    return s1-s2

if __name__=="__main__":
   print("Python program to find the missing number in the range 0..N")
   N=int(input("Enter the Max limit value for 0..N"))
   ar= random.sample(range(1,N+1),N-1)
   print("The input random array is")
   print(ar)
   print("The missing number is %d" %get_missing_number(ar,N)) 
