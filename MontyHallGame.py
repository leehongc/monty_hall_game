#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import random

def custom_input(question):
    user_response = input(question).strip().lower()
    return user_response
    
def monty_game():
    doors = [1,2,3]
    prize = random.choice(doors)
    ask_for_door = 'There are three doors. Behind one of the doors there is a vintage Porche. \nWhile the other two doors contains black holes in which you will be sucked in immediately.  \nWhich door do you chose?'
    userpick = int(custom_input(ask_for_door))
    
    while userpick not in doors:
        userpick = int(custom_input('Your input is out of range.  Try again...'))
    print('You chose door number {}'.format(userpick))
    reveal = [i for i in doors if i not in (prize, userpick)][0]
    print('There is a blackhole behind door number {}'.format(reveal))
    
    notrevealed = [i for i in doors if i not in (reveal, userpick)][0]
    change_options = ['yes', 'no']
    switch_door = 'Would you like to switch to door number {}?  Yes or No'.format(notrevealed)
    change = custom_input(switch_door)
    
    while change not in change_options:
        change = (custom_input('Incorrect input. Try again...[yes/no]'))
                
    if change == 'no':
        if userpick == prize:
            print('Congratulations, you won the Porsche!')
        else:
            print('Black hole, better luck next time!')
    else:
        print('You\'ve switched to door number {}'.format(notrevealed))
        if notrevealed == prize:
            print('Congratulations, you won the Porsche!')
        else:
            print('Black hole, better luck next time!')
            
def quick_game(switch_choice, number_of_games):
    doors = [1,2,3]
    games_played = 0
    total_wins = 0
    for i in range (int(number_of_games)):
        prize = random.choice(doors)
        userpick = random.choice(doors)
        reveal = [i for i in doors if i not in (prize, userpick)][0]
        notrevealed = [i for i in doors if i not in (reveal, userpick)][0]
        change = switch_choice.lower()
        if change == 'no':
            if userpick == prize:
                total_wins += 1
                games_played += 1
            else:
                games_played += 1
        else:
            if notrevealed == prize:
                total_wins += 1
                games_played += 1
            else:
                games_played += 1
            
    print('Out of {} games, you have won {} times.'. format(games_played, total_wins))

    
def main(argv):
    if len(argv) > 0:
        rawchange = int(argv[0])
        if rawchange == 0:
            change = 'no'
        else:
            change = 'yes'
        number_of_games = int(argv[1])
        quick_game(change, number_of_games)
    else:
        monty_game()
    
    
if __name__ == "__main__":
    main(sys.argv[1:])

