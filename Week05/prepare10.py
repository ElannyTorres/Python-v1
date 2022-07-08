print('Please enter the items of the shopping list (type: quit to finish):')

prod_name = ''
keep_looping = True
cart = []

while keep_looping:
  prod_name = input('Item: ')

  if prod_name == 'quit':
    keep_looping = False
  else:
    cart.append(prod_name)

print('\nThe shopping list is:')
for i in range(len(cart)):
  item = cart[i]
  print(f'{i}. {item.capitalize()}')

index = int(input('\nWhich item would you like to change? '))
new_item = input('What\'s the new item? ')

cart[index] = new_item

print('\nThe shopping list with indexes is:')
for i in range(len(cart)):
  item = cart[i]
  print(f'{i}. {item.capitalize()}')