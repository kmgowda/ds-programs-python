def print_matrix(mat, N, msg):
    print(msg)  
    #for i in range (0,N):
    print(mat)
        
def input_matrix(N, msg):
    print(msg)
    mat = list()
    for i in range (0,N):
        print("Input row %d" %i)
        temp = list()
        for j in range (0,N):
           print("Input cell  [%d] [%d] :" %(i,j), end='')
           val =int(input())
           temp.append(val)
        mat.append(temp)
    return mat
        
if __name__=='__main__':
   N = int(input("Enter the Size N (N*N) matrix"))
   mat = input_matrix(N, "Enter the matrix values")
   print_matrix(N,mat, "Matrix contents are")
       
             
         