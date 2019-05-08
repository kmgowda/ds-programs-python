import random

class heapsort:
      def __init__(self):
          pass

      def heapfiy(self, a, N):
          for i in range(1, N, 1):
              item = a[i]
              j = i//2
              while j >= 0 and item > a[j]:
                  a[i] = a[j]
                  i = j
                  if j:
                     j //=2
                  else:
                      break 
              a[i] = item    
      
      def adjust(self, a, N):
         i = 0
         item = a[i]
         j = 1
         while j <= N:
             if j+1 < N and a[j] < a[j+1]:
                j+=1
             
             if item < a[j]:
                  a[i] = a[j]
                  i = j
                  j = 2*i+1
             else:
                 break
         a[i] = item         
       
      def sort(self, a, N):
          self.heapfiy(a, N)
          for i in range(N-1, 0, -1):
              tmp = a[i]
              a[i] = a[0]
              a[0] = tmp
              self.adjust(a, i-1)
          print("The list after heapsort")
          print(a)    
              

if __name__=="__main__":
    print("Python program for heap sort")
    N = int(input("How many numbers?"))
    a = random.sample(range(1,1000), N)
    print("The input numbers are")
    print(a)
    hs = heapsort()
    hs.sort(a, N)
    