def print_par(l, r, str=""):
    if l < 0 or r < l:
        return 
    if l == 0 and r == 0:
        print("%d: %s" %(print_par.counter, str))
        print_par.counter +=1
        
    if l > 0:
        print_par(l-1, r, str+"(")
    if r >0:
        print_par(l, r-1, str+")")
print_par.counter =1 


if __name__=="__main__":
    print("Python program to print all valid combinations of parentheis")
    N= int(input("How many number?"))
    print("comibination of parenthis are")
    print_par(N,N)
