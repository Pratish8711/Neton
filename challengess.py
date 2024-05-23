# Minutes into Seconds

minutes = int (input ("Enter The Time in Minute --->"))

second = minutes * 60 

print ("The time in seocnd is  ----> " , second)

# Challenge no.2

n =  int  (input  ("Enter any number 1-100 -->"))

if n >= 1 and n <=100 :
    if n % 2 != 0 :
        print ("Weird")

    elif n % 2 == 0 and n <= 2 and n>= 5:
        print ("Not Weird")

    elif n % 2 == 0 and n <=6 and n>= 10 :
        print ("Wierd")