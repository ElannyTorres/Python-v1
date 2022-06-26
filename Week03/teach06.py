"""
Amusement Park Rides
"""
from re import T


print('Welcome to The Amusement Park!')
print('If you want to ride, please answer the next questions:')

# Information
first_rider_age = int(input('What is the age of the first rider? '))
first_rider_height = int(input('What is the height of the first rider? '))

# Can ride
can_ride = False

if first_rider_age >= 12 and first_rider_age < 18:
  golden_pass1 = input('Does this rider haven a golden passport? (yes/no) ')

second_rider = input('Is there a second rider (yes/no)? ')

if second_rider.lower() == 'yes':
  second_rider_age = int(input('What is the age of the second rider? '))
  second_rider_height = int(input('What is the height of the second rider? '))
  if second_rider_age >= 12 and second_rider_age < 18:
    golden_pass2 = input('Does this rider have a golden passport? (yes/no) ')
  if first_rider_height < 36 or second_rider_height < 36:
    can_ride = False
  else:
    if first_rider_age >= 18 or second_rider_age >= 18 or golden_pass1.lower() == 'yes' or golden_pass2.lower() == 'yes':
      can_ride = True
    else:
      if first_rider_age >= 12 and second_rider_age >= 12 and first_rider_height >= 52 and second_rider_height>= 12:
        can_ride = True
      elif (first_rider_age >= 16 and second_rider_age >= 14) or (first_rider_age >= 14 and second_rider_age >= 160):
        can_ride = True
      else:
        can_ride = False
else:
  if (first_rider_age >= 18 or golden_pass1.lower() == 'yes') and first_rider_height >= 62:
    can_ride = True
  else:
    can_ride = False

# Answers
if can_ride:
  print('Welcome to the ride. Please be safe and have fun!')
else:
  print('Sorry, you may not ride.')
