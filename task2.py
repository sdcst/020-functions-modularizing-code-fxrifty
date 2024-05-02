"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
def title():
 print('Hello! In This Game You Have 1 Chance To Guess A Number Between 1 And 10. Good Luck!')
x=input("Enter Your Guess Here")



title()
name = input('Enter a Username ')
print('Welcome',name)
numbers=('1','2','3','4''5','6','7','8''9','10')
answer=random.choice(numbers)
x=input("Enter Your Guess Here\n")
if x == answer:
 print("Congradulations {name}! {x} Was The Answer")
else:
 print("Nice Try") 

 