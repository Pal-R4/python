def romanDec(rno):
 rdict ={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
 rback = list(rno)[::-1]
 value = 0
 rval = rdict[rback[0]] 
 for i in rback:
  lval = rdict[i]
 if lval < rval:
  value -= lval
 else:
  value += lval
 rval = lval
 return value
Rval = input("Enter a Roman Number : ")
print("Equivalent Decimal number :",romanDec(Rval))