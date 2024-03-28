n=int(input("enter n"))
if n>1:
    for i in range(2,int(n/2)+1):
        if(n%i)==0:
            print(n)
            start=int(input("enter start"))
            end=int(input("enter end"))
            for i in range(start,end+1):
                if n>1:
                    for i in range(2,n):
                        if(n%i)==0:
                            print("numbers are",n)
                    

