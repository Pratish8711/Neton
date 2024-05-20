# Functions
def signup ()  :
   global user_name
   global pass_word
   user_name =  input ("Enter a username ---->")

   pass_word = input ("Enter a strong password --->")

   while not len (pass_word)>=8 and pass_word.isalnum():
    print ("Please Enter a valid password")
    pass_word = input ("Enter a strong password --->")

   else:
      print ("Successful Signup...Redirecting you to Main Page")
      
def login() :
   username = input ("Enter your username ---->")

   password = input ("Enter your password ---->")

   if username == user_name and password == pass_word :
      print ("Welcome Access Approved")
   else :
      print ("Wrong password or username Please Retry later")

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

   else :  
      print ("Error 404")

   a = input("Do you want to start over or terminate this program??(Yes/No)")

   if a.lower() == "yes" :
      b = True

   else  :
    b = False

else :
   print ("Thank you for using This Program")