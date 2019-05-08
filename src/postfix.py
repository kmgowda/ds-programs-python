import re
def pr_exp(ch):
    pr={'+':1, '-':1,'*':3,'/':3,'%':3,'^':6, '**':6, '(':9,')':0}
    return pr.get(ch,7)

    
def pr_st(ch):
    pr={'+':2, '-':2,'*':4,'/':4,'%':4,'^':5,'**':5,'(':0,'#':-1}
    return pr.get(ch,8)


def infix_postfix(exp):
    tmp = re.split('(\+|\-|\*|\/|\(|\)|\^|\%)',exp)
    lt = filter(None,tmp)
    st = list()
    st.append('#')
    out=""
    outlt=list()
    for item in lt:
        while pr_st(st[-1]) > pr_exp(item):
            top=st.pop()
            out+=top+' '
            outlt.append(top)
        if pr_st(st[-1]) != pr_exp(item):
            st.append(item)
        else:
            st.pop()
    while st[-1] != '#':
            top=st.pop()
            out+=top+' '
            outlt.append(top)                    
    return out,outlt

def is_operator(ch):
    if ch =='+' or ch =='-' or ch == '*' or ch == '/' or ch == '%' or ch == '^':
        return True
    else:
        return False 

def operate(op, one, two):
    if op == '+':
        return one+two
    if op == '-':
        return one-two
    if op =='*':
        return one*two
    if op =='/':
        return one//two
    if op =='%':
        return one%two
    if op =='^':
        return one**two  

   
    
def eval_postfix(lt):
    st = list()
    for item in lt:
        if is_operator(item):
            two = st.pop()
            one = st.pop()
            val= operate(item, one, two)
            st.append(val)
        elif item.isdigit():
            st.append(int(item))
        else:
            val = int(input("enter the integer value for %s: " %item))
            st.append(val)    
    return True, st.pop()
              
if __name__=="__main__":
   print("Python program to convert infix expression to postfix expression")
   st=input("Enter an expression")
   out, outlt=infix_postfix(st)
   print("The postfix expression : "+out)
   print("The postfix expression in list ")
   print(outlt)
   res, val = eval_postfix(outlt)
   if res:
       print("The output : %d" %val)
   else:
       print("Invalid expression ")    
    
        
    
                

