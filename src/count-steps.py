
def count_steps(N, str=""):
    if N < 0:
        return
    elif N ==0:
        print("%d : %s" %(count_steps.count, str))
        count_steps.count+=1
    else:
        count_steps(N-1, str+"1 ")
        count_steps(N-2, str+"2 ")
        count_steps(N-3, str+"3 ")    
count_steps.count=1


if __name__=="__main__":
    print("Python program to print all possible ways to print the paths to claim N steps")
    N = int(input("How many stpes of stairs?")) 
    count_steps(N)        