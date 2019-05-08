import re


if __name__ == '__main__':
   msg = "inet addr:172.28.4.1  Bcast:172.28.7.255  Mask:255.255.248.0" 
   inetaddr = re.search('inet addr:(.*) (.*)', msg).group(1)
   print ("inetaddr= "+inetaddr)
   lst = re.split(':',msg)
   lst1 = lst[1].split()
   print (lst)
   print(lst1[0])
    