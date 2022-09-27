# WAP to say hello to people whose name start with s other wise see them next day

people = ['Max', 'Jim','kim','Sam', 'Jam', 'Sisi','smiley']

for p in people:
    if p.startswith('s') or p.startswith('S'):
        print("Hi " + p +" !!")
    else:
        print("See you tommrrow, "+p)
        