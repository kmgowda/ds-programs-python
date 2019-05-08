import random

def negate(a):
    neg = 0
    if a > 0:
        sign = -1
    else:
        sign = 1
    delta = sign
    while a != 0:
        newsign = (a+delta > 0) != (a > 0)
        if newsign and a+delta != 0:
            delta = sign
        a += delta
        neg += delta
        delta += delta
    return neg

if __name__=="__main__":
    print("Python program to substract two numbers without using '-' operator")
    ar = range(1,1000)
    print (ar)
    a = random.sample(range(1,1000), 2)
    print("The input numbers are %d %d" %(a[0], a[1]))
    print("The negate of %d is %d" %(a[1], negate(a[1])) )
    print("The numbers difference is : %d  (%d [-])" %(a[0]+negate(a[1]), a[0]-a[1]))                 