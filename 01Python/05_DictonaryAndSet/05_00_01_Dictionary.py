# Topic : Dictionary
# Dictionary is collection of key value pair
# Dictionary is indexed, unordered and mutable object of clss dict
# keys in Dictionary must be unique and can only be immutable objects like string
# values can be mutable or immutibale objects

rand_dict = {'key':'value',
            "car":"Ford's",
            "marks":100,
            'list':[2,4,89],
            1:34,
            'emptykey':None,
            None:'Wow',
            True: 'next to wow',
            2:234}

#Accessing Dictionary using keys 
print(rand_dict['key'])
#print(rand_dict[0])  key not found as it is not ordered/indexed list or tuple
print(rand_dict[1])
print(rand_dict['list'])
print(rand_dict[True])
print(rand_dict['emptykey'])


email_dict = {'sam':'sam@gmail.com',
             'ram':'ram@yahoo.com',
             'buddy': None,
             'tim':'tim@gmail.com',
             'jim':'jim@gmail.com',
             'kim':'adfasf'}
print(email_dict)
# deleting key-value pair in dictionary using key
del email_dict['kim']
print('''after: del email_dict['kim'] ''')
print(email_dict)

# <dict>.items() returns list of key-value pairs
print(email_dict.items(),type(email_dict.items()))

# <dict>.keys() returns list of key
print(email_dict.keys(),type(email_dict.keys()))

# <dict>.valuses() returns list of key
print(email_dict.values(),type(email_dict.values()))

# accessing key-value pairs or items of dictionary one by one using loops
for name,n_email in email_dict.items():
    print(f'Contact {name} at {n_email}') 

# updating dictonary
#email_dict.update('buddy','buddy@ymail.com') gives error due wrong syntax of update method for dict
email_dict.update({'buddy':'buddy@ymail.com'})
email_dict.update({'tom':'tom@tom.com'})  #addes new item
print(email_dict)
