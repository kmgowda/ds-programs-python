
def is_substring(st, sb):
    i = 0
    lsb = len(sb)
    while i < len(st):
        j = lsb
        while j > 0 and (i+j-1) < len(st):
            if sb[j-1] != st[i+j-1]:
                break
            j -= 1
        if j == 0:
            return i+1 
        i+=1
    return -1

if __name__=='__main__':
    print("python substring program")
    st = input("Enter the main string")
    sb =  input("Enter the substring to find")
    pos = is_substring(st, sb)
    if pos != -1:
        print("The substring %s is found in the string %s at index %d" %(sb,st,pos))
    else:
        print("The substring %s is NOT found in the string %s" %(sb,st))            