class node:
    def __init__(self,value):
        self.value = value
        self.next = None


def add(first , node):
    if( first == None):
       first = node
       return first
    cur = first
    while (cur.next != None):
         cur = cur.next
    else:
         cur.next = node
    return first     

def delete(first, value):
    prev = first
    cur = first
    while (cur != None and cur.value != value):
         prev = cur
         cur = cur.next
    else:
        if (cur == None):
            return None
        elif (prev == cur):
            first = cur.next
            del prev
            return first
        else:
            prev.next = cur.next
            del cur
            return first    
            
def display(first):
    if (first == None):
        print("empty Linked List")
    else:
        print("The Linked list content are as follows")
        while (first != None):
            print("%d" %first.value, end="")
            first = first.next
            if (first == None):
                print("")
            else:
                print("->", end="")    
             

def reverse(first):
    if (first == None):
        print("empty Linked List")
        return first
    else:
        rev_head = first
        prev = None
        while(first.next != None):
            first = first.next
            rev_head.next = prev
            prev = rev_head
            rev_head = first
        else:
            rev_head.next = prev     
        return rev_head    



def rev_recursion(first, rh):
    if (first == None):
       print("empty Linked List")
       return None, None
    elif (first.next == None):
       return first, first
    else:
       rev_head, rhead = rev_recursion(first.next, rh)
       rev_head.next = first
       return first, rhead
   
        
if __name__=='__main__':
    print("Python Linked List program")
    first = None
    while(True):
        print("Choose the operation")
        print("1-Display")
        print("2-Add value to linked list")
        print("3-Delete the value from linked list")
        print("4-Reverse a linked list")
        print("5-Reverse a linked list by recursion")
        print("Press any other key to exit")
        choice=int(input(""))
        if (choice == 1):
            display(first)
        elif (choice == 2):
            value = int(input("Enter the value to add"))
            first = add(first, node(value))
        elif(choice == 3):
             value = int(input("enter the value to delete"))
             ret = delete(first,value)
             if ret != None:
                print("The node value %d Successfully deleted" %value)
                first = ret
             else:
                print("The node value %d Not found in the list" %value)
        elif(choice == 4):
             first =  reverse(first)
             display(first)
        elif(choice == 5):
             tmp = first
             rev_head, first = rev_recursion(first, None)
             tmp.next = None 
             display(first)             
        else:
            print("program terminates") 
            break        
                
                                  