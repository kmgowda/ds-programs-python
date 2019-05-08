def unique_str(str):
    bitmap = 0
    for c in str:
        val = 1 << ord(c)
        if (bitmap&val == 0):
           bitmap |= val
        else:
            return False
    return True


if __name__=='__main__':
   print("Python program to find check string uniqueness")
   str = input("Enter the input string")
   if unique_str(str):
      print("String %s has unique characters" %str)
   else:
      print("String %s does NOT has unique characters" %str)
          
                         