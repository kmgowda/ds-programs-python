

def robo_print(st):
    flag =0
    down = 0
    for i in range(len(st)):
        if st[i] == '|':
           if flag == 0:
              flag = 1 
              tmp = st[i]
              if down == 0:
                  down = i         
           else:
               tmp =' '*down+st[i]
           print(tmp)
        else:
            if flag:
               flag = 0 
               tmp=' '*down+st[i]
            else:
                tmp =st[i]
            down+=1    
            print(tmp, end="")


def robo_path(N, r=0, d=0, str=""):
    if r > N or d > N:
        return
    if r == N and d == N:
        robo_print(str)
        print()
        print("****************************")
    robo_path(N, r+1, d, str+"->")
    robo_path(N, r, d+1, str+"|")    

if __name__=="__main__":
   print("Python program to print the all possible paths for robo grid of N*N")
   N=int(input("Enter the input N*N matrix size"))
   print()
   print("****************************")
   robo_path(N)
                        
