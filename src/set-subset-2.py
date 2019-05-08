import random

def get_subset(lt, index):
    if len(lt) == index:
        subsets = list()
        subsets.append(list())
    else:
        subsets = get_subset(lt,index+1)
        item = lt[index]
        moresubsets= list()
        for subset in subsets:
            newset= list()
            newset.extend(subset)
            newset.append(item)
            moresubsets.append(newset)
        subsets.extend(moresubsets)   
               
    return subsets             
  


def get_subset_2(lt):
    if len(lt) == 0:
       subsets= list()
       subsets.append(list())
       return subsets
    first = lt[0]
    rem = lt[1:]
    subsets = get_subset_2(rem)
    more = list()
    for sub in subsets:
        tmp = list()
        tmp.extend(sub)
        tmp.append(first)
        more.append(tmp)
    subsets.extend(more)
    return subsets 



def get_subset_3(lt):
    subsets = list()
    subsets.append(list())
    if len(lt) == 0:
        return subsets
    first = lt[0]
    words = get_subset_3(lt[1:])
    for word in words:
        tmp = list()
        if len(word):
           tmp.extend(word)
           subsets.append(word)
        tmp.append(first)
        subsets.append(tmp)
    return subsets



if __name__=="__main__":
    print("Python program to print all subsets of set")
    N = int(input("How many numbers?"))
    if N > 64:
        print("Maximum 64 numbers only")
        exit()
    a = random.sample(range(1,100), N)
    print("The input numbers are")
    print(a)
    subsets = get_subset_2(a)
    print("All subsets of string")
    for i in range(len(subsets)):
          print("%d : " %(i+1), end="")
          print(subsets[i])