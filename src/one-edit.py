
def onereplace(str1, str2):
    found = False
    for i, c in enumerate(str1):
        if c != str2[i]:
            if found:
                return False
            else:
               found = True 
    return found

def oneinsert(str1, str2):
    id2 = 0
    id1 = 0
    while id1 < len(str1):
        if str1[id1] != str2[id2]:
            if id1 != id2:
                return False
            else:
                id2+=1
        else:
           id1+=1
           id2+=1
    return True            

def one_edit(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 == l2:
       if onereplace(str1, str2):
           print("The string %s is one replacement of string %s " %(str1,str2))
       else:
           print("The string %s is not one replacement of string %s " %(str1,str2))
    else:
        if l1 < l2:
            if oneinsert(str1, str2):
                print("The string %s is one increment of string %s " %(str2,str1))
            else:
                print("The string %s is not one increment of string %s " %(str2,str1))
        else:
           if oneinsert(str2, str1):
                print("The string %s is one increment of string %s " %(str1,str2))
           else:
                print("The string %s is not one increment of string %s " %(str1,str2))


if __name__ == '__main__':
    print("Python string single edit, replace and remove identification program")
    str1 = input("Enter the input string 1")
    str2 = input("Enter the input string 2")
    one_edit(str1,str2)
                                                  