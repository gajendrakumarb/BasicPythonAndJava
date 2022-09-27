# Topic : Set
# Set is unordered collection of non repetaive simple items
# - Sets are unordered and unindexed
# - Set in python are simmilar to sets in mathamatics 
#   and can be used to demonstrate set theory or venn diagram


rand_set1 = {1,3,5,7,8,'sdf','1',1.0}
print(rand_set1,type(rand_set1))

#rand_set1 = {1,3,[5,7],8,'sdf'} #we cant add indexed collection of objects into set like list

rand_set1 = {1,3,(5,7),8,'sdf'} 
print(rand_set1)

# emplty set can be decalared with funtion set()
print('Empty set')
rand_set1 = set()
print(rand_set1,type(rand_set1))

# adding object into set


rand_set1.add(1)
rand_set1.add(134)
rand_set1.add('sdk')
rand_set1.add(1) #cant add duplicate values into set
rand_set1.add(1)
print(rand_set1)

rand_set1.remove(1)
print(rand_set1)


rand_set1.add(23)
rand_set1.add(34)
rand_set1.add(99)

rand_set2 = {23, 11, 56, 99}

print(rand_set1)
print(rand_set2)

print("Checking set1 is superset of set2")
print(rand_set1.issuperset(rand_set2))

print("Checking set1 is subset of set2")
print(rand_set1.issuperset(rand_set2))

print("Intersection of set1 and set2")
print(rand_set1.intersection(rand_set2))

print("Union of set1 and set2")
print(rand_set1.union(rand_set2))

rand_set3 = set(['a','b','c'])
print(rand_set3)


# rand_set3 = set('a','b','c')  # gives error as set take one argument as list or single item
# print(rand_set3)