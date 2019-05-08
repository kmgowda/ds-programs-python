import random

class heapsort:
      def __init__(self):
          pass

      def heapfiy(self, a, N):
          max = a[0]
          pos = 0
          for i in range(N//2, -1, -1):
              l = 2*i+1
              if l+1 < N:
                  if a[l+1] > a [l]:
                     l = l+1
              if l < N and a[l] > max:
                 max = a[l]
                 pos = l
          a[pos] = a[0]
          a[0] = max                            
       
      def sort(self, a, N):
          for i in range(N, 0, -1):
              self.heapfiy(a, i)
              tmp = a[0]
              a[0] = a[i-1]
              a[i-1] = tmp
              
              

if __name__=="__main__":
    print("Python program for heap sort")
    N = int(input("How many numbers?"))
    a = random.sample(range(1,1000), N)
    print("The input numbers are")
    print(a)
    hs = heapsort()
    hs.sort(a, N)
    print("Numbers after heap sort")
    print(a)
    