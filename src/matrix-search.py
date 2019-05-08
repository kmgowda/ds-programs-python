import random

def create_matrix(a, m, n):
    mat = list()
    for i in range(m):
        index = n*i
        mat.append(a[index:index+n])
    return mat

def print_matrix(mat):
    for row in mat:
        print(row)
    

def matrix_search(mat,m,n,item):
    r = 0
    c = n-1
    while r < m and c >= 0:
        if mat[r][c] == item:
            return r,c
        elif mat[r][c] > item:
            c-=1
        else:
            r+=1
    return -1,-1

if __name__=="__main__":
    print("Python program for search an item in M*N mtrix")
    m=int(input("Enter the row size"))
    n=int(input("Enter the column size"))
    a = random.sample(range(1,1000), m*n)
    a.sort()
    print (a)
    mat = create_matrix(a,m,n)
    print("input matrix is as follows")
    print_matrix(mat)
    item=int(input("enter the elment to search"))
    r,c= matrix_search(mat,m,n,item)
    if r == -1:
        print("the number %d not found in the matrix" %item)
    else:
        print("The number %d found at row %d , column %d" %(item,r+1,c+1))    
                            