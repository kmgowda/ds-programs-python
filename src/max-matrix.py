import random


def print_matrix(msg, mat, r1, r2, c1, c2):
    print(msg)
    for i in range(r1, r2):
        for j in range(c1, c2):
            print("%3d " %mat[i][j], end="")
        print()

def get_sum(mat, r1, r2, c1,c2):
    sum = 0 
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            sum +=mat[i][j]
    return sum        

def get_sum_matrix(mat,N):
    row1= -1
    row2 = -1
    col1 = -1
    col2 = -1
    maxsum = 0
    for r in range(1, N):
        for i in range(r):
            for c in range(1,N):
                for j in range(c):
                     summat = get_sum(mat,i,r,j,c)
                     if row1 == -1 or max_sum < summat:
                         max_sum = summat
                         row1 = i
                         row2 = r
                         col1 = j
                         col2 = c
    return  row1, row2, col1, col2, max_sum 


def sum_through(mat,N):
    st = list()
    for i in range(N):
        st.append(list)
        st[i] = list()
        for j in range(N):
            if j-1 >= 0:
                left = st[i][j-1]
            else:
                left = 0
            if i-1 >= 0:
                top = st[i-1][j]
            else:
                top = 0
            if i-1 >= 0 and j-1 >= 0:
                topleft = st[i-1][j-1]
            else:
                topleft = 0
            val = mat[i][j]+left+top-topleft 
            st[i].append(val)
    return st                            
            
def get_sum_by_through(st, r1, r2, c1, c2):

    if r1-1 >= 0:
        top = st[r1-1][c2]
    else:
        top = 0
    
    if c1-1 >= 0:
        left = st[r2][c1-1]
    else:
        left = 0
    
    if r1-1 >= 0 and c1-1 >=0:
        topleft = st[r1-1][c1-1]
    else:
        topleft = 0
 
    return st[r2][c2]-top-left+topleft

def get_max_matrix_by_through(mat, N):
    st = sum_through(mat,N)
    print_matrix("The sum through  matrix is as follows", st, 0, N, 0,N)  
    row1 = -1
    row2 = -1
    col1 = -1
    col2 = -1
    maxsum = 0
    for r2 in range(1, N):
        for r1 in range(r2):
            for c2 in range(1,N):
                for c1 in range(c2):
                    val = get_sum_by_through(st, r1, r2, c1, c2)
                    if row1 == -1 or val > maxsum:
                        maxsum = val
                        row1 = r1
                        row2 = r2
                        col1 = c1
                        col2 = c2
    return row1, row2, col1, col2, maxsum                
                    


def sum_seq(ar, N):
    sum = 0
    maxsum = 0
    index = 0
    flag = True
    num = 0
    count =0
    for i in range(N):
        sum+=ar[i]
        count +=1
        if maxsum < sum:
           maxsum = sum
           num = count
           if flag:
              flag = False
              index = i
        elif sum < 0:
            sum = 0
            flag = True
            count = 0
    return maxsum, index,index+num-1

def get_max_sum_matrix(mat, N):
    row1 = -1
    row2 = -1
    col1 = -1
    col2 = -1
    maxsum = -1
    
    for r1 in range(N):
        part = [0]*N
        for r2 in range(r1,N):
            for c in range(N):
                part[c] +=mat[r2][c]
                
            val, c1, c2 =  sum_seq(part, N)
            if row1 == -1 or val > maxsum:
               maxsum = val
               row1 = r1
               row2 = r2
               col1 = c1
               col2 = c2
    return  row1, row2, col1, col2, maxsum       


if __name__=="__main__":
    print("Python program get the matrix of maximum sum")
    N = int(input("what is size of N*N matrix"))
    mat = list()
    for i in range(N):
        mat.append(list)
        mat[i] = [random.randint(-10,10) for x in range(N)]
    print_matrix("The input matrix is as follows", mat, 0, N, 0,N)    
    r1,r2,c1, c2, summat = get_sum_matrix(mat, N)
    if r1 == -1:
        print("Unable to find the sub matrix of max sum")
    else:    
        print_matrix("The matrix with max sum : %d, r1=%d, c1=%d , r2=%d , c2=%d " %(summat, r1, c1, r2,c2) , mat, r1, r2+1, c1,c2+1)

    r1,r2,c1, c2, summat = get_max_matrix_by_through(mat, N)
    if r1 == -1:
        print("Unable to find the sub matrix of max sum")
    else:    
        print_matrix("The matrix with max sum : %d, r1=%d, c1=%d , r2=%d , c2=%d " %(summat, r1, c1, r2,c2) , mat, r1, r2+1, c1,c2+1)

    r1,r2,c1, c2, summat = get_max_sum_matrix(mat, N)
    if r1 == -1:
        print("Unable to find the sub matrix of max sum")
    else:    
        print_matrix("The matrix with max sum : %d, r1=%d, c1=%d , r2=%d , c2=%d " %(summat, r1, c1, r2,c2) , mat, r1, r2+1, c1,c2+1)  
          
                               