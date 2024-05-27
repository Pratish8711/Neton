print("\n                             Hello!!!! Welcome To Our Shop NETON..... \n")
print("                                              Here You Can Buy Items in Wholesale And With Good Discount .... \n")

# Admin credentials
admins = {
    'User_Name': "Pratish",
    'Password': "Pratish09"
}

# Item Storage
items = {}

# Price Of Items
price = {
    'Rice': 150,
    'Oil': 100,
    'Salt': 60,
    'Chips': 20,
    'Apple': 60,
    'Banana': 40,
    'Mango': 50
}

# Display Of Items
print("Here are the list of items that are sold at our shop ----------->>>\n")
for item, cost in price.items():
    print(item, ":", cost)


def buy_items():
    cart = {}
    while True:
        choice = input("\nWhat do you want to buy (Enter item name)? ")
        if choice.capitalize() in price:
            quantity = int(input("How much do you want per kg or per liter? "))
            if choice.lower() in cart:
                cart[choice.lower()] += quantity
            else:
                cart[choice.lower()] = quantity
        else:
            print("This Item is not In our Shop! Sorry")
        response = input("Do you want to buy more items? (Y/N): ").lower()
        if response != 'y':
            break
    return cart


def calculate_total(cart):
    total = 0
    for item, quantity in cart.items():
        total += quantity * price[item]
    return total


# Main program
cart = buy_items()
total_cost = calculate_total(cart)

print("\nThank You!! Your Items and The Total Will Be Displayed Shortly .....\n")

# Displaying Items With Quantity with Price
for item, quantity in cart.items():
    print(item.capitalize(), ":", quantity, "/ kg / l ------>> Rs.", quantity * price[item])

print("\nTotal Cost: Rs.", total_cost)
print("Have a great day!")


