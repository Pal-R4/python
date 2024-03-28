s=int(input("enter s"))
e=int(input("enter e"))
sum=0
for num in range(s,e+1):
 if num%2!=0:
        sum=sum+num
print("sum=",sum)        
