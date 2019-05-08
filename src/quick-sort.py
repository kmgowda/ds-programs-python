import random

class quicksort:
      def __init__(self):
          pass

      def partition(self, a, l, h):
          i = l
          j = h
          while i < j:  
              while i < h and a[l] >= a[i]:
                  i +=1
              while l < j and  a[l] < a[j]:
                  j -=1
              if i < j:
                  tmp = a[i]
                  a[i] = a[j]
                  a[j] = tmp 
          tmp = a[l]
          a[l] = a[j]
          a[j] = tmp
          return j            
                      
       
      def quick_sort(self, a, l, h):
          if l < h:
             p = self.partition(a, l, h)
             self.quick_sort(a, l, p-1)
             self.quick_sort(a, p+1, h)
 
        
      def sort(self, a, N):
          self.quick_sort(a, 0, N-1) 
                        
              

if __name__=="__main__":
    print("Python program for Quick sort")
    N = int(input("How many numbers?"))
    a = random.sample(range(1,1000), N)
    print("The input numbers are")
    print(a)
    qs = quicksort()
    qs.sort(a, N)
    print("Numbers after Quick sort")
    print(a)
    