# Local Variable

# Global Variable

# NonLocal Variable

def s () :
    global a
    a=10 
    print ("The value of a in s function is ; " ,a)

def z () :
    print ("The value of a in z is;" ,a)

s ()

z()
