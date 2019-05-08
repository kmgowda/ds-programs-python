import random

def get_target(a,b):
    sa= sum(a)
    sb= sum(b)
    if sa > sb:
        return 0, (sa-sb)//2
    else:
        return 1, (sb-sa)//2

def get_sum_pair(a,b,target):
    for num in a:
        diff = num-target
        if diff in b:
            return num,diff
    return None,None

def print_sum_pair(a,b):
    t, target = get_target(a,b)
    if t:
       one,two = get_sum_pair(b,a,target)
       if one:
           nsum = sum(b)-one+two
    else:
       one, two = get_sum_pair(a,b,target)
       if one:
           nsum = sum(a)-one+two
    print("The input arrays are ")
    print(a)
    print(b)       
    if one:
        print("The pair of values to exchange to get the sum %d are %d and %d" %(nsum, one,two))
    else:
        print("There are no pair of values to get the same sum")           


if __name__=="__main__":
    print("Python program to identify the pair of values in an arry which yields the same sum")
    M = int(input("How many numbers in array 1 ?"))
    N= int(input("How many numbers in array 2 ?"))
    print(range(10))
    if M > N:
       a = random.sample(range(0,50),M)
       b = random.sample(range(0,99),N)
    else:
       a = random.sample(range(0,99),M)
       b = random.sample(range(0,50),N)
    print_sum_pair(a,b)
 
    
    
             
    
