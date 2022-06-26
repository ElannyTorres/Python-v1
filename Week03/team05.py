grade = float(input('What\'s your percentage? '))
letter = 'F'
sign = ''

reminder = grade % 10
if reminder >= 7:
    sign = '+'
elif reminder < 3:
    sign = '-'

if grade >= 90:
    if reminder >= 7:
        sign = ''
    letter ='A'
elif grade >= 80:
    letter ='B'
elif grade >= 70:
    letter ='C'
elif grade >= 60:
    letter ='D'
else:
    sign = ''

print(f'Your letter grade is {letter}{sign}')
if grade >= 70:
    print('Congrats! You pass the course')
else:
    print('Try harder next time! :) ')