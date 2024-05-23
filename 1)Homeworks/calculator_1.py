def add() :
    c = a+b 
    print ("The result is---->",c)

def sub() :
    c = a - b 
    print ("The result is---->",c)
    
def multiply() :
    c = a *b
    print ("The result is---->",c) 

def div() :
    while a != 0 and b != 0:
        if d.lower() == "a" :
            c = a /b
        else :
            c = b / a
    print ("The result is---->",c)


a = int (input("Enter number----->"))

b = int (input ("Enter another number----> "))

v =( input ("""What do you want to perform
           1) Add
           2)Subtract
           3)Multiply
           4) Divide
            ------>"""))

if v.lower() == "divide":
    d = input ("What do you want to divide with a/b or b/c")
    
elif v.lower() == "add" or v == "1" or v == "+":
    add()

elif v.lower() == "subtract" or v == "2" or v == "-" :
    sub()

elif v.lower() == "multiply" or v == "3" or v == "*" :
    multiply()

elif v.lower() == "divide" or v == "3" or v == "/":
    div()

else :
    print ("Error")