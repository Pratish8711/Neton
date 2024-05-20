# A simple calculater 

a=float(input("enter a number:"))
op=input("enter the operator:")
b=float(input("enter the second number:"))
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("invalid")
    