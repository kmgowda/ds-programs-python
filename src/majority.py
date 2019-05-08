import random


def validate(ar,major):
    count = 0
    for item in ar:
        if item == major:
            count+=1
    return count >= (len(ar)//2)


def get_major(ar):
    for item in ar:
        if validate(ar,item):
            return item
    return None

def get_candidate(ar):
    count = 0
    for item in ar:
        if not count:
            major = item
        if item == major:
            count +=1
        else:
            count -=1
    return major

def get_major_1(ar):
    tmp = get_candidate(ar)
    if validate(ar,tmp):
        return tmp
    else:
        return None             

if __name__=="__main__":
    print("Python program to get the majority element")
    N=int(input("How many numbers?"))
    ar=[random.choice([1,2,3]) for x in range(N)]
    print("The input array")
    print(ar)
    major =  get_major(ar)
    if major:
       print("Method 1: The majority element : %d" %major)
    else:
       print("Method 1: No major element found")
    major =  get_major_1(ar)
    if major:
       print("Method 2: The majority element : %d" %major)
    else:
       print("Method 2: No major element found")                               