import random

def get_subset_it(lt):
    max = 1 << len(lt)
    subset = list()
    for i in range(1,max):
         tmp = list()
         k = i
         index = 0
         while k > 0:
           if k&1:
              tmp.append(lt[index])
           k = k >> 1
           index +=1
         subset.append(tmp)
    return subset             
  

if __name__=="__main__":
    print("Python program to print all subsets of set")
    N = int(input("How many numbers?"))
    if N > 64:
        print("Maximum 64 numbers only")
        exit()
    a = random.sample(range(1,100), N)
    print("The input numbers are")
    print(a)
    subsets = get_subset_it(a)
    print("All subsets of string")
    for i in range(len(subsets)):
          print("%d : " %(i+1), end="")
          print(subsets[i])