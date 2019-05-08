import sys

def count_ones(n):
    count = 0
    while n!= 0:
        if n&1:
            count = count+1
        n = n>>1    
    return count


def get_next_number(n):
    onec = count_ones(n)
    n = n+1
    while onec != count_ones(n) and n != 0:
         n = n+1
    return n 

def get_next(n):
    count = 0
    mask = 0
    while n != 0:
          if n&1:
             if n&3 == 1:
                break
             mask = (mask << 1) | 1
          else:
             mask =0
          n = n>>1
          count = count+1
    n = (n&~1)|2
    n = (n << count) | mask
    return n 



def get_prev_number(n):
    onec = count_ones(n)
    n = n-1
    while onec != count_ones(n) and n != 0:
         n = n-1
    return n 

def get_prev(n):
    count = 0
    mask =0
    mas =0
    while n != 0:
          if n&1:
              mask = (mask << 1) | 1
          else:    
              if n&2 == 2:
                  break
              mas = mas+1
          n = n>>1
          count = count+1
    n = n&~2|1
    n = (n << count) | (mask << mas)
    return n 

if __name__=="__main__":
    print("Python program to get next number and previous number of the same bits of the given number")
    n = int(input("Enter a number"))
    a = get_next_number(n)
    b = get_next(n)
    print("given number %d (%s), next numbers %d (%s)   %d (%s)" %(n, bin(n), a, bin(a),  b, bin(b)))
    a= get_prev_number(n)
    b= get_prev(n) 
    print("given number %d (%s), previous numbers %d (%s)   %d (%s)" %(n, bin(n), a, bin(a),  b, bin(b)))                   