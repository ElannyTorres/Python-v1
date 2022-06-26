"""
File: check05.py
Author: Luz Gavancho

Purpose: Practicing if statements
"""
# comparing numbers
firstNum = int(input('What i the first number? '))
secondNum = int(input('What i the second number? '))

if firstNum > secondNum:
  print('The first number is greater')
  print('The numbers are not equal')
  print('The second number is not greater')
elif firstNum < secondNum:
  print('The first number is not greater')
  print('The numbers are not equal')
  print('The second number is greater')
else:
  print('The first number is not greater')
  print('The numbers are equal')
  print('The second number is not greater')

#comparing strings
favAnimal = input('\nWhat is your favorite animal? ')

if favAnimal.lower() == 'cat':
  print('That\'s my favorite animal too!')
else:
  print('That\'s not my favorite.')