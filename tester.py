#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:26:03 2021

@author: Shannon Duvall

    bet_choice = int(input('Choose your type of bet:\n'+
                       '1: Straight bet\n'+
                       '2: Even/odd bet\n'+
                       '3: Dozen bet\n'+
                       '4: Column bet\n'))

    bet_value = int(input('Enter number to bet on, and use 37 for double-zero \n'+
                       'Enter 0 for even or 1 for odd \n'+
                       'Enter 1 for first dozen, 2 for second, or 3 for third \n'+
                       'Enter column number: 1, 2, or 3 \n'))
"""
import roulette

def general_tester(tests, function, row_change, function_str):
    for b in range(len(tests)):
        for d in range(len(tests[0])):
            bet = b + row_change
            your_answer = function(bet, d)
            correct = tests[b][d]
            if (your_answer == None):
                reply = function_str+"("+str(bet)+","+str(d)+")"+ \
                " incorrectly returned None"
                return reply
            elif(your_answer!= correct):
                reply = function_str+"("+str(bet)+","+str(d)+")"+ \
                " incorrectly returned "+str(your_answer)
                return reply
    return function_str+": ALL TESTS PASSED"

def test_straight():
    tests = [[b==d for b in range(38)]for d in range(38)]
    return general_tester(tests, roulette.win_straight, 0, "win_straight")

def test_eo():
   row0 = [True,False]*19
   row0[0] = False
   row1 = [False,True]*19
   row1[37] = False
   tests = [row0, row1]
   return general_tester(tests, roulette.win_even_odd,0,"win_even_odd")

def test_dozen():
   tests = [[False]+[True]*12 + [False]*24 + [False],
            [False]+[False]*12 + [True]*12 + [False]*13,
            [False]*25 + [True]*12 + [False]]
   return general_tester(tests, roulette.win_dozen,1, "win_dozen")

def test_col():
   tests = [[False]+[True,False,False]*12+ [False],
            [False]+[False,True,False]*12+ [False],
            [False]+[False,False,True]*12+ [False]]
   return general_tester(tests, roulette.win_column,1, "win_column")

if __name__ == "__main__":
    print(test_straight())
    print(test_eo())
    print(test_dozen())
    print(test_col())    
   
    