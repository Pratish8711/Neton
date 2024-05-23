#A simple Calculator
#Code written By Pratish
def add(x, y,z):
    return x + y+z

def subtract(x, y, z):
    return x - y-z

def multiply(x, y, z):
    return x * y * z

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))

        if choice == '1':
            print("Result:", add(num1, num2,num3))
        elif choice == '2':
            print("Result:", subtract(num1, num2,num3))
        elif choice == '3':
            print("Result:", multiply(num1, num2,num3))
        elif choice == '4':
            print("Result:", divide(num1, num2,num3))
    else:
        print("Invalid input")

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        break
