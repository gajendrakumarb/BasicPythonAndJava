# find like following for n 
# n =3
#     *
#    ***
#   *****
n = int(input("enter value of n\n"))
i = n-1  # if i = n  i will be refrence to n can chage value of n
j = 1
while i >= 0:
    print(' '*i, end='')
    print('*'*j, end='')
    print(' '*i, end='')
    print()
    i -= 1
    j = n+n-1 - (i*2)


# find like following for n 
# n =3
#     *
#    **
#   ***
n = int(input("enter value of n\n"))
i = n-1  # if i = n  i will be refrence to n can chage value of n
j = 1
while i >= 0:
    print(' '*i, end='')
    print('*'*j, end='')
    #print(' '*i, end='')
    print()
    i -= 1
    j += 1
