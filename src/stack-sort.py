class stack:
    def __init__(self):
        self.st = list()
       
    def push(self, val):
        self.st.append(val)
       
    def pop(self):
       return self.st.pop()
   
    def top(self):
        return self.st[-1]
    
    def display(self, msg):
        print(msg)
        print(self.st)
 
    def len(self):
        return len(self.st) 
 
def get_min(fr, to):
    min = fr.pop()
    size = fr.len()
    for i in range(size):
        if min < fr.top():
           to.push(fr.pop())
        else:
           to.push(min) 
           min = fr.pop()
    return min

def stack_sort(st1, st2, st3):
    size = st1.len()
    for i in range(size):
        min = get_min(st1,st2)
        st3.push(min)
        tmp = st1
        st1= st2
        st2 = tmp
         
if __name__ == "__main__":
    print("Python program to do sorting using stacks")
    N = int(input("How many elements"))
    st1 = stack()
    for i in range(N):
        val = int(input(" [index : %d] Enter the value to push" %(i+1)))
        st1.push(val)
    st1.display("Input stack is as follows")
    st2 = stack()
    st3= stack()
    stack_sort(st1, st2, st3)
    st3.display("The storted stack is as follows") 
                                     