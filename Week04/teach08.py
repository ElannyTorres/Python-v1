""" fav_letter = input('What\'s your favorite letter? ')
word = 'Commitment' """
""" for i in word:
  if i.lower() == fav_letter.lower():
    #print(i.capitalize(), end='')
    print('_', end='')
  else:
    print(i.lower(), end='') """

phrase = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'

keep_looping = 'yes'

while keep_looping == 'yes':
  num = int(input('Please enter a number: '))
  
  for i, letter in enumerate(phrase):
    rest = i % num
    if rest == 0:
      print(letter.upper(), end='')
    else:
      print(letter.lower(), end='')
  still = input('\nWould you like to enter another number (yes/no)? ')
  if still == 'yes':
    keep_looping = 'yes'
  else:
    keep_looping = 'no'

print('Goodbye')