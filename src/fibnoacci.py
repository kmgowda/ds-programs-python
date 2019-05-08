def get_fib(a,b,N, ar):
    if N > 0:
        ar.append(a)
        get_fib(b,a+b, N-1,ar)

def get_nth_fib(a,b,N):
    if N == 1:
        return a
    else:   
        return get_nth_fib(b,a+b,N-1)

if __name__=="__main__":
    print("Python program to generate the fibnacci series")
    N=int(input("Enter the number"))
    ar=list()
    get_fib(0,1,N,ar)
    print("The fibonacci series are")
    print(ar)
    f = get_nth_fib(0, 1, N)
    print(f)

            
        