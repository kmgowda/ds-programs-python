import sys

def count_ones(n):
    count = 0
    while n!= 0:
        if n&1:
            count = count+1
        n = n>>1    
    return count


if __name__=="__main__":
    print("Python program to gets the number bits to change from first number to second number")
    a = int(input("Enter first number"))
    b = int(input("Enter the second number"))
    c = count_ones(a^b)
    print("the number of bits to change from %d (%s) to %d (%s) : %d" %(a, bin(a), b, bin(b), c))