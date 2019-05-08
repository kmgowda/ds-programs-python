import random

class mergesort:
      def __init__(self):
          pass

      def merge_copy(self, a, b, c, k):
          i = 0
          j = 0
          al = len(a)
          bl = len(b)
          while i < al and j < bl:
              if a[i] < b[j]:
                  c[k] = a[i]
                  i = i+1
              else:
                  c[k] = b[j]
                  j = j+1
              k = k+1
          while i < al:
              c[k] = a[i]
              i = i+1
              k = k+1
          while j < bl:
              c[k] = b[j]
              j = j+1
              k = k+1                 

      def merge(self, a, l, m, h):
          print("merge : l=%d , m=%d , h=%d" %(l,m,h))
          print(a)
          b = list()
          c = list()
          for i in range(l,m+1):
              b.append(a[i])
          for i in range(m+1, h+1):
              c.append(a[i])
          self.merge_copy(b, c, a, l)
          print(a)
          print()
       
      def merge_sort(self, a, l, h):
          if l < h:
             m = (l+h)//2
             self.merge_sort(a, l, m)
             self.merge_sort(a, m+1, h)
             self.merge(a,l, m, h) 
        
      def sort(self, a, N):
          self.merge_sort(a, 0, N-1) 
                        
              

if __name__=="__main__":
    print("Python program for Merge sort")
    N = int(input("How many numbers?"))
    a = random.sample(range(1,1000), N)
    print("The input numbers are")
    print(a)
    ms = mergesort()
    ms.sort(a, N)
    print("Numbers after Merge sort")
    print(a)
    