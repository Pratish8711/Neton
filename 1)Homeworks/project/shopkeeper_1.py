# THIS IS A PROGRAM TO TAKE ITEMS AND THEN FIND OUT THE PRICE OF IT WITH SOME TWIST


#                                                               Welcoming Screen

print ("""                 \n                             Hello!!!! Welcome To Our Shop NETON..... \n               """)

print ("""                                              Here You Can Buy Items in Wholesale And With Good Discount .... \n """)

#                                                            ID PASSWORD Storage

admins = {
    
    'User_Name' : "Pratish" ,
    'Password' : "Pratish09"
    

} 


#                                                              Item Storage

Items = { 
    'Items Name': " Quantity " ,
}

#                                                               Price Of Items

Price = {
    'Rice' : 150 ,
    'Oil'  : 100 ,
    'Salt' : 60 ,
    'Chips' : 20 , 
    'Apple' : 60 ,
    'Banana' : 40 ,
    'Mango' : 50 

}



#                                                              Verification


identity = input("Are you an Admin or a Customer?? -->> ").strip().lower()


if identity == "admin":

    id = input("Enter Your Id ----->> ").strip()

    pas = input("Enter Your Password ---->> ").strip()

    if id in admins and admins[id] == pas:

        print("""As You Are The Admin You Can Do The Following Things ----->
                1) Add Items To The List
                2) Remove Items From The List 
                3) Update Items From The List""")
        

        ad = input("What do you want to do (add/remove/update)? ----->> ").strip().lower()


        if ad == "add" or ad == "1":

            add = input("Enter What Do You Want To Add ------>> ").strip()

            quantity = int(input("How Much Do You Want To Add per/kg or per/liters ----->> "))

            Items[add.capitalize()] = quantity

            print(f"Added {quantity} kg/l of {add.capitalize()}")

        elif ad == "remove" or ad == "2":

            for item, qty in Items.items():

                print(f"{item}: {qty}")

            remove = input("What Do You Want To Remove?? ----->> ").strip().capitalize()

            if remove in Items:

                Items.pop(remove)

                print(f"Removed {remove}")

            else:

                print(f"{remove} is not in the item list.")

        elif ad == "update" or ad == "3":

            for item, qty in Items.items():

                print(f"{item}: {qty}")

            change = input("Enter Which Item Do You Want To Change ----> ").strip().capitalize()

            if change in Items:

                update = int(input(f"Enter the new quantity for {change} ------>> "))

                Items[change] = update

                print(f"Updated {change} to {update} kg/l")

            else:

                print(f"{change} is not in the item list.")

        else:

            print("Invalid option selected.")

    else:

        print("Wrong Password or Id!!")



elif identity.lower() == "customer" :
                    
        pass 

else :
           
            print ("Sorry You Entered Wrong Role")

#                                                                Display Of Items

print ("""Here are the list of items that are sold at our shop ----------->>>\n""")

for x,y in Price.items() :

    print (x ,":" ,y)

#                                                          Input Of Items 

while True:

    choice = input("\nWhat do you want to buy ---->> ").strip().capitalize()

    if choice in Price:

        quantity = int(input("How much do you want per/kg or per/l ---->> "))

        if choice in Items:

            Items[choice] += quantity

        else:

            Items[choice] = quantity

        ask = input("Do you want to buy more items? (Y/N) -----> ").strip().lower()

        if ask != 'y':

            break

    else:

        print("This item is not in our shop! Sorry")


print("\nThank You!! Your Items and The Total Will Be Displayed Shortly ..... \n")


                                         


#                                                    Displaying Items With Quantity with  Price 

total = 0

for item, qty in Items.items():

    if item in Price:

        cost = qty * Price[item]

        total += cost

        print(f"{item}: {qty} kg/l ------>> Rs. {cost}")


print(f"\nTotal Bill: Rs. {total}")


