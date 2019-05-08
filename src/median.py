import random

class heapclass:
    def __init__(self):
        self.ar = list()
    
    def heapfiy(self):
        print("This method not defined")
        pass
           
    def size(self):
        return len(self.ar)
    
    def append(self, val):
        self.ar.append(val)
        self.heapfiy()
    
    def top(self):
        return self.ar[0]
    
    def print_heap(self, msg):
        print(msg)
        print(self.ar)
     
    def pop(self):
        return self.ar.pop()    
 

class minheapclass(heapclass):
    def __init__(self):
#        super(minheapclass, self).__init__()
       heapclass.__init__(self)
    
    def heapfiy(self):
        N = self.size()
        i = N//2        
        while i >= 0:
           j = i*2
           if j+1 < N and self.ar[j+1] < self.ar[j]:
               j+=1
           if j < N:
               if self.ar[i] > self.ar[j]:
                   temp = self.ar[i]
                   self.ar[i] = self.ar[j]
                   self.ar[j] = temp
           i-=1
           

            
class maxheapclass(heapclass):
    def __init__(self):
       heapclass.__init__(self)
    
    def heapfiy(self):
        N = self.size()
        i = N//2
        while i >= 0:
           j = i*2
           if j+1 < N and self.ar[j+1] > self.ar[j]:
               j+=1
           if j < N:
               if self.ar[i] < self.ar[j]:
                   temp = self.ar[i]
                   self.ar[i] = self.ar[j]
                   self.ar[j] = temp
           i-=1

if __name__=="__main__":
    print("python program to keep the median of random numbers")
    ar = list()
    minheap = minheapclass()
    maxheap = maxheapclass()
    while True:
        try:
           n = int(input("Enter the number , press x for exit "))
        except:
            break   
        ar.append(n)
        print("The input list : " , end="")
        print(ar)
        
        if maxheap.size() > minheap.size():
            median = maxheap.pop()
            val = median
        else:
            if maxheap.size() == 0:
               print("The median is : %d" %n)
               maxheap.append(n)
               continue
            median = (maxheap.top()+minheap.top())//2
            val = minheap.pop()

        if n <= median:
           maxheap.append(n)
           minheap.append(val)
        else:
           minheap.append(n) 
           maxheap.append(val)   

        minheap.print_heap("The min heap values are")
        maxheap.print_heap("the max heap values are") 
        if maxheap.size() > minheap.size():
            median = maxheap.top()
        else:
            median = (maxheap.top()+minheap.top())//2
        print("The median value is : %d" %median)    
               
 
         
