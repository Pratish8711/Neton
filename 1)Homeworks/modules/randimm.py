import random

error = True

while error :

    ##                                                  Welcoming Screen

    print ("""                                 Hello !!! Welcome To Guess Your Luck  \n  """)
        
    print ("""                                This Game You Will Be Choosing Your Difficulty ,\n 
                                                Then Find Out Your Luck         \n                """)

    chance= True


    ##                                                 Choosing Levels

    level = input (""" Choose Your Difficulty Please 
                ---- 1) Easy   (1 - 5)  ---> The Odds Of you getting it is 1/5
                ---- 2) Normal (1 - 10 ) ---> The Odds Of you getting it is 1/10
                ---- 3) Hard   (1 - 20)  ---> The Odds Of you getting it is 1/20
                ---  Please Choose ------->>>>""")

    ##                                                Level  Wise 

    ##                                               Easy Level (1 - 5) 

    if level.lower() == "easy" or level == "1" :

        for i in range (5) :  

            ran =  random.randint (1  , 5)
        
        print ("    Preparing Your Game    ....... \n ")

        print (""" This is Easy Level which means You Have to guess a number from 1 - 5  \n""")
        
        while chance :
        
            guess = int (input ("Enter your Guess   ----->>>"))

            if guess ==  ran :

                print ("""\n CORRECT GUESS You Wonn  !!!!!    You Can Leave  
                        THANK YOU FOR PLAYING !!!""")

                chance = False
    

            elif  guess < ran :

                print ("\n Ohh..  You Seem To Went Lower Please Higher Up")

            else  :

                print ("\n Ohh..  You Seem To Went Higher Please Lower Down")

        break     

    ##                                               Normal Level (1 - 10)   

    elif level.lower() == "normal" or level == "2" :

        for i in range (5):

            ran =  random.randint (1  , 10)
        
        print ("    Preparing Your Game    ....... \n")

        print (""" This is Normal Level which means You Have to guess a number from 1 - 10 \n""")
        
        while chance :
        
            guess = int (input ("Enter your Guess   ----->>>>"))

            if guess ==  ran :

                print ("""\n CORRECT GUESS You Wonn  !!!!!    You Can Leave  
                        THANK YOU FOR PLAYING !!!""")

                chance = False
    

            elif  guess < ran :

                print ("\n Ohh..  You Seem To Went Lower Please Higher Up")

            else  :

                print ("\n Ohh..  You Seem To Went Higher Please Lower Down")

        break
                
    ##                                              Hard Level (1 - 20)   
 
    elif level.lower() == "hard" or level == "3" :

        for i in range (5) :

            ran =  random.randint (1  , 20)
        
        print ("    Preparing Your Game    .......\n ")

        print (""" This is Hard Level which means You Have to guess a number from 1 - 20 \n """)
        
        while chance :
        
            guess = int (input ("Enter your Guess   ----->>>>"))

            if guess ==  ran :

                print ("""\n CORRECT GUESS You Wonn  !!!!!    You Can Leave  
                        THANK YOU FOR PLAYING !!!""")

                chance = False
    

            elif  guess < ran :

                print (" \n Ohh..  You Seem To Went Lower Please Higher Up")

            else  :

                print (" \n Ohh..  You Seem To Went Higher Please Lower Down")

        break
                
    else :

        print ("THE GIVEN DIFFICULTY IS INVALID!!!! PLEASE RETRY  \n \n \n")
    
        b = False
