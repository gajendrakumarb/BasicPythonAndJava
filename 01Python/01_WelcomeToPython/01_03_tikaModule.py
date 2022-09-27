# Prints only text files present in Folder
# import os 
# for x in os.listdir():
#     if x.endswith(".txt"):
#         print(x)


# Read text file using open function
# with open('01_03_InstallModuleandUse.txt') as mytxt:
#     for line in mytxt:
#         print (line)

# using open, we can not read pdf file thus we will use tika
# with open('byte-of-python.pdf') as mytxt:
#      for line in mytxt:
#          print (line)

# pip install tika
from tika import parser 
rawtxt = parser.from_file('byte-of-python.pdf')
print(rawtxt['content'])

# 2022-08-28 11:38:40,015 [MainThread  ] [ERROR]  Unable to run java; is it installed?

# Installed Java runtime (OpenJDK) to run tika
# Rerun line 19 to 21 and we read pdf!!