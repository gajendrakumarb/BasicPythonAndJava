# following program to check comment entered has recoreded spam or offencsive words
# this programme can be effecieny wite with the help set as well
record_comment = input("Whrite your comments about life: \n")

spam_wlist = ["play and win","make a free money","subscribe this","subscribe my","click this","click here" ]
offensive_wlist = ["fuck","f**k"] 

commentflag = True
for wrd in offensive_wlist:
    if(wrd  in record_comment):
        print('recored comment is offensive')
        commentflag=False

for wrd in spam_wlist:
    if(wrd  in record_comment):
        print('recored comment is spam')
        commentflag=False

if(commentflag is True):
    print('Thank you for your comment')
else:
    print('Have a nice day')



