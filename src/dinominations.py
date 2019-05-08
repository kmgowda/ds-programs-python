
def print_din(ar, count, a, b, c):
    if a in ar[0] and  b in ar[1] and c in ar[2]:
        return count
    ar[0].append(a)
    ar[1].append(b)
    ar[2].append(c)
    print("%d : 2000 * %d, 500 * %d ,  100 * %d" %(count, a,b, c))
    return count+1


def dinominations(amt,ar, a=0,b=0,c=0):
    if amt < 0:
        return
    elif amt == 0:
        dinominations.count = print_din(ar,dinominations.count,a,b,c)
    else:
        dinominations(amt-2000, ar,a+1, b, c)
        dinominations(amt-500, ar, a, b+1, c)
        dinominations(amt-100, ar, a, b, c+1)

dinominations.count=1


if __name__=="__main__":
    print("python program to print the dinominations (Rs 2000, 500) of given amount (minimum of 500)")
    N =int(input("enter the amount"))
    if N < 100:
        print("Invalid input")
    else:
        ar = list()
        ar.append(list())
        ar.append(list())
        ar.append(list())
        dinominations(N,ar)    