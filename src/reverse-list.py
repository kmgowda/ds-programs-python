
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self, msg):
        cur = self.head
        print(msg)
        while cur != None:
            print("%d" %cur.data, end="")
            if cur.next == None:
               print("")
            else:
               print("->", end="")
            cur = cur.next   
    
    def add(self, node):
        cur = self.head
        if cur == None:
            self.head = node
        else:        
            while cur.next != None:
                  cur = cur.next
            cur.next = node      
    
    def reverse(self):
        cur = self.head
        rev = None
        while cur != None:
            tmp = cur
            cur = cur.next
            tmp.next = rev
            rev = tmp
        self.head = rev

    def reverse_list(self, cur):
        if cur.next == None:
            return cur
        else:
            rhead = self.reverse_list(cur.next) 
            if rhead.next == None:
                rhead.next = cur
            else:
                cur.next.next = cur
            cur.next = None
            return rhead
        
    def rcur_reverse(self):
        self.head = self.reverse_list(self.head) 



if __name__=='__main__':
    print("Python program to reverse a linked list")
    N = int(input("How many elements?"))
    llist=LinkedList()
    for i in range(N):
        val = int(input("Enter the value for the node %d" %(i+1)))
        llist.add(node(val))
    llist.display("The input linked list ")
    llist.reverse()
    llist.display("The reversed linked list ")
    llist.rcur_reverse()
    llist.display("The linked list after recursive reverse")    
        

                                             