import random

def print_matrix(msg, mat, r, c, size):
    print(msg)
    for i in range(size):
        for j in range(size):
            print("%d " %mat[r+i][c+j], end="")
        print()
            

def is_square(mat, r,c,size):
    for i in range(0, size):
        if mat[r][c+i]:
            return False
        if mat[r+size-1][c+i]:
            return False
        if mat[r+i][c]:
            return False
        if mat[r+i][c+size-1]:
            return False 
    return True

def find_square(mat, N, size):
    count = N-size+1
    for i in range(count):
        for j in range(count):
            if is_square(mat, i,j,size):
                return True, i,j
    return False, 0,0

def find_square_with_size(mat, N):
    for i in range(N, 0, -1):
        res, r, c =  find_square(mat, N, i)
        if res:
            return res, r, c, i 
    return False, 0, 0, 0


def process_square(mat, N):
    pro = list()
    for i in range(N):
        pro.append(list())
        pro[i] = list()
        for j in range(N):
            pro[i].append([0,0])
    
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if not mat[i][j]:
                pro[i][j] = [1,1]
                if j+1 < N:
                   pro[i][j][0] += pro[i][j+1][0]
                if i+1 < N:
                    pro[i][j][1] += pro[i+1][j][1] 
    #print(pro)                  
    return pro            

def is_square_1(r,c, size, pro):
    topleft = pro[r][c]
    topright = pro[r][c+size-1]
    bottomleft = pro[r+size-1][c]
    
    if topleft[0] < size or topleft[1] < size or topright[1] < size or bottomleft[0] < size:
        return False
    return True

def find_square_size_1(mat, N, size, pro):
    count = N-size+1
    for i in range(count):
        for j in range(count):
            if is_square_1(i, j, size, pro):
                return True, i, j
    return False, 0,0

def find_square_1(mat, N):
    pro = process_square(mat, N)
    
    for i in range(N, 0, -1):
        res, r, c = find_square_size_1(mat, N, i, pro)
        if res:
            return True, r, c, i
    return False, 0,0,0
     
     
if __name__=="__main__":
    print("Python program to find the max square in give square matrix")
    N = int(input("Enter the size of the matrix"))
    mat = list()
    for i in range(N):
        mat.append(list())
        mat[i] = [random.choice([0,1,0,0]) for x in range(N)]
    print("The given input matrix is as follows")
    for i in range(N):
        print(mat[i])
    res, r, c, size = find_square_with_size(mat, N)
    if res:
        print("The largest square surrounded by 0s found at row : %d and column : %d , size = %d" %(r,c,size))
        print_matrix("The square matrix ", mat, r, c, size)
    else:
        print("The square matrix not found") 

    res, r, c, size = find_square_1(mat, N)
    if res:
        print("Alternative Method : The largest square surrounded by 0s found at row : %d and column : %d , size = %d" %(r,c,size))
    else:
        print("Alternative method: The square matrix not found")             
                                 
        
           