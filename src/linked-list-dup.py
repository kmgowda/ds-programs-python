from platform import node
from pip._vendor.requests.api import head
from macpath import curdir
class node:
    def __init__(self, val):
        self.value = val
        self.next = 0

class LinkedList:
    def __init__(self):
        self.head = 0

    def add(self,node):
        if self.head == 0:
           self.head = node
        else:
           cur = self.head
           while cur.next != 0:
                 cur = cur.next
           cur.next = node       
    
    def remove(self, node):
        cur = self.head
        found = False
        while (cur != 0):
           if cur.value == node.value:
              if self.head == cur:
                 self.head = cur.next
              else:
                 prev.next = cur.next   
              del cur
              cur = 0
              found = True
           else:
               prev = cur
               cur = cur.next
        if found:                      
           print("The node %d is successfully removed " %node.value)
        else:
           print("The node %d is not found  " %node.value) 
        del node 
      
    def display(self):
        if self.head:
            print("The elements of the linked list are")
            cur = self.head
            while cur != 0:
                print("%d" %cur.value, end="")
                cur = cur.next 
                if (cur == 0):
                   print("")
                else:
                   print("->", end="")    
        else:
            print("The linked list is empty")
    
    def remove_duplicates(self):
        cur = self.head
        while cur != 0:
           cur1 = cur.next
           prev = cur
           while cur1 != 0:
               if cur.value == cur1.value:
                   prev.next = cur1.next
                   del cur1
                   cur1 = prev.next
               else:
                   prev = cur1
                   cur1 = cur1.next
           cur = cur.next                   
 
 
if __name__=='__main__':
    print("Python program to remove the duplicate entries in the linked list")
    N = int(input("how many nodes?"))
    llist = LinkedList()
    for i in range(N):
        val = int(input("enter the value for the node %d " %(i+1)))
        llist.add(node(val))
    print("The input list is as follows")
    llist.display()
    llist.remove_duplicates()
    print("the linked list after the duplciates removal")
    llist.display()
         
                    