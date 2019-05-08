import random

def get_perms(lt):
    perms = list()
    if len(lt) == 0:
        return perms
    first = lt[0]
    rem = lt[1:]
    words = get_perms(rem)
    if len(words):
        for word in words:
            for j in range(len(word)+1):
                tmp = list()
                tmp.extend(word)
                tmp.insert(j, first)
                perms.append(tmp)
    else:
        tmp = list()
        tmp.append(first)
        perms.append(tmp)           
    return perms


def get_perms_1(lt):
    perms = list()
    if len(lt) == 0:
       perms.append(list())
       return perms
    first = lt[0]
    words = get_perms_1(lt[1:])
    for word in words:
            for j in range(len(word)+1):
                tmp = list()
                tmp.extend(word)
                tmp.insert(j, first)
                perms.append(tmp)
    return perms  


if __name__=="__main__":
    print("Python program to print all permutations of set")
    N = int(input("How many numbers?"))
    if N > 10:
        print("Maximum 10 numbers only")
        exit()
    a = random.sample(range(1,100), N)
    print("The input numbers are")
    print(a)
    perms = get_perms_1(a)
    print("All permutations of string")
    for i in range(len(perms)):
          print("%d : " %(i+1), end="")
          print(perms[i])
          
        


