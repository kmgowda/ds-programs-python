import random


def extract_array(a,m,n):
    lt =list()
    for i in range(m,n):
        lt.append(a[i])
    return lt    

def equal_array(a, m, n):
    count = 0
    for i in range(m, n):
        if a[i] ==0:
            count+=1
        else:
            count-=1
    return (count == 0)            
        

def get_arr(a):
    lt =list()
    for i in range(len(a),0,-1):
        for j in range(0, i):
            if equal_array(a,j,i):
               lt.append(extract_array(a,j,i))
    return lt 


def get_delta(a):
    lt = list()
    count=0
    for item in a:
        if item == 0:
            count+=1
        else:
            count-=1
        lt.append(count)
    return lt
 
def get_large_array(delta):
    hash={}
    max = 0
    ms=0
    me =0
    for i in range(len(delta)):
        if delta[i] in hash:
            k = hash.get(delta[i])
            d = i-k
            if d > max:
               max = d 
               ms = k
               me = i
        else:
            hash.update({delta[i]:i})       
    return ms,me 
  
  
def get_max_subarray(a):
    delta=  get_delta(a)
    ms, me =  get_large_array(delta)
    return extract_array(a,ms,me+1)        
                 

if __name__=="__main__":
    print("Python program to return the sub arrays of equal 0s and 1s")
    N=int(input("How many numbers?"))
    ar=[random.randint(0,1) for x in range(N)]
    print("The input list is")
    print(ar)
    print("The largest array with equal number of 0s and 1s ")
    print(get_max_subarray(ar))
    lt = get_arr(ar)
    print("The equal size arrays are as follows")
    for l in lt:
        print(l)           
        