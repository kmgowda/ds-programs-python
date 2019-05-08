import random

def find_pair(ar,sum):
    ar.sort()
    size = len(ar)
    last = size-1
    first = 0
    lt=list()
    while first < last:
        tmp = ar[first]+ar[last]
        if tmp == sum:
            lt.append([ar[first],ar[last]])
            first+=1
            last-=1
        elif tmp < sum:
            first+=1
        else:
            last-=1
    return lt                

if __name__=="__main__":
    print("Python program to print the pair of values which sums to input value")
    N=int(input("How many values?"))
    ar=random.sample(range(-10,10),N)
    print("The input array is as follows")
    print(ar)
    sum=int(input("Enter the sum value"))
    lt=find_pair(ar,sum)
    if len(lt):
        print("The list of pairs which the sum %d" %sum)
        print(lt)
    else:
        print("There is no list of pairs")    

        
