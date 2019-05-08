import random

def add(a,b):
    while b:
        sum = a^b
        carry = (a&b)<<1
        a = sum
        b = carry
    return a

# the below logic works only for C
#def add_1(a,b):
#    return print("%*c%*c",  a, ' ',  b, ' ')

if __name__=="__main__":
    print("Python program to add two numbers without using '+' operator" )    
    a = random.randint(0,1000)
    b = random.randint(0,1000)
    print("The numbers are %d %d" %(a,b))
    print("The sum of %d and %d without + is %d (%d)" %(a,b,add(a,b), a+b))
#    tmp = add_1(a,b)
#    print("another way: %d" %(tmp))
