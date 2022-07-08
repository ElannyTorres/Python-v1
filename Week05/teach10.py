bank_accounts = []
balances = []
account = None
total = 0.0
average = 0

print('Enter the names and balances of bank accounts (type: quit when done)')


while account != 'quit':
  account = input('What\'s the name of this account? ')

  if account != 'quit':
    balance = float(input('What is tha balance? '))
    bank_accounts.append(account)
    balances.append(balance)


print('\nAccount Information:')
for i in range(len(bank_accounts)):
  print(f'{i}. {bank_accounts[i].capitalize()} - ${balances[i]:.2f}')

  total += balances[i]

average = total / len(balances)
print(f'\nTotal: ${total:.2f}')
print(f'Average: ${average:.2f}')

highest_acount = None
#It must be -1 because we don't know the length could have and 0 is the first item
highest_balance = -1

for i in range((len(bank_accounts))):
  account = bank_accounts[i]
  balance = balances[i]

  if balance > highest_balance:
    highest_balance = balance
    highest_acount = account

print(f'Highest balance: {highest_acount} - ${highest_balance:.2f}')

update = 'yes'
while update != 'no':
  update = input('\nDo you want to update an account (yes/no)? ')

  if update.lower() == 'yes':
    up_index = int(input('What account index do you want to update? '))
    up_amount = float(input('What is the new amount? '))

    balances[up_index] = up_amount
  
  print('\nAccount Information:')
  for i in range(len(bank_accounts)):
    print(f'{i}. {bank_accounts[i].capitalize()} - ${balances[i]:.2f}')