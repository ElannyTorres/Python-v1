"""
Author: Luz Gavancho Torres
"""
from pickle import APPEND


keep_running = True
cart = []
amount = []
item_name = ''
options = ('Please select one of the following: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit')

print('Welcome to the Shopping Cart Program!')
print()
print(options)

option_selected = int(input('Please enter an action: '))

while keep_running:
  if option_selected == 1:
    item_name = input('What item would you like to add? ')
    item_price = float(input(f'What is the price of "{item_name.capitalize()}"? '))
    cart.append(item_name)
    amount.append(item_price)
    print(f'"{item_name.capitalize()}" has been added to the cart.')
    print()
    print(options)
    option_selected = int(input('Please enter an action: '))
  elif option_selected == 2:
    if len(cart) == 0:
      print('There\'s nothing in the shopping cart. Choose option 1 to add an item.')
    else:
      print('\nThe contents of the shopping cart are:')
      for index, item in enumerate(cart, start=1):
        print(f'{index}. {item.capitalize()} - ${amount[index - 1]:.2f}')
    print()
    print(options)
    option_selected = int(input('Please enter an action: '))
  elif option_selected == 3:
    index_to_update = int(input('Which item would you like to remove? '))

    if index_to_update <= len(cart) and index_to_update > 0:
      print('Item removed')
      cart.pop(index_to_update - 1)
      amount.pop(index_to_update - 1)
    else:
      print('Sorry, that is not a valid item number')
    print()
    print(options)
    option_selected = int(input('Please enter an action: '))
  elif option_selected == 4:
    print(f'The totxal price of the items in the shopping is ${sum(amount):.2f}')
    print()
    print(options)
    option_selected = int(input('Please enter an action: '))
  elif option_selected == 5:
    keep_running = False
  else:
    print('\nOption not available.',)
    print(options)
    option_selected = int(input('Please enter an action: '))
print('\nThank you. Goodbye!')