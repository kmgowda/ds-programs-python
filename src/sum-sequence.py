import random


def sum_seq(a):
    sum = 0
    maxsum = 0
    index = 0
    flag = True
    num = 0
    count =0
    for i in range(len(a)):
        sum+=a[i]
        count +=1
        if maxsum < sum:
           maxsum = sum
           num = count
           if flag:
              flag = False
              index = i
        elif sum < 0:
            sum = 0
            flag = True
            count = 0
    return maxsum, index,num

if __name__ == "__main__":
    print("Python program to get the sum sequence")
    N =int(input("How many numbers?"))
    ar = [random.randint(-10,10) for x in range(N)]
    maxsum, index,num = sum_seq(ar)
    print("The array indexes are [" , end="")
    for i in range(len(ar)):
        print("%d, "  %i, end="")
    print("]")    
    print("The input array is   :" , end="")
    print(ar)
    print("The maximum sum sequence at index : %d , %d elements with sum : %d" %(index,num,maxsum))                 