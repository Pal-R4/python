n=int(input("enter n:"))
for i in range(1,n+1):
    for j in range(i):
         print(chr(j+65),end="")
    print()