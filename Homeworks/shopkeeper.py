# This program displays you the list of items and asks you to enter the number of items and the name of item which is to be calculated and shown the price at last

print ("Hello!! Welcome to our Grocery Store  -------->")

items = ["Rice", "Oil" , "Soap" , "Face Wash"]

price = [100 , 160 , 30 , 250]

print ("The items and the prices of the items are shown down below ---->")

print (items)

print (price)

item_2 = input ("Enter what items do you want to buy -----> " ,)
item_1 = item_2.lower()

quantity = float(input ("How many do you want to buy -----> ",))

if item_1 == "rice" or item_1 == "oil" or item_1 == "face wash" or item_1 == "soap":

    if item_1 == "rice" :
        price_1 = 15/100 *(100 * quantity )    
        print ("The Price will be --> Loading ....", price_1)

    if item_1 == "oil" :
        price_1 = 15/100 *(160 * quantity )    
        print ("The Price will be --> Loading ....", price_1)

    if item_1 == "soap" :
        price_1 = 15/100 *(30 * quantity )    
        print ("The Price will be --> Loading ....", price_1)

    if item_1 == "face wash" :
        price_1 = 15/100 *(250 * quantity )    
        print ("The Price will be --> Loading ....", price_1)

else :
    print ("Sorry I don't think We sell that item")


print ("Thank You For Visiting Our Store.....Please do Visit Again :D")
