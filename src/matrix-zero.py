def matrix_zero(mat, N):
    found = False
    r = [0]*N
    c = [0]*N
    for i in range (N):
        for j in range(N):
            if mat[i][j] == 0:
                r[i] = 1
                c[j] = 1 
   
    for idx, i in enumerate(r):
        if i == 1:
           for j in range(N):
               mat[idx][j] = 0
               found = True  
    for idx, i in enumerate(c):
        if i == 1:
           for j in range(N):
               mat[j][idx] = 0
    return found        
                            

if __name__=='__main__':
    print("Matrix 0 set program")
    N = int(input("Enter the size of N*N matrix"))
    mat = list()
    for i in range(N):
        mat.append(list())
        print("**** row %d ****" %(i+1))
        for j in range(N):
            val = int(input("Enter the value for mat[%d][%d]" %(i+1, j+1)))
            mat[i].append(val)
    print("Input matrix")
    print(mat)
    found = matrix_zero(mat, N)
    if found == False:
       print("No zeros found")
    else:    
       print("Matrix output")
       print(mat)              
                                    