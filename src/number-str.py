
def create_below_twenty_str():
    num = list()
    num.append("")
    num.append("One")
    num.append("Two")
    num.append("Three")
    num.append("Four")
    num.append("Five")
    num.append("Six")
    num.append("Seven")
    num.append("Eight")
    num.append("Nine")
    num.append("Ten")
    num.append("Eleven")
    num.append("Twelve")
    num.append("Thirteen")
    num.append("Fourteen")
    num.append("Fifteen")
    num.append("Sixteen")
    num.append("Seventeen")
    num.append("Eighteen")
    num.append("Nineteen")
    return num
  
def create_twodig_str():
    num = list()
    num.append("")
    num.append("")
    num.append("Twenty")
    num.append("Thirty")
    num.append("Forty")
    num.append("Fifty")
    num.append("Sixty")
    num.append("Seventy")
    num.append("Eighty")
    num.append("Ninety")
    return num 

def convert_twodigit_str(num):
    t1 = create_twodig_str()
    t2 = create_below_twenty_str()
    if num < 20:
        return t2[num]
    else:
        return t1[num//10]+" "+t2[num%10]

def convert_num_string_below_crore(num):
    l = len(num)
    st = ""
    if l == 7 or l == 6:
       if l == 7:
          tmp = int(num[:2])
          s = "lakhs "
          l-=2
          num=num[2:]
       else:
          tmp = int(num[0])
          s = "lakh "
          l-=1
          num=num[1:]
       if tmp != 0:    
          st +=  convert_twodigit_str(tmp)+" "+s
    if l == 5 or l == 4:
       if l == 5:
          tmp = int(num[:2])
          l-=2
          num=num[2:]
       else:
          tmp = int(num[0])
          l-=1
          num=num[1:]
       if tmp != 0:              
          st +=  convert_twodigit_str(tmp)+" thousand "       
    if l == 3:
       tmp = int(num[0])
       l-=1
       num=num[1:]
       if tmp != 0:
          st +=  convert_twodigit_str(tmp)+" hundred "                
    if l > 0 and l <= 2:
       st += convert_twodigit_str(int(num))
    return st


def convert_num_str(num):
    l = len(num)
    if l > 7:
       return  convert_num_str(num[:l-7])+" Crores "+ convert_num_string_below_crore(num[l-7:])
    else:
       return  convert_num_string_below_crore(num)              
    
if __name__ == "__main__":
   print("Python program to convert the input number in to English description")
   num = input("Enter the number: ") 
   if num.isdigit():
       print("The number : %s" %convert_num_str(num))
   else:
       print("Invalid input , Enter only positive integer")    
  
    