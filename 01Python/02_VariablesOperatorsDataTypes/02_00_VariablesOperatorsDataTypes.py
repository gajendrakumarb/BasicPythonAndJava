# Topic : literals
#   literals are constant values.
#   example - 12 , -7, 76.3, "theGround" etc


# Topic : Variables
#   variable are used to store literals
#   variable name can start with alphabes or underscore
#   variable name can contain alphables, numbers and underscore
#   variable name can not start with digit 
#   variable can not have white spaces
#   In python, variable does not requred pre data type defination.
#       It will assingn data types automatically when we assign variable with literal values.


a = '''theString'''
b = 12
c = 11.23
d = False
e = None

print(a)
print(b)
print(c)
print(d)
print(e)

_num1 = 23

print(_num1)

# Topic : type(<variable or literal>)
#   type function returns datatypes of variable or literal passed as argument

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(_num1))
print(type('''This is string'''))
print(type(print()))
print(type(print(2)))

# Topic : String are immutable i.e. ones declared can not be changed.

a = 'new string'
print(a)

# a[0] = 'd'
# print(a)


# Topic : operators
#   Arathmetic operators    +, -, *, ** (power) , /, // (divid and floor), %  etc.
#   bitwise operator        <<, >>, &, | , ^ (bit-wise XOR), ~ (bit-wise invert)
#   assingment operators    =, +=, -=, *=, /= etc.
#   Comparision operators   ==, >=, <=, >, <, != etc.
num1 = 28
num2 = 34
num3 = 99
num4 = 99

print('Check num3 {0} equal to num4 {1} :'.format(num3,num4) , num3==num4)
print('Check num1 {} equal to num4 {} :'.format(num1,num4) , num1==num4)
print(f'Check num1 {num1} is greater than or equal to num2  {num2} :', num1>=num2)
print(f'Check num1 {num1} is less than num2 {num2} :', num1 < num2)
# Topic : <string>.format() function 
#   f<string> or <string>.format(variables) function takes variable name and replae arguments {} within string 
#   regarless of their datatype as it convert and return as string

#   decimal precision of 3 for float 0.333
print('{0:.3f}'.format(1.0/3))
#   fill text with _ with text centered
print('{0:_^11}'.format('hello'))

# Topic : print() function
#   Print function automatically end with new line i.e. \n
#   to override, we can specifiy 'end' attribute

print('following line should be printed next to this one.', end=' ')
print('Did this line contined with the above statment?')


# Topic : Logical operators       and, or, not
bool1 = True
bool2 = False

print('bool1 and bool2 results :', bool1 and bool2)
print('bool1 or bool2 results :', bool1 or bool2)
print('not bool2 results :', not bool2)


# Topic : data type conversiton

strToInt = int("23")
intToStr = str(123)
intToFloat = float(12)

print(strToInt, type(strToInt))
print(intToStr, type(intToStr))
print(intToFloat, type(intToFloat))

# Topic : Read from keybard (user) using input() function
#   input() funtion read string entered via keybead till enter key pressed
#   input() return catched string as string datatype

a = input("Enter your Name :")
print(a, type(a))








