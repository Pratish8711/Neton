#Just a Small Trick To Have Fun

a = int ( input ("Enter any number between (1 - 20) = \n"))

A = input ( "Enter any name = \n")

if a > 0 and a<=20 :
    num_1 = a + 5

    print ("Adding 5 , We get {}\n".format(num_1))

    num_2 = num_1 * 2

    print (f"Mutiplying it with 2 , We get {num_2}\n")

    num_3 = num_2 - 2

    print ( f"Subtracting it with 2 , We get {num_3}\n")

    num_4 = num_3 /  2

    print ( "Half the number will be , We get {}\n".format (num_4))

    num_5 = num_4 - a

    print ( f"At last, The result will be {num_5}\n")

    print ( f"Is that what you got HuH?? {A}\n")

else :
    print (f"Learn English kid...Mr/Mrs.{A}")