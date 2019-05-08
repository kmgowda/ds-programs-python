

def fact(num):
    f = 1
    for i in range(2, num+1):
        f *= i
    return f

def trailing_zeros(num):
    count = 0
    i = 5
    while num//i > 0:
        count += num // i 
        i *=5
    return count 

if __name__=="__main__":
    print("Python program to get the factorial of the number")
    num = int(input("Enter the positive value"))
    print("the factorial of %d is %d and number of trailing zeros %d" %(num, fact(num), trailing_zeros(num)))        
    
    



