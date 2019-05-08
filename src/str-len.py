
def strlen(st):
    count = 0
    while True:
        if st[count:] == '':
            break
        count+=1
    return count


if __name__=="__main__":
    print("Python program to find the length of the string without using len function")
    st = input("Enter the string")
    cu = strlen(st)
    print("The length of the string : %d" %cu)    
            
