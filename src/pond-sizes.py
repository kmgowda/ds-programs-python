import random
import sys

def comput_size_it(ar,r, c, N):
    if r >= N or c >= N or r< 0 or c < 0 or ar[r][c] != 0:
        return 0
    lt = list()
    lt.append([r,c])
    size = 1
    ar[r][c] = -1
    while(len(lt)):
        [row,col] = lt[0]
        lt=lt[1:]
        for i in [-1,0,1]:
           for j in [-1,0,1]: 
               if row+i >= N or col+j >= N or row+i< 0 or col+j < 0 or ar[row+i][col+j] != 0:
                  continue
               else:
                  size+=1
                  ar[row+i][col+j] = -1 
                  lt.append([row+i,col+j])
    return size  
            

def compute_size(ar,r,c,N):
    if r >= N or c >= N or r< 0 or c < 0 or ar[r][c] != 0:
        return 0
    size = 1
    ar[r][c] == -1
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            size += compute_size(ar, r+i, c+j,N)
    return size        

def pond_sizes(ar,N):
    sizes = list()
    for i in range(N):
        for j in range(N):
            if ar[i][j] == 0:
               sizes.append(comput_size_it(ar, i, j,N))
    return sizes           
             
if __name__=="__main__":
    print("Python program to find the connected water cells(ponds) in the input matrix of plot of land")
    print (sys.getrecursionlimit())
    #sys.setrecursionlimit(0x1000)
    N=int(input("Enter the size of N*N matrix"))
    ar = list()
    for i in range(N):
        row = [random.randint(0,2) for x in range(N)]
        ar.append(row)
    print("The input matrix is")
    for i in range(N):
        print(ar[i])    
    sizes = pond_sizes(ar,N)
    print("The connected water sizes")
    print(sizes)    
                        