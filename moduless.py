# Modules is the collection of function , class and variable 

# Import functions from the file name ppo.py

import ppo as cal
# A Variable For Loop

b = True

# Loop So That The User Will Be Able To Redo All The Performance

while b: 

    # Taking Numbers

    num_1 = float (input ("Enter the first number ---->"))

    num_2 = float (input ("Enter the second number ---->"))

    num_3 = float (input ("Enter third number --->"))

    # Taking Choice Either To Add , Subtract , Multiply or Divide

    choice_1 = input ("""What would you like to perform
                  1)Add --> +
                  2)Subtract --> -
                  3) Mutiply --> *
                  4) Divide --> /""")

    # Conditional Statement
    if choice_1.lower() == "add" or choice_1 == 1 or choice_1 == "+" :
     print ( cal.add())

    elif choice_1.lower() == "subtract" or choice_1 == 2 or choice_1 == "-" :
     print ( cal.sub())
    elif choice_1.lower() == "mutiply" or choice_1 == 3 or choice_1 == "*" :
     print ( cal.mutiply())

    elif choice_1.lower() == "divide" or choice_1 == 4 or choice_1 == "/" :
        print ( cal.division())

    else:
        print ("Sorry It is Not In The Given Choice Above ")
    

    #This is for the restart

    l = input ("Do you want to start over again (Yes / No)??  ---->")
    
    if l.lower() == "yes" :
    
       b = True

    else :
    
       b = False


    
