#os module has listdir fuction which returns list of contents of specified directory
#if directory has not specified during function call, it will return list of content form current directory
#https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files


import os 
for file_name in os.listdir():
        print(file_name)
