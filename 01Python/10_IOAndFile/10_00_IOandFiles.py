#WAP to check entered text is palindrome or not  

def reverseText(enteredText):
    return enteredText[::-1]    #defalut step is 1, wheh we state step as -1 it reverses the string

def is_palindrome(enteredText):
    return enteredText == reverseText(enteredText)

enteredText = input("Enter text to check palindrome: \n") #input from user using input inbuilt function which return value as string
if is_palindrome(enteredText):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

#File reading and writting to the file
poem = '''
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
f = open('poem.txt', 'w')   # Open for 'w'riting if given file is not there it will create file
f.write(poem)   # Write text to file
f.close()   # Close the file
# If no mode is specified, 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline() #reading line by line
    if len(line) == 0:    # Zero length indicates EOF
        break
    print(line, end='') # The `line` already has a newline at the end of each line since it is reading from a file.
# close the file
f.close()

#WAP to write multiplication table of user's choice number in sample.txt

#We can only have exactly one of create/read/write/append mode cant have multiple

with open('sample.txt') as f:   #using with we do not need to close file, it will automatically gets called
    content = f.read()
    print(content) #Reading previous content of sample.txt

with open('sample.txt','w') as f:   #using with we do not need to close file, it will automatically gets called
    
    i=1
    num = int(input("enter number to print its multiplication table\n"))
    while i < 11:
        line = str(num)+ ' X ' +str(i)+ ' = ' +str(num*i)
        print(f'this is line{i}'+line)
        f.write(f'{num} X {i} = {num*i} \n')
        i+=1

with open('sample.txt','r') as f:
    content = f.read()
    print(content) #Reading after writting into sample.txt



#unicode
# to read non english content of the file

# encoding=utf-8
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"ऑस्ट्रेलियाचा सहा विकेट्स राखून पराभव करत मालिका 2-1 अशी जिंकली")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)