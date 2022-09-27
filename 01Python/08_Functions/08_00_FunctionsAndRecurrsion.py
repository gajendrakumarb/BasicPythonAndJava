# Topic Functions
# Functions are reusable code snippet.

# there are built-in functions and user defined functions.
# range(), str(), int(), print() etc. are build-in function. 
def say_hello():
    print("Hello")

say_hello()
say_hello()
say_hello()

#find greater of two numbers

def print_max(a,b):
    if(a>b):
        print(a,' is greater than ',b)
    elif(a==b):
        print(a,' is equal to ',b)
    else:
        print(a,' is smaller than ',b)

# calling function and pass literal directy into function
print_max(13,5)

#passing varibales as arguments
x = 18
y = 83
print_max(x,y)


# defalut argument funtions
def print_sayhello(name='Stranger'):
    print(f'Hello {name}')

print_sayhello('Sam')
print_sayhello()


#local varibles

# x = 'sam'   # create x varible at with local binding
# def print_name(x):   # create x varible at with local binding
#     print('x is '+x)
#     x = 13
#     print(f'changed x in function to {x}')

# print_name(x)
# print(f'x outside fun still : {x}')

# Globle variable

x = 'sam'
def print_name(): #def print_name(x): #"x" is assigned before global declarationPylance at line 43(current line + 2) i.e
    #print('x is '+x) # can not create x varible at with local binding as we are going use x as global var 
    #global x          # throws error as it x was used before declaring it as global var
    x =14
    print(f'changed x in function to {x}')

print_name()
print(f'x outside function also changes : {x}')


#return statements
# return statment returns the value of the code


#Recurrsive function
# reuse function within same function 

num = int(input("Enter number to find factorial of \n"))
def recur_factorial(num):
    if(num<=1):
        return 1
    return num*recur_factorial(num-1)

print(f'factorial of {num} is {recur_factorial(num)}')





