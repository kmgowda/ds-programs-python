
def count_2s(num):
    count = 0
    while num:
        if num%10==2:
           count+=1
        num//=10
    return count


def count_2s_in_range(num):
    count=0
    index=1
    for i in range(2, num+1):
        tmp = count_2s(i) 
        if tmp:
           count+= tmp
           if index%10: 
              print("%5d " %i, end="")
           else:
              print("%5d " %i)
           index+=1       
           
    print("\nThe number of 2 in the range 2 to %d : %d" %(num, count))
    return count 



def count2s_at_digit(number, d):
    pow10 = 10**d
    nextpow10 = pow10*10
    right = number%pow10
    
    rounddown = number-right
    roundup = rounddown+nextpow10
    
    digit = (number//pow10)%10
#    print("digit = %d , rounddown = %d , roundup = %d,  right = %d , pow10 = %d"  %(digit,rounddown, roundup,right,pow10))
  
    if d:
       if digit < 2:
          return rounddown//10
       elif digit == 2:
          return rounddown//10+right+1
       else:
          return roundup//10
    else:
        if digit < 2:
            return 0
        else:
            return 1  

def count2s_at_alldigits(number):
    count = 0
    tmp = number
    index = 0
    while tmp:
        count +=count2s_at_digit(number, index)
        index+=1
        tmp //=10
    return count    
 
    
    
if __name__=="__main__":
    print("Python program to count and print the number of2 in the range N")
    N=int(input("Enter the range value N"))
    count_2s_in_range(N)
    print("Total count of 2s is %d" %(count2s_at_alldigits(N)))
          