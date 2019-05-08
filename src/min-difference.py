import random

def min_diff(a,b):
    flag = 0
    min1 = 0
    min2 = 0
    for i in range(len(a)):
        if not flag:
            min = abs(a[i]-b[i])
            min1 = a[i]
            min2 = b[i]
            flag = 1
        else:
            if min > abs(a[i]-b[i]):
                min = abs(a[i]-b[i])
                min1 = a[i]
                min2 = b[i]
    return min, min1, min2

if __name__=="__main__":
    print("Python program to get the minimum of difference of two arrays")
    n = int(input("Enter the size of the array"))
    lt1 = random.sample(range(1, 1000), n)
    lt2 = random.sample(range(1, 1000), n)
    print("The input arrays")
    print(lt1)
    print(lt2)
    lt1.sort()
    lt2.sort()
    min, min1, min2 = min_diff(lt1,lt2)
    print("The minimum difference value are %d , %d and diff value : %d" %(min1, min2,min))
                        


