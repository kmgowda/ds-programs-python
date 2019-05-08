

def print_queen(ar,N):
    print(ar)
    for col in ar:
        for i in range(col):
            print("0 " , end="")
        print("1 ", end="")
        for i in range(col+1, N):
            print("0 ", end="")
        print()
    print("************") 
 
def is_ok(ar, k):
    for i in range(k):
        if x[i] == x[k] or i-x[i] == k-x[k] or i+x[i] == k+x[k]:
            return False
    return True


def nqueen(N,x):
    k = 0
    x[k] = 0
    
    while k >= 0 :
#        x[k] += 1
        while x[k] < N and is_ok(x,k)==False:
            x[k]+=1
        
        if x[k] < N:
            if k == N-1:
                print_queen(x,N)
                # next solution
                # try with the same row; but next column
                x[k]+=1
            else:
                # go to next row
                k+=1
                # start with first column
                x[k] = 0     
        else:
            # go to the previous row
            k-=1
            # go to next column
            x[k]+=1
 
 
 
 
def nqueen_rec(N,x,k=0):
    if k < N and k >= 0:
       x[k]+=1
       while x[k] < N and is_ok(x,k)==False:
            x[k]+=1
       if x[k] < N:      
          if k == N-1:
             print_queen(x,N)
#             nqueen_rec(N,x,k)
          else:   
             x[k+1]=-1
             nqueen_rec(N,x,k+1)
       else:
            nqueen_rec(N,x,k-1)     
             
                           



if __name__=="__main__":
     print("Python program to N-queen probem")
     N=int(input("Enter the number of queens?"))
     x = [-1]*N
     nqueen_rec(N,x)     
                                              