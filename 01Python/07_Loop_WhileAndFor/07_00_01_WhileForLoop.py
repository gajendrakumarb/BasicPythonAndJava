# Topic : Loops
# In programming language we need to run code snippet repetitivy in one program 
# In python, while and for
# 
# Else block with while and for loop: 
# - else block can be used at the end of 'while' and 'for' loops. 
# - It will only excutes when condition express of 'while' and 'for' does not fullfill.  
# - else block will not run when 'while' or 'for' loop exit with 'break' statment 

# Syntax:
# while <codition>:
#   Do something....


# progam to print 1 to 50
from math import sqrt


i = 1
while i<=50:
    print(i, end=' ')
    i +=1

print()

# ## Guess number while loop 
# run_something = True
# num= 23
# while  run_something:
#     guess_num = int(input("Guess number(0<num<50) that is stored : "))
#     if(guess_num==num):
#         print('Congrats You gessed it')
#         run_something = False # this statment breaks the loop
#     elif(guess_num<num):
#         print('Nope. Its higher that this num')
#     else:
#         print('Nope. Its lower that this num')

# else:
#     print("While loop is over")

#loop through list
print('printing list one by one item using while loop')
i= 0
list1 = [2,5,7,9,34,8]
while i<len(list1):
    print(list1[i],end=' ')
    i += 1
print()

#In python, for loop mainly is used to iterate through sequance object like tuple list string etc.
print('printing list one by one item using for loop')

for item in list1:
    print(item, end=' ')

print()


# range function is one of the way to iterate loop with specific number of time

# range(start_num, end_end, incremental step from start to end where end is not included)
# range(int) points to start = 0 to end = int -1

num = int(input('Enter the number to print mulipication table\n'))
for i in range(1,11):
    #print(num*i,end=' ')
    #print(str(num)+' X '+ str(i)+' = '+str(num*i))
    print(f"{num} X {i} = {num*i}")


# break
# break statment exits current loop at that iteration and line 


# continue
# continue statment skips statement below in the current iteration of the loop and goes for next iteration of the loop


# wap find first four prime numbers for 10 to 50
p =1
prime = False
for q in range(10,50):
    if(p>10):
        break
    #print(q)
    for r in range(2, int(sqrt(q))+1):
        if(q%r==0):
            #print(f'{r}', end=' ')
            prime = False
            break
        else:
            prime= True
    if(prime):
        print(f'{p} prime between 10 and 50 is {q} {r}')
        p +=1
        

#pass
# 
#pass is null statement it does nothing 
# 
i = 4
if i<0:
    pass   

i =2
while i<10:
    pass

def funDoSomthing(cricketplayer): #will define later
    pass

# pass helps to escape error for unwritten code logic for various code blocks



