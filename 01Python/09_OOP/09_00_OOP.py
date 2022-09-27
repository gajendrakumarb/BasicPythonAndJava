#Creating Class and creat object from that class
'''
class Person:
    pass

p = Person();  #p is an object/ an instance of Person class 
print(p)

'''

#Creating methods in the class which objects can use
# Class methods have one little differnce from regular methods is 
#   that they have one argument that is object itself as 'self'.
# 'self' is similar to this in c++, java, c# etc.

'''
class Person:
#    def greet():               # throws error as greet() takes 0 positional arguments but 1 was give
    def greet(self):
        print('Hello There..!!')
    def greetTo(self,name):
        print(f'Hello, How are you doing?, {name}')

p = Person()
print(p)
p.greet()   # greet(p)
p.greetTo('Ram')

'''

# __init__ function fo the class is similar to constructors in java/c# etc.
# They get called automatical at time of creating/initilisation of the new object
'''
class Person:
    def __init__(self, name):
        self.name = name
        print(f'You have created object of person named {self.name}')
    def greetTo(self,name):
        print(f'Hello, How are you doing?, {name}. My name is {self.name}')


#p = Person()    
# this gives error as we modified default __init__ and now it require one more argumet to initilize
#print(p)
#p.greet()   # greet(p)
#p.greetTo('Ram')

p = Person('Sam')
p.greetTo('Ram')  # Person('Sam').greetTo('Ram') 

'''


# class varibles and object varibles 

class CricketPlayer:
    no_of_players = 0  # A class variable, counting the number of employees
    def __init__(self, name): #object variables 
        self.name = name    #initailized object varible and assinged value at time of inilization
        self.role = None    #initailized object varible with null value
        print("(Added employee named {})".format(self.name))
        CricketPlayer.no_of_players += 1 # When employee created, it increases number of employees
    
    def injured(self):
        print(f'{self.name} has injured and stop playing the sport')
        CricketPlayer.no_of_players -= 1
        if(CricketPlayer.no_of_players == 0): print(f'{self.name} was last player to play the game')
        else: print(f'We still have {CricketPlayer.no_of_players} players left.')
    
    def playerrole(self, role):
        self.role = role
        print(f'{self.name} has {self.role} skills.')

    def getDetails(self):
        print(f'{self.name} is a {self.role}')

    @classmethod
    def getNoOfPlayers(cls):
        print(f'You have {CricketPlayer.getNoOfPlayers} players')


p1 = CricketPlayer('p1')
p2 = CricketPlayer('p12')
p3 = CricketPlayer('p99')
p4 = CricketPlayer('p21')

p3.playerrole('bowling')
p1.playerrole('bowling')
p1.playerrole('batting')
    
p1.getDetails()
p2.getDetails()
p3.getDetails()
p4.getDetails()