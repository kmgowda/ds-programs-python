import random

# Assuming that 32  bit number
def sign(num):
    return (num>>31)&0x1

def flip(bit):
    return 1^bit

def max(a,b):
    # sign will 1 if a<b
    s = sign(a-b)
    f = flip(s)
    return a*f+b*s

if __name__=="__main__":
    print("Python program to find the maximum of two numbers without using if , else  and comparision statements")
    lt = random.sample(range(-1000, 1000), 2)
    m = max(lt[0],lt[1])
    print("The maximum of %d and %d is %d" %(lt[0],lt[1],m)) 