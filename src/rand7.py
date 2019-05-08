import random


def rand7():
    while True:
          num = 5*random.randint(0,5)+random.randint(0,5)
          if num < 21:
            return num%7

if __name__=="__main__":
    print("Python program to print the random integer of 0.. 6")
    print("Press a key") 
    while True:
        input()
        val = rand7()
        print("The random number %d" %val)
        
        
