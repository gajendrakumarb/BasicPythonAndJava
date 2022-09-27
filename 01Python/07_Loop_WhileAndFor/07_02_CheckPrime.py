# wap check entered number is prime numbers or not
from math import sqrt


num = int(input('Enter number to check prime or not : \n'))
prime = False
for r in range(2, int(sqrt(num))+1):
    
    if(num%r==0):
        prime = False
        break
    else:
        prime= True
    
if(prime):
    print('Yes, prime number !! ')
else:
    print('Not a Prime number')
    
        

   

