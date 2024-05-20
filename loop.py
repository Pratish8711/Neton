# This is the signup panel

username = input ("What do you want to add your username?? \n")
password = input ("What do you want to make your password = \n")
while not len (password)>=8 and password.isalnum():
    print ("Please Enter a valid password")
    password = input ("What do you want to make your password = \n")

        
else:
    #This is the login panel
    if len (password)>=8 and password.isalnum():
        print ("Successful signup..Returning back \n")
        print ("Hello ! Please login \n")

        username_1 = input ("Enter your username = \n")
        password_1 = input ("Enter your password = \n")

        while not username == username_1 and password == password_1:
            print ("There seems like there is an error..\n Please Check your user name and password")
            password_1 = input ("Enter your password = \n")
        
        else :
            if username == username_1 and password == password_1:
                print ("Successful Login \n")



    



