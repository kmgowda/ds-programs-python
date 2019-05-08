from builtins import str
def str_angram(str1, str2):
    l1 = list(str1)
    l2 = list(str2)
    l1.sort()
    l2.sort()
    return l1 == l2


def str_angram_2(str1, str2):
    if(len(str1) != len(str2)):
        return False
    c1 = [0]*256
    c2 = [0]*256
    for c in str1:
        val = ord(c)
        c1[val]+=1
         
    for c in str2:
        val = ord(c)
        c2[val]+=1
    
    for i in range(256):
        if c1[i] != c2[i]:
            return False
    return True             
    
    
if __name__ == '__main__':
    print("Python program to check if two input strings are anagrams or not")
    str1 = input("Enter the input string 1")
    str2 = input("Enter the input string 2")
    print("**** Approach 1 ****")
    if str_angram(str1, str2):
        print("Approach 1:  Input strings are Anagram") 
    else:
        print("Approach 1: Input strings are NOT Anagram")       
        
    print("**** Approach 2 ****")
    if str_angram_2(str1, str2):
        print("Approach 2: Input strings are Anagram") 
    else:
        print("Approach 2: Input strings are NOT Anagram")              