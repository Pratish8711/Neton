
def verify() :

    global Items
    global admins

    identity = input ("Are you an Admin or a Customer?? -->>")

    if identity.lower() == "admin" :

        id = input ("Enter Your Id ----->>")

        pas = input ("Enter Your Password ---->>")

        for x,y in admins.items() :

            if x == id and pas == y :

                b = True

            else :

                b = False

            if b :


                print("""As You Are The Admin You Can Do The Following Things ----->
                    1) Add Items To The List
                    2) Remove Items From The List 
                    3) Update Items From The List  """)
                
                ad = input ("What  do you want to do ----->>")

                if ad.lower() == "add" or ad == "1" :
                        
                    add = input ("Enter What Do You Want To Add ------>>")

                    quantity = int ( input ( "How Much Do You Want To Add per / kg or per / liters ----->>"))

                    Items.update({add : quantity } )

                elif ad.lower() == "remove" or ad == "2" :

                    for x , y in Items.items() :

                        print (x , ":" , y)
                            
                    remove = input ("What Do You Want To Remove?? ----->>")

                    Items.pop (remove)


                elif ad.lower() == "update" or ad == "3" :

                    for x , y in Items.items() :

                        print (x , ":" , y)
                        
                    change = input ("Enter Which Item Do You Want To Change ---->")

                    update = input (f"Enter What Do You Want To Change {change} into ?? ------>>")

                    Items [change] = update


            elif identity.lower() == "customer" :
                    
                pass 

            else :
                print ("Sorry You Entered Wrong Role")

        else :
            print ( "Wrong Password or Id!!")

