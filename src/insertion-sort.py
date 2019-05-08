import random


def selection_sort(a, N):
    for i in range(N):
        pos = i
        for j in range(i+1, N):
            if a[j] < a[pos]:
                pos = j
        tmp = a[pos]        
        a[pos] = a[i]
        a[i] = tmp

def bubble_sort(a, N):
    for i in range(N):
        flag = 0
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                tmp = a[j+1]
                a[j+1] = a[j]
                a[j] = tmp
                flag = 1
        # all are sorted elements        
        if flag == 0:
            break        


def insertion_sort(a, N):
    for i in range(1,N):
        j = i-1
        tmp = a[i]
        while j >= 0 and a[j] > tmp:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = tmp


if __name__=="__main__":
    print("program for selection sort, bubble sort and insertion sort")
    N = int(input("How many numbers?"))
    lt = random.sample(range(1, 1000), N)
    print(lt)
    lt2= list()
    lt2.extend(lt)
    lt3 = list()
    lt3.extend(lt)
    selection_sort(lt, N)
    bubble_sort(lt2, N)
    insertion_sort(lt3,N)
    print("selection sort")
    print(lt)
    print("Bubble sort")
    print(lt2)
    print("insertion sort")
    print(lt3)
                                                    