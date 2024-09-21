#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
"""

@author: JadaMoody  

"""

""" 
This project has two parts: The "main" code that plays
the game, and completing the functions that determine if 
the player won the game.  Note that for all code, the 
number 37 represents a roll of 00.
"""

"""
Part 1: Winning functions

Complete each function, which should return True if the player wins
the bet, and False if they lose.  The bet_value is the number that the 
player bets on and the roll is the number where the marble landed.
The number 37 refers to a roll of 00.

Running the tester.py code will run these functions and check the answers,
reporting any incorrect answers it finds.

Note: If your code is very complex or long for any of these functions,
try using your problem solving techniques to find a more elegant (mathy)
solution.  
"""



#Function for a straight bet, bet_value must equal roll to win 
def win_straight(bet_value, roll):
    if bet_value == roll:
        return True
    else:
        return False   


# Function for an even/odd bet, a bet_value of 0 is even and 
# a bet_value of 1 is odd
# Roll can't equal 0 or 37 (37 is 00) 
def win_even_odd(bet_value,roll):
    if roll == 0:
        return False
    if roll == 37:
        return False
    if bet_value == 0 and roll % 2 == 0:
        return True
    elif bet_value == 1 and roll % 2 == 1:
        return True
    else:
        return False

    

# Function for a dozen bet, bet_value is 1, 2, or 3, 1 representing 
# first dozen, 2 representing second dozen, and 3 representing third dozen 
# Roll can't equal 0 or 37 (37 is 00 )
def win_dozen(bet_value, roll):
    if roll == 0:
        return False
    if roll == 37:
        return False
    if bet_value == 1 and (roll >= 1 and roll <= 12):
        return True
    elif bet_value == 2 and (roll > 12 and roll <= 24):
        return True
    elif bet_value == 3 and (roll >24 and roll <=36):
        return True
    else:
        return False


# Function for a column bet, bet_value is 1, 2, or 3, 1 representing
# first column, 2 representing second column, and 3 representing third column
def win_column(bet_value, roll):
    if roll == 0:
        return False
    if roll == 37:
        return False
    if bet_value == 1 and roll % 3 == 1:
        return True
    elif bet_value == 2 and roll % 3 == 2:
        return True
    elif bet_value == 3 and roll % 3 == 0:
        return True
    else:
        return False
        
        

""" 
Project Part 2: Play the game.

Leave the code provided, then complete the game using the 
directions in the comments.

There is no autograder for this part.  You should play the game to test it.
"""
# Ask the user how much money they want to bet, what type of bet,
# and the bet value
if __name__ == "__main__":
    money = int(input('Enter the amount of money you want to bet: '))

    bet_choice = int(input('Choose your type of bet:\n'+
                       '1: Straight bet\n'+
                       '2: Even/odd bet\n'+
                       '3: Dozen bet\n'+
                       '4: Column bet\n'))

    bet_value = int(input('If you chose option 1, enter number to bet on, and use 37 for double-zero \n'+
                       'If you chose option 2, enter 0 for even or 1 for odd \n'+
                       'If you chose option 3, enter 1 for first dozen, 2 for second, or 3 for third \n'+
                       'If you chose option 4, enter column number: 1, 2, or 3 \n'))


    
    
    # Finds a randomn number between 0 and 37, printing what number was rolled
    roll = random.randint(0,37)
    print('Roll: ', roll)
    
    

   # These if-statements calls and prints whether or not the player won 
   # and how much they won or lost  based on which bet they chose.
    if bet_choice == 1 and win_straight(bet_value, roll) == True:
        print('Won: $', money * 36)
    if bet_choice == 1 and win_straight(bet_value, roll) == False:
        print('Lost: $',money)
    
    
    if bet_choice == 2 and win_even_odd(bet_value, roll) == True:
        print('Won: $',money * 2)
    if bet_choice == 2 and win_even_odd(bet_value, roll) == False:
        print('Lost: $', money)
        
        
    if bet_choice == 3 and win_dozen(bet_value, roll) == True:
        print('Won: $', money * 3)
    if bet_choice == 3 and win_dozen(bet_value, roll) == False:
        print('Lost: $',money)
        
        
    if bet_choice == 4 and win_column(bet_value, roll) == True:
        print('Won: $', money * 3)
    if bet_choice == 4 and win_column(bet_value, roll) == False:
        print('Lost: $', money)
        
    
    
    
    
    

