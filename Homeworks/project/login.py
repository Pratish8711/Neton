import datetime
#                           This is a Program That Allows the user to input their id and password 
#                               Or Signup or Login


#                                       Welcome Screen      

print ("""                              Hello!!! Welcome To Our Site  
                                            Here You Can Login In To Access Your Files
                                            Or Signup To Create New Files to Add """)

#                                         Input of IDS

# Functions

def signup ()  :


   global file_1
    
   global user_name

   global pass_word

   file_1 = open ("E:/Python-Codes/Neton/files" , "a")

   user_name =  input ("Enter a username ---->")

   pass_word = input ("Enter a strong password --->")


   while not len (pass_word)>=8 and pass_word.isalnum():

    print ("Please Enter a valid password")

    pass_word = input ("Enter a strong password --->")

   else:
      
      print ("Successful Signup...Redirecting you to Main Page")

      file_1.write(f"{user_name}:{pass_word}\n")

      file_1.close()

  


      
def login() :

   global file_2

   file_2 = open ("E:/Python-Codes/Neton/files" , "r")

   username = input ("Enter your username ---->")

   password = input ("Enter your password ---->")

   for line in file_2:
            
      stored_username, stored_password = line.strip().split(":")

      if username == stored_username and password == stored_password:
                
         print("Welcome! Accessing your data.")

      else : 
         
         print ("Wrong PassWord OR UserName")
         
# Main Codes   

b = True

while b:

   choice = input ("""       Welcome To Our Site...Do you want to          
                  Login or Signup 
                  -----> """)


   if choice.lower() == "signup" :

    signup()

    


   elif choice.lower () == "login":

      login()

      file_2.close()


   else :  

      print ("Error 404")

   a = input("Do you want to start over or terminate this program??(Yes/No)")

   if a.lower() == "yes" :

      b = True

   else  :

    b = False

else :

   print ("Thank you for using This Program")

