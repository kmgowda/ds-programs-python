import random

max_width = 16

class HashTable:
    def __init__(self, size):
        self.lt = [None]*size
        self.size = size

    def insert(self,value):
        rem = value%self.size
        if self.lt[rem] == None:
            self.lt[rem]= list() 
        self.lt[rem].append(value)
        id = len(self.lt[rem])
        key = ((id-1) << max_width) | rem
        return key
    
    def get_value(self, key):
        rem = key & (max_width-1)
        id = key >> max_width
        return self.lt[rem][id]
    
    def get_key(self, value):
        rem = value%self.size
        found = False
        for i in range(len(self.lt[rem])):
            if self.lt[rem][i] == value:
               found = True
               break 
        if found:
               return (i << max_width) | rem 
        else:
             return -1    
    
    def printt(self, msg):
        print(msg)
        print(self.lt)
        for ar in self.lt:
            if ar == None:
                continue
            for val in ar:
                key = self.get_key(val)
                if key == -1:
                    print("Hash key not found for the value %d" %val)
                else:
                    value = self.get_value(key)
                    print("hash key = %d (%x), value = %d" %(key, key, value))             



if __name__=="__main__":
    print("Python program to create an Hash Table")
    N = int(input("How many numbers?"))
    if N > 64:
        print("Maximum 64 numbers only")
        exit()
    a = random.sample(range(1,100), N)
    print("The input numbers are")
    print(a)
    ht = HashTable(10)
    for val in a:
        ht.insert(val)
    ht.printt("Hash Table contents are as follows")    


    
    
            