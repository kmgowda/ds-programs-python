
def tower(N,A='A',B='B',C='C'):
    if N > 0:
        tower(N-1,A,C,B)
        print("Move %d from tower %c to tower %c" %(N,A,C))
        tower(N-1,B,A,C)
        
        
if __name__=="__main__":
    print("Python program for tower of honai")
    N=int(input("How many disks?"))
    tower(N)        