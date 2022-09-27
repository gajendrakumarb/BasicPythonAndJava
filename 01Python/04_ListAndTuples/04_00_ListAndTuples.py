# Data Structures (Ways of collecting data)
# - Python has four built-in data types - List, tuples, Dictonry and Set
# - These data structure allows data to be stored and accessed 
#   in effiencent manner with the help of build-in methods

#'''

# Topic : Lists
# - List is mutable data structure that holds an ordered collection of items
# - List stores its items in sequace with in []



a = [45,67, 34, 30, 23,234]

# Printing List using print()
print(a) 

# Accessing list items usint indexs like a[0] a[2] etc
print(a[4])

# Lists are mutable so we can change values of it's item
a[2] = 28
print(a)

# List can hold items of different types as well
b = [23, 'Sijuku', 3.5, True]
print(b)

b[1] = 34
print(b)

# Topic : List slicing i.e. creating sub-list using indexs
numlist = [12, 2, 9, 56, 321, 2, 23]
cars = ["Ford", "Maruti", "TATA", "Honda", 8, "Delta"]

print("Printing slice of the list using list[startindex : endindex]")
print(cars[2:4])
print(cars[-4:])

print("Printing length of the list using len() method")
print(len(numlist))
print(len(cars))

#deleting item from list using index
print("Deleting item form list using del list[<index>/<slice_of_index>]")
del cars[2]
print(cars)

#del cars['Delta']      this will create error as [] indexs should be int or slice
del cars[3:]
print(cars)


# Topic : List methods
# - List has various build-in methods to access and modify the data/items in the list.
  
numlist = [12, 2, 9, 56, 321, 2, 23]
cars = ["Ford", "Maruti", "TATA", "Honda", 8, "Delta"]
print(numlist)
print(cars)
print("Printing list using for loop \n numlist : ")
for item in numlist:
    print(item, end=', ')
print("\n cars : ")
for item in cars:
    print(item, end=', ')
print()

# <list>.sort() sorts the list itself
print("Sorting list using <list>.sort() method")
print("Sort() method sorts in Ascending order maintaing order of repeted items")
numlist.sort() #"Sort() method sorts in Ascending order maintaing order of repeted items"
print("Sort(reverse=True) with reverse flag sorts in decending order")
numlist.sort(reverse=True)  #Sort(reverse=True) with reverse flag sorts in decending order
#cars.sort()  
# - List can not be sorted if it contains multiple data types 
# - list.sort() method only works with items with consistant data type in the list
print(numlist)
#print(cars)

# <list>.reverse() reverses the list itself
print("Reversing list using <list>.reverse() method")
numlist.reverse()
cars.reverse()
print(numlist)
print(cars)


# <list>.append(<item>) adds item at the end of list itself
print("Adding new item at the end of list using <list>.append() method")
numlist.append(53)
cars.append(False)
print(numlist)
print(cars)



# <list>.insert(<index>,<item>) adds <item> at <index> in the list itself other element automaticaly get shited to next indexs
print("Inserting new item at index of list using <list>.insert() method")
numlist.insert(2, 49)
cars.insert( 12, 'ford') # As cars length is 6 but this line add the element at the end of the list cars
cars.insert(0,False)   # inserting at index 0 
cars.insert(-1,True)   # inserting after index -1 i.e. adding element after second index from last/ end of list
cars.insert(-2,"BMW")   # inserting after index -2 i.e. adding element after second index from last/ end of list
print(numlist)
print(cars)

# <list>.pop(<index>) deletes item at the <index> of list
print("Removing item at <index> of list using <list>.pop() method")
numlist.pop(2)
cars.pop(4)
print(numlist)
print(cars)

# <list>.remove(<item>) deletes first occrance of item, if exsists and repeated, from the list
print("Removing first occrance of item, if exsists and repeated, from list using <list>.remove() method")
numlist.remove(2)
cars.remove(False)
print(numlist)
print(cars)

# '''

# Topic : Tuples
#   Tuple are used to store mupltible items or objects.
#   Unlike List, tuples are immutable like string. 
#   Python does not allow to modify the tuple once items stored alongsinde delcaratin of tuple. 

# Creating a tuple using ()
tuple1 = (1, 2, 4, 5)

tuple_empty = () # Empty tuple
tuple_singleitem = (1) # Wrong way to declare a Tuple with Single element
print(str(tuple_empty)+' : '+str(type(tuple_empty)))
print(str(tuple1)+' : '+str(type(tuple1)))
print(str(tuple_singleitem)+' : '+str(type(tuple_singleitem)))
tuple_singleitem = (1,) # Tuple with Single element
print(tuple_singleitem)
print(str(tuple_singleitem)+' : '+str(type(tuple_singleitem)))


# tuple can hold diffent items even sub tuple

rand_tuple = (2,'Messi', True, ('Red','Blue',4.5))
print(rand_tuple)

print(rand_tuple[1])
print(rand_tuple[2])
print(rand_tuple[3])
print(rand_tuple[3][2],type(rand_tuple[3][2]))
print(rand_tuple[3][1:], type(rand_tuple[3][1:]))
# Printing the elements of a tuple
print(tuple1[0])

# Cannot update the values of a tuple
# tuple1[0] = 34 # throws an error

# Tuple has count and index function
tuple2 = (14, 2, 1, 47, 35, 47, 1, 2,1 ,1)
print(tuple2)
print('tuple.count(<item>) will return number occurances of item in given tuple')
print(tuple2.count(1))

print('tuple.index(<item>) will return index of first occrance of the item from given tuple')
print(tuple2.index(2))