count = 0

print ("This is a Quiz \n")

print ("This is the first question \n")

print ("A) What is the smallest country in this world?\n")

print ("""1> Nepal         2> USA
    3> Vatican City  4> India""")

while count < 3:

    a = input ()
    if a == 3:
        print ("Correct Answer")
        
        print ("B) How many countries are there in this world?")

        print ("""1> 195     2> 200
                  3> 197     4> 199""")
        a = input ()
        
        if a == 1:
            print ("Right Answer")
    else :
        count += 1
        
    break


