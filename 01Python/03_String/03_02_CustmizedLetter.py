'''WAP to create customized letter head 
addrssed to names and dates entered by user'''

name_entered = input('Please enter name to sent a letter : ')
date_entered = input('Please enter date : ')

letter = '''Dear <|NAME|>
            You are Selected!
<|DATE|>'''

letter = letter.replace('<|NAME|>',name_entered)
letter = letter.replace('<|DATE|>',date_entered)

print(letter)