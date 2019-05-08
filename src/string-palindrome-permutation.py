def toggle(bitmap, bit):
    val = 1 << bit
    if bitmap&val:
        bitmap &= ~val
    else:
        bitmap|= val
    return bitmap    

def is_one(bitmap):
    if bitmap:
       return (bitmap & (bitmap-1))==0
    else:
       return False 

def create_bitmap(str):
    bitmap = 0
    for c in str:
        c = c.lower()
        val =ord(c)
        val -= ord('a')
        bitmap = toggle(bitmap, val)
    return bitmap 

def str_palindrom(str):
    str = str.replace(' ','')
    bitmap =  create_bitmap(str)    
    if (len(str)&1):
        if is_one(bitmap):
            print("ODD: Input string is  a palindrom permutation")
        else:
            print("ODD: Input string is NOT a palindrom permutation")    
    else:
        if is_one(bitmap):
            print("EVEN: Input string is NOT a palindrom permutation")
        else:
            print("EVEN:Input string is a palindrom permutation")    

if __name__ == '__main__':
    print("Python program to determine if the input string is palindrom permutation or not")
    str = input("Enter the input string")
    str_palindrom(str)
                           