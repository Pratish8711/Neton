# List datatype

# a= ["a" , "a" , 'b' , "b" , "c" , "c"]
# l = ["Dog" , "Cat" , "Banana" , "Apple"]

# p = 0 - Just a variable 
# q = 0 - Just a variable
# r = 0 - Just a variable

# for i in a : - This will count the number of items in a loop
#    if i in a:
#        p += 1


# print (f"The number of a in this statement is {p} and the number of b in this statement is {q} and finally the number of c in this statement is {r}")

# print (a[0:]) - This will display all the items in the list

# print (len (a)) - This will count thr numbers of items in the list

# l.insert( 0 , 'Cat') - This will instert new item in the list



# p = l + a - This will add 2 lists together

# print (p) - This will display that added list

# l.remove ("Dog") - This will remove the item in the list named Dog

# l . pop (0) - This will remove the item in the position of 0

# l.pop () - This will remove the last item in the list 

# del l[0] - This will delete the item in the list with the given location

# del l - This will delete the whole list

# l.clear () - This will clear the whole list and make it empty

# print (l.clear()) - The upper list will display [] this when u print it

# l = []

# # for i in a:
# #     if i not in l:
# #         l.append(i)

#  print (l)
# s = "abacdcab"

# l = [i for i in s if (i not in s)]

# print (l)

# List Sorting

# l = ["o" , "a" , "b" , "e"]

# l.sort()

# l.sort (reverse=True)

# l.sort(key=str.lower)

# l.reverse()

# # l2 = l.copy()

# # l2 = list(l)

# l2 = [1,2,3]

# l.extend(l2)
# print (l)

# del(l)

# print (l)

# l = [1,3,5,7,5,6]

# for i in l:
#     if i == 5 :
#         l.remove(i)

# print (l)


files = ['song.mp3' , 'video.mp4' , 'doc.pdf', 'song1.mp3' , 'video1.mp4']

for i in files:
    if i.endswith(".mp3"):
        print (i)
    


    
