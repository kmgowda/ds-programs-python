def string_compress(st):
    idx=0
    com = ""
    count = 0
    while idx < len(st):
        if idx == 0:
           count = 1
        else:
           if st[idx-1] != st[idx]:
               com += st[idx-1]
               com += str(count)
               count =1
           else:
               count+=1
        idx+=1
    if count > 0:
       com += st[idx-1]
       com += str(count)         

    return com 

if __name__ =='__main__':
    print("Python string compress program")
    st = input("Enter the input string")
    com = string_compress(st)
    print("Compressed string : "+ com)
                       