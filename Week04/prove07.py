"""
Proyect: Wordle Game
"""
secret_word = 'samuel'
counter = 0

print('Welcome to the word quessing game!')
guess = input('What is your guess? ')
while guess.lower() != secret_word:
  counter += 1
  print('Your guess was not correct.')
  guess = input('What is your guess? ')

print(f'It took you {counter + 1} guesses.')

""" value = 20
while value < 20:
   value = value + 1
print(value) """