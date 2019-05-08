
def get_perms(lt):
    perms = list()
    if len(lt) == 0:
        return perms
    first = lt[0]
    rem = lt[1:]
    words = get_perms(rem)
    if len(words):
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                tmp = list()
                tmp.extend(words[i])
                tmp.insert(j, first)
                perms.append(tmp)
    else:
        tmp = list()
        tmp.append(first)
        perms.append(tmp)           
    return perms 


if __name__=="__main__":
    print("Python program to print all permutations of string")
    str = input("Enter the input string")
    lt = list(str)
    #print (lt)
    perms = get_perms(lt)
    print("All permutations of string")
    for i in range(len(perms)):
        str = ''.join(perms[i])
        print("%d : %s" %(i+1, str))
        


