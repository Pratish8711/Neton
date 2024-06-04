import os

import datetime


def signup () :

    #                                           Welcoming Screen

    print ("""                      Welcome To The Signup Panel         """)

    #                                           Input IDs

    username = input ("Enter Your Username ---->>>")

    print ("The Password must be 8 character long and must include a number")

    password = input ("Enter A Suitable Password  ----->>>")

    while not len (password)>=8 and password.isalnum():
        print ("Please Enter a valid password")

        password = input ("Enter a strong password --->")

    else:

        print ("Successful Signup...Redirecting you to Main Page")

        signup_file = open (f"E:/Python-Codes/Neton/signup records/{username}" , "w")


        signup_file.write (f"{username} : {password}")

        signup_file.close()
     

def login () :


    #                                       Welcoming Screen

    print ("""                          Welcome To Login Panel """)

    #                                       Input IDs

    user_name = input ("Enter your username ---->>")

    pass_word = input ("Enter your passwordd --->>")

    path = open (r"E:\Python-Codes\Neton\signup records" , "r")

    ls = os.listdir(path) 

    if user_name in ls:

        login_record = open (f"E:/Python-Codes/Neton/signup records/{user_name}" , "r")

        for line in login_record:
            
            stored_username, stored_password = line.strip().split(":")

            if user_name == stored_username and pass_word == stored_password:
                
                print("Welcome! Accessing your data.")

                record = open (f"E:/Python-Codes/login records/{user_name}" , "a")

                record.write (datetime.datetime.now)

                record.close()

            login_record.close()

        else : 
         
         print ("Wrong PassWord OR UserName")
        


while True  :

        #                                   Welcoming Screen

        print ("""                              Welcome To Our Site!! 
                                            Please Login Or Signup """ )

        #                                   Modules

        choice = input ("What do you want to do?? (Login Or Signup)").strip().lower()

        if choice == "login" :

            login()

        elif choice == "signup" :
            
            signup()

        else :

            print ("Error 404")

        repeat = input ("Do you want to repeat??(Yes/ No) -->>").strip().lower()


        if repeat == "yes" :
             
             pass   
        
        else :
             
             break
        
else :
     
     print ("Thank you for visiting our Site")
