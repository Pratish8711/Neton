#                                                              A Project For Filtering MP3 Files

import os 

dir_list = []

path = "C:/Users/Dell/Downloads"

dir_list = os.listdir(path) 

for name in dir_list :
    if name.endswith('.mp3'):
    
        print (name)
