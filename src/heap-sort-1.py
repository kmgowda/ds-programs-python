import random

class heapsort:
      def __init__(self):
          pass

      def heapfiy(self, a, i, N):
          if i <= N//2:
              self.heapfiy(a, i+1, N)
              l = 2*i+1
              r = l+1
              k = l
              if r < N:
                  if a[r] > a [l]:
                      k = r
              if k < N and a[i] < a[k]:
                  tmp = a[i]
                  a[i] = a[k]
                  a[k] = tmp
                           
       
      def sort(self, a, N):
          for i in range(N, 0, -1):
              self.heapfiy(a, 0, i)
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
    