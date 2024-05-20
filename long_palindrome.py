# This is the long and not so best version of palindrome
# Written By Pratish
a = int(input ("Enter any number = \n"))

n = a

s = 0

while n!=0 :
    r = n % 10
    #This line finds the reminder of the number you entered while it is divided by 10
    s = (s * 10) + r
    #This line stores the number in reverse
    n = int (n/10)
    #This line finds the integer value of the number you entered

if a == s :
    print (f"The number {a} is Palindrome")

else :
    print (f"The number {a} isn't Palindrome")