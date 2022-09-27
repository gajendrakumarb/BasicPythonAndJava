import random

def rockpaperscissors(usr_choice):
    game=['r','p','s']
    comp_choice = random.choice(game)
    if(usr_choice==comp_choice):
        return 0
    elif((usr_choice=='r'and comp_choice=='s') or (usr_choice=='s'and comp_choice=='p') or (usr_choice=='p'and comp_choice=='r')):
        return 1
    else:
        return -1


print('Welcome fellow stranger..!!')
print('Play Rock-Paper-Scissors with Computer..')
r = int(input('Enter number of rounds you want to play : '))
if(r>0):
    no_of_wins = 0
    no_of_draws = 0
    pr= 1
    while(r>0):
        usr_choice = input(f'Round {pr} : type \n r for rock \n p for paper \n s for Scissors \n e for exit \n').lower()
        if( usr_choice in ['r', 'p', 's']):
            usr_result= rockpaperscissors(usr_choice)
            if(usr_result==1):
                no_of_wins += 1
                print(f'You won round {pr}')
            elif(usr_result==0):
                no_of_draws += 1
                print(f'You draw round {pr}')
            else:
                print(f'You lost round {pr}')
            r -= 1
            pr += 1
        elif(usr_choice == 'e'):
            print(f'you exited the game after {pr-1} round')
            break
        else:
            print('Invalid Input')
    if(no_of_wins > pr - 1 - no_of_wins -no_of_draws):
        print(f'You won the game with {no_of_wins} rounds out if {pr-1} with {no_of_draws} draws')
    elif(no_of_wins == pr - 1 - no_of_wins -no_of_draws):
        print(f'Game draw. Computer and you win {no_of_wins} rounds each out of {pr-1} with {no_of_draws} draws')
    else:
        print(f'You lost the game with {pr - 1 - no_of_wins -no_of_draws} losses out of {pr-1} rounds with {no_of_draws} draws')
else:
    print('Invalid Input')


