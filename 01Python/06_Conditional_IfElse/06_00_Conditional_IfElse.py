# Topic : Conditional Operations
# In python, if - elif - else blocks used to evaluate condition and excute code block
# sytanx similar to c, c++ , java or any other langugare if- else if - else block 
# elif is short for  else if


# from datetime import date

# # If today is Monday (aka 0 of 6), then run the report
# if date.today().weekday() == 0:
#     run_report()


from datetime import date
#today = date.today().weekday
today = date.today().weekday()
print(date.today())
print(today)
if(today == 0):
    print('today is monday')
elif(today == 1):
    print('today is tuesday')
elif(today == 2):
    print('today is wednsday')
elif(today == 3):
    print('today is thursday')
elif(today == 4):
    print('today is friday')
elif(today == 5):
    print('today is satday')
else:
    print('today is sunday')


a=12

if (a>2):
    print(f'{a} is greater than 2')
elif (a>10):
    print(f'{a} is greater than 10')
elif (a<20):
    print(f'{a} is less than 20')
#print('this is print statement between if and else block which not programming lang allow')
else:
    print('This is else statment which is optional')

# is and in

a = 12
b = [23, 14, 12, 17]
if(a is 12):
    print('this a is 12')
if( a%2==0 and a%4==0):
    print('''a is even and has 4 as one of factor or come in 4's table''')
if( a in b):
    print('a present in b list')
