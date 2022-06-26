"""

"""
user_grade = int(input('What\'s your grade percentage? '))
"""
if user_grade >= 90:
  print('Your letter grade is A')
elif user_grade >= 80:
  print('Your letter grade is B')
elif user_grade >= 70:
  print('Your letter grade is C')
elif user_grade >= 60:
  print('Your letter grade is D')
else:
  print('Your letter grade is F')
"""

if user_grade >= 90:
  letter = 'A'
elif user_grade >= 80:
  letter = 'B'
elif user_grade >= 70:
  letter = 'C'
elif user_grade >= 60:
  letter = 'D'
else:
  letter = 'F'

#Stretch1
sign = ''
last_number = user_grade % 10

if last_number >= 7:
  sign = '+'
elif last_number < 3:
  sign = '-'
else:
  sign = ''

#Stretch2 AND Stretch3
if user_grade >= 93 or letter == 'F':
  sign = ''

print(f'Your letter grade is: {letter}{sign}')

if user_grade >= 70:
  print('Congratulation! you passed the class!')
else:
  print('You didn\'t pass the course. Best luck next time.')
