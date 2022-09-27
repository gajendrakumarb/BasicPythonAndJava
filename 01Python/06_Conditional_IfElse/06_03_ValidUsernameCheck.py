record_username = input('please enter your user name : ')

if(len(record_username)<10 or ' 'in record_username):
    print('your username is less than 10 char or has white space(s)')
else:
    print('Hi '+record_username)
    print('Thank you')