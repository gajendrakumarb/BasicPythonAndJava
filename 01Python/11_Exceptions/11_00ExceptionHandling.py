'''
# Play Guess game with computer

import random
comnum = random.choice(range(1,11))
while(True):
    print('Play the guess nummber game or press e for \'exit\'')
    num = input('enter any number between 1 and 10\n')
    if(num =='e'):
        break
    num = int(num)  #if user enter any string other than e or number, this statement will throw value error
    if(num < 0 or num > 10):
        print(f'You have entered invalid number.')
    if(num == comnum):
        print(f'Congrats..!!Matched with computer guess..!!')
        break
    else:
        print('wrong.. guess again..!!')

print(f'computer num was {comnum}')
print('Thanks for playing the guess game')

'''
#there are various types of error value error, io error, etc.
#we can catch these error or exceptions in try catch block so we can write clean code

'''

try:
    text = input('Write anything on keyboard--> ')
except EOFError:
        print('Why did you do an EOF on me?')   # Press ctrl + d
except KeyboardInterrupt:
    print('You cancelled the operation.')   # Press ctrl + c
else:
    print(f'You entered \'{text}\' on keyboard')

'''

# Raising an exception
# We can raise exceptions using the raise statement by providing the name 
# of the error/exception and the exception object that is to be thrown.

'''
class ShortInputException(Exception):   #A user-defined exception class. 
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter anything on keybaord greater than 3 letters --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Why did you do an EOF on me?') # Other work can continue as usual here
except ShortInputException as ex:
    print(('ShortInputException: The input was length of' + '{0} , expected at least {1}').format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

'''

# try finally

# finally will run and of try block regardless of try except block  and even after exit method

try:
    j= int(input('Enter any num '))
    i = 1/j 
    print(f'reciprocal of {j} is {i}')
    #exit()
except Exception as ex:
    print(ex)
    #exit()
finally:
    print('we are in finally')


# suppose we are reading a file. 
# How do we ensure that the file object is closed properly whether or not an exception was raised? 
# This can be done using the finally block.

'''
import sys
import time
f = None
try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
        print("(Cleaning up: Closed the file)")
'''

# we can use 'with' for file handling for cleaner code rather than try finally