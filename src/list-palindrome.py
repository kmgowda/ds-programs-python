
class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
        
def rec_palindrome(slow, fast):
    if fast == None:
        # Even number of nodes
        return 1, slow
    elif fast.next == None:
        return -1, slow
    else:
        res, ptr = rec_palindrome(slow.next, fast.next.next)
        if res == -1:
           tmp = ptr.next
           if tmp.val != slow.val:
              return 0, None
           else: 
              return 1, tmp.next 
        elif res == 0:
           return 0, None
        elif res == 1:
           if ptr.val != slow.val:
                return 0, None
           else:
                return 1, ptr.next
        else:
           return res, None     
            
class LinkedList:
     def __init__(self):
         self.head = None
     
     def append(self, node):
         if self.head == None:
             self.head = node
         else:
             cur = self.head 
             while cur.next != None:
                 cur = cur.next
             cur.next = node
     
     def display(self, msg):
         print(msg)
         cur = self.head
         while cur != None:
             print("%d" %cur.val, end="")
             if cur.next != None:
                 print("->", end="")
             else:
                 print("")
             cur = cur.next
     
     def is_palindrome(self):
         res, ptr = rec_palindrome(self.head, self.head)
         if res :
             print("The input list is palindrome")
         else:
             print("The input list is NOT palindrome")
             
 
if __name__ == "__main__":
     print("Pyhton program to check if the input list is palindrome or not")
     N = int(input("How many elements?"))
     llist = LinkedList()
     for i in range(N):
         val = int(input("Enter the element of node %d" %(i+1)))
         llist.append(Node(val))
     llist.display("Input Linked List")
     llist.is_palindrome()
                                                    
                