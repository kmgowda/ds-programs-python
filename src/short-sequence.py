import random


def find_next(big, element, index):
    for i in range(index, len(big)):
        if big[i] == element:
            return i
    return -1     

def find_closure(big,small, index):
    max = -1
    for item in small:
        next = find_next(big, item, index)
        if next == -1:
            return next
        if max < next:
            #index = next
            max = next
    return max 

def short_sequence(big, small):
    start = -1
    end = -1
    for i in range(len(big)):
        tmp = find_closure(big,small, i)
        if tmp == -1:
            break
        if start == -1 or (tmp-i < end-start):
           start = i
           end = tmp 
    return start, end


def create_indecies(big,small):
    ind= [None]*len(small)
    for i in range(len(small)):
        ind[i]=list()
        for j in range(len(big)):
            if small[i] == big[j]:
                ind[i].append(j)
    return ind            
                

def get_sequence(ind,tmp):
    seq= [None]*len(tmp)
    #print("sequence indexes")
    #print(tmp)
    for i in range(len(tmp)):
        seq[i] = ind[i][tmp[i]]
    #print("sequences")    
    #print(seq)    
    return seq

def get_min_seq(seq):
    min = seq[0]
    max = seq[0]
    for item in seq:
        if item < min:
            min = item
        if item > max:
            max = item
    return min,max 


def get_min(one,two):
    if one[0] == None:
        return two, True

    val1 = one[1]-one[0]
    val2 = two[1]-two[0]
 
    if val1 < val2:
        return one, True
    else:
        return two, False
        



def get_short_sequence(ind):
    tmp = [0]*len(ind)
    best_min=[None,None]
    i = len(tmp)-1
    index = i
    l = index
    while index >= 0:
        seq = get_sequence(ind,tmp)
        min = get_min_seq(seq)
        best_min, flag = get_min(best_min, min)
        print("sequence: ", end="")
        print(seq)
        print("best min: ", end="")
        print(best_min)
        if flag and tmp[l] < len(ind[l])-1:
            tmp[l]+=1
        else:
            for k in range(index, len(tmp)):
                tmp[k]=0
            i = len(tmp)-1    
            index-=1
            if index >= 0:
               tmp[index]+=1 

    return best_min           
        

def get_short_sequence_method2(big, small):
    ind = create_indecies(big,small)
    print("Indexes are")
    print(ind)
    tmp = get_short_sequence(ind)
    print(tmp)

if __name__=="__main__":
    print("Python program to find the shortest subsequence")
    N = int(input("what is the size of big array?"))
    M = int(input("what is the size of sub array?"))
    big=[random.choice([1,2,3,4,5,6,7,8,9]) for x in range(N)]
    #big = random.sample(range(1,N+1),N)
    small = list()
    for i in range(M):
           pos = random.randint(0, N-1)
           if big[pos] not in small:
              small.append(big[pos])
  
    print("The big array")
    print(big)
    print("The small array")
    print(small)
    start, end = short_sequence(big, small)
    if start != -1:
        print("The sequence positions are %d and %d" %(start, end))
    else:
        print("The short sequence not found") 
    get_short_sequence_method2(big,small)
   