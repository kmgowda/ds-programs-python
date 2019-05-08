
def max(a,b):
    if a > b:
        return a
    else:
        return b


def left_bfactor(a, b):
    a = a-1-max(b*-1, 0)
    b = b-1-max(0, a)
    return a, b        


def right_bfactor(a,b):
    a = a+1+max(0, -1*b)
    b = b+1+max(a, 0)
    return a, b


def print_left_bfactors():
    a = 2
    for b in range(-2, 3):
        c, d = left_bfactor(a,b)
        print("left rotate before : %d, %d   , after = %d, %d" %(a, b, c, d))
    
    a = 1
    for b in range(-2, 3):
        c, d = left_bfactor(a,b)
        print("left rotate before : %d, %d   , after = %d, %d" %(a, b, c, d))



def print_right_bfactors():
    a = -2
    for b in range(-2, 3):
        c, d = right_bfactor(a,b)
        print("right rotate before : %d, %d   , after = %d, %d" %(a, b, c, d))
    
    a = -1
    for b in range(-2, 3):
        c, d = right_bfactor(a,b)
        print("right rotate before : %d, %d   , after = %d, %d" %(a, b, c, d))


if __name__=="__main__":
    print("program to generate the AVL Balance factors")
    print_left_bfactors()
    print()
    print_right_bfactors()
    
    
