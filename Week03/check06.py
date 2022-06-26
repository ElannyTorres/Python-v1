"""
Qualifying for a loan
"""
print('Please provide from 1 to 10 rating each of the following questions:')
#info variables
loan_size = int(input('How large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

#should have the loan
loan = False

if loan_size >= 5:
  if credit >= 7 and income >= 7:
    loan = True
  elif credit >= 7 or income >= 7:
    if down_payment >= 5:
      loan = True
    else:
      loan = False
  else:
    loan = False
else:
  if credit < 4:
    loan = False
  else:
    if income >= 7 or down_payment >= 7:
      loan = True
    elif income >= 4 and down_payment >= 4:
      loan = True
    else:
      loan = False

#Answer
if loan:
  print('The decision is YES. Congratulations!')
else:
  print('The decision is NO. Maybe a loan is not the best option.')