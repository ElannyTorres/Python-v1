"""
Assigment: L08 Prove: Assignmet
Student: Luz Torres
"""

# letter colors
colors = {
  'green': '\033[92m',
  'yellow': '\033[93m',
  'red': '\033[91m',
  'ENDC': '\033[0m',
}
#function
def color(letter, color):
  return colors[color] + letter + colors['ENDC']

#init game
print('Welcome to the word guessing game!')
print(f'Some instructions:\n- The word you are guessing have 6 letter.\n- If the letter is not included in the word it will appear like this {color("_", "red")}.\n- If the letter is included in word but is not in the correct position it will appear like this {color("a".lower(),"yellow")}.\n- If the letter is included in the word and is in the correct position it will appear like this {color("a".upper(),"green")}.')
lives = 6
print(f'You have {lives} lives')

win = False
word = 'hidden'
board = []

for i in range(6):
  board.append(['_' for l in range(6)])
  print(' '.join(board[i]))

counter = 0
while (not win) and (counter < len(word)):
  text = input('\nWhat is your guess? ')
  while len(text) != len(word):
    print(f'The word must have {len(word)} letters.')
    text = input('\nWhat is your guess? ')

  # win logic
  if word == text:
    board[counter] = [color(l.upper(), 'green') for l in text]
    win = True

  # each letter in the word
  else:
    test_line = []
    for j in range(len(text)):
      if text[j] == word[j]:
        test_line.append(color(text[j].upper(), 'green'))
      elif text[j] in word:
        test_line.append(color(text[j].lower(), 'yellow'))
      else:
        test_line.append(color('_', 'red'))
    board[counter] = test_line

  for i in range(6):
    print(' '.join(board[i]))
  
  counter += 1
  if word != text:
    print(f'You have {lives - counter} lives.')

if win:
  print('Yeah! You did it!')
else:
  print('Best luck next time')