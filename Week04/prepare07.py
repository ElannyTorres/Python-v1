# Positive answer
num = int(input('Please type a positive number: '))
while num < 0:
  print('Sorry, that is a negative number. Please try again.')
  num = int(input('Please type a positive number: '))

print(f'The number is: {num}')

# child asking
answer = ''
while answer != 'yes':
  answer = input('May I have a piece of candy? ')
print('Thank you.')