
def rotate_one(mat,r, c, N):
    temp = [None]*4
    
    for i in range(N-1):
        # move right the first row     
        temp[0] = mat[r][c+N-1]
        for j in range(N-2, 0, -1):
            mat[r][j+1]= mat[r][j]
                
    
        #move down the last colum
        temp[1] = mat[r+N-1][c+N-1]
        for j in range(N-2, 0, -1):
            mat[r+j+1][N-1] = mat[r+j][N-1]
                    
                
        #move left the last row
        temp[2] = mat[r+N-1][c]
        for j in range(N-2):
            mat[r+N-1][c+j] = mat[r+N-1][c+j+1]
                      
        #move up the first column
        temp[3] = mat[r][c]
        for j in range(N-2):
            mat[r+j][c] = mat[r+j+1][c]
    
        mat[r+1][c+N-1] = temp[0]
        mat[r+N-1][c+N-2] = temp[1]
        mat[r+N-2][c] = temp[2]
        mat[r][c+1] = temp[3]
                      
            

def rotate_matrix(mat, N):
    r = 0
    c = 0
    for i in range(N, 1,-2):
        rotate_one(mat,r, c,i)
        r =r+1
        c =c+1
       


if __name__=='__main__':
    print("Python Matrix Rotation program")
    N = int(input("Enter the Size of N*N matrix"))
    mat = list()
    for i in range(N):
        mat.append(list())
        print("*** Row  %d ***" %(i+1))
        for j in range(N):
            val = int(input("Enter the value for mat[%d][%d]" %(i+1, j+1)))
            mat[i].append(val)
    print("Input matrix")
    print(mat)
    rotate_matrix(mat, N)
    print("Matrix rotated by 90 degrees right")
    print(mat)         
            
        


        