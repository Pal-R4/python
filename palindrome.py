n=input("enter the string")
length=len(n)
for i in range(0,(length/2)+1):
 if n[i]!=n[-i-1]:
  break
 if i<int(length/2):
   print("not palindrome")
 else:
  print("palindrome")
               