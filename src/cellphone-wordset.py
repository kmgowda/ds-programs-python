import random

class cellphone_keypad:
    def __init__(self):
        self.T9 = [None,None,('a','b','c'),('d','e','f'),('g','h','i'),('j','k','l'),('m','n','o'),('p','q','r','s'), ('t','u','v'), ('w','x','y','z')]
    
    def get_words_rec(self, num, wordlist, index=0, prefix=""):
        if index == len(num):
            wordlist.append(prefix)
            return  
        digit = int(num[index])
        chars = self.T9[digit]
        if chars:
           for char in chars:
               self.get_words_rec(num,wordlist,index+1,prefix+char)
        else:
             self.get_words_rec(num,wordlist,index+1,prefix)      

    
    def get_words(self, num):
        wordlist = list()
        self.get_words_rec(num,wordlist)
        return wordlist
    
if __name__=="__main__":
    print("Python program to print all the 4 chars words of cellphone keypad")
    ar = random.sample(range(1001,10000), 3)
    keypad = cellphone_keypad()
    for num in ar:
        st = str(num)
        words = keypad.get_words(st)
        print("The words list for the number "+st)
        print(words)


