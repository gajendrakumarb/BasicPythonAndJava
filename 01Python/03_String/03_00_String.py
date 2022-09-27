# Topic : String

from cgi import print_arguments


str1 = 'Fassos'
# single quotes can not be used with string containing single quotes eg. opostopy kumar's etc
str2 = "Fasso's"
# Double quotes can not be used with string containing double quotes eg. Hanuman said "Jai Siya Ram"
# All above issue can be dealt with esquape sequance \ but it is hard to read to layman or to new eyes 
# triple quotes also used for multiline string
str3 = '''Baba said to chatur's students "Do not run after Success. 
Run after Excellence and Success will follow "'''

print(str1)
print(str2)
print(str3)

# Topic : String Concatination
str1 = "Hello"
str2 = "How are you doing?"

print(str1+", "+str2)

# Topic : String slicing (sub string)
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])

print(str1[0:3]) # from index 0 to index (3-1)
print(str1[2:5]) # from index 2 to index (5-1)
print(str1[1:]) # will start from index 1 till end of string
print(str1[:3]) # will start the start of string till index (3-1)
print(str1[2:2]) # returns null as end indx need to greater than start index in <str>[start:end]
print(str1[5:0]) # returns null as end indx need to greater than start index in <str>[start:end]

#str        H   E   L   L   L   O
#index      0   1   2   3   4   5       from start, index starts with 0
#index      -6  -5  -4  -3  -2  -1      from last, index starts with -1 and backwards

print(str1[-6:-1])
#print(str1[-6:0])      We can not use negative and non-negative index together
print(str1[-6:])   # will start from index -6 till end of string
print(str1[:-2])    # will start the start of string till index (-2-1)
print(str1[-1:-6])  # returns empty string as end indx need to greater than start index in <str>[start:end]
print(type(str1[-1:-6]))  # returns empty string as end indx need to greater than start index in <str>[start:end]

print(str2)
print(str2[0:16:2]) # will return every 2nd string for index 0 to index (16-1)
print(str2[3:14:3]) # will return every 3nd string for index 3 to index (14-1)

# Topic: String functions
longstr = "This is very long string example. This example is used in demostration of string's function."
print(longstr)

# len(<string>) returns lengths of string which indudes white spaces as well
print(len(longstr))

#<string>.startwith("abc") returns boolen value where <string> start with 'abc' or not
print("Does string starts with 'This' "+str(longstr.startswith('This')))
print("Does string starts with 'Once' "+str(longstr.startswith('Once')))

#<string>.endswith("xyz") returns boolen value where <string> ends with 'xyz' or not
print("Does string ends with 'function.' "+str(longstr.endswith('function.')))
print("Does string ends with 'Done' "+str(longstr.endswith('Done')))

#<string>.count("ijk") returns number of occurances of 'ijk' within <string>
print("Number of occurance of sub-string 'example' in the given string "+str(longstr.count('example')))
print("Number of occurance of sub-string 'is' in the given string "+str(longstr.count('is')))


#<string>.capitalized() returns string with captailzed first char of the string
stdname= 'bucky'
print(stdname)
print(stdname.capitalize())

#<string>.find("abc") returns index of first occurance of 'abc' within <string> else return -1
print(longstr.find('example'))

#<string>.replace("abc","xyz") returns string with of replacing all occurances of 'abc' in <string> with 'xyz'
print(longstr.replace('example','instances'))

#escape sequances \n, \t, \', \\  etc



 



