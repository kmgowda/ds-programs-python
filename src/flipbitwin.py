import sys

def get_zeros_ones_list(n):
    s = sys.getsizeof(n)
    a = list()
    ones = 0
    zero = 0
    flag = 1
    for i in range(s):
        val = (n >> i) & 1
        if val:
            if zero:
                a.append(zero)
                zero = 0
            ones = ones+1
        else:
            if flag == 1 or ones > 0:
               a.append(ones)
               flag = 0 
               ones = 0
            zero = zero+1
    if zero:
        a.append(zero)
    if ones:
        a.append(ones)
    return a

def flipbitwin(a):
    max = a[0]
    for i in range(1, len(a)):
        if i%2:
            if a[i] == 1 and i+1 < len(a):
               tmp = a[i-1]+a[i+1]
               if tmp > max:
                   max= tmp
        else:
           if max < a[i]:
              max = a[i]             
    return max+1
 

def flipbitwin_1(n):
    ones = 0
    pones = 0
    max = 0
    while n != 0:
        if n&1:
            ones = ones+1
        else:
            if n&2:
                pones = ones
            else:
                pones = 0      
            ones = 0
        if max < ones+pones+1:
            max =  ones+pones+1 
        n = n>>1
    return max                 
 
if __name__=="__main__":
    print("Python program to flip a bit to win")
    n = int(input("Enter a number"))
    a = get_zeros_ones_list(n)
    print(a)
    max = flipbitwin(a)
    print("%d = %s, flipbitwin = %d , alternative flipbitwin = %d" %(n, bin(n), max, flipbitwin_1(n)))
                       