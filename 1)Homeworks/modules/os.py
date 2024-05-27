# OS Module

# --> OS ( Operating System)

# --> Interaction with windows system directory 

import os

# Creat Dir

# List Dir

# Remove Dir


#                                       To Create

# os.getcwd()

# # cwd --> current working dir

# a = "Test"

# location = "E:/Python-Codes/Neton"

# path = os.path.join(location,a)

# os.mkdir(path)


#                                   To Remove

# file = "Test"

location = "E:/Python-Codes/Neton"

path = os.path.join (location)

# os.rmdir (path)

print (os.listdir(path))