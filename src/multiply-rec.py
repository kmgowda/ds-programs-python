import random

def multiply(s,b):
    if s == 0:
        return 0
    elif s == 1:
        return b
    else:
        h= multiply(s>>1, b)
        if s&1:
            return (h<<1)+b
        else:
            return h<<1
    
    
if __name__=="__main__":
    print("Python program to multiply two numbers")
    a = random.sample(range(0,1000), 2)
    if a[0] > a[1]:
        s = a[1]
        b = a[0]
    else:
        s = a[0]
        b = a[1]
    print("Multiplication of %d and %d : %d , %d(*)" %(a[0], a[1], multiply(s,b),a[0]*a[1]))                