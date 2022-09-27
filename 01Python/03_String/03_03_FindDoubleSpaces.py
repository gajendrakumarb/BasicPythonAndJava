#WAP to find double spaces in the string
# replace with single spaces
longstr = "He went after the cat.  She ignored her as usual. He winned her back with her  favrate treats."
print(longstr)

print(longstr.find('  '))

longstr = longstr.replace('  ', ' ')

print(longstr)