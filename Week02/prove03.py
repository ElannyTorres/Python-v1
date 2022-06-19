print('Welcome to the meal Calculator!')
print('Please introduce the following information:')
# Variables
children = input('\nAre you ordering for children (yes/no)? ')
if children == 'yes':
    childNum = int(input('How many children\'s are? '))
    childMeal = float(input('What is the price of a child\'s meal? '))
    childDrink = float(input('What is the price of a child\'s drink? '))
    childTotalAmount = childNum * (childMeal + childDrink)

adults = input('\nAre you ordering for adults (yes/no)? ')
if adults == 'yes':
    adultNum = int(input('How many adults are? '))
    adultMeal = float(input('What is the price of an adult\'s meal? '))
    adultDrink = float(input('What is the price of an adult\'s drink? '))
    adultTotalAmount = adultNum * (adultMeal + adultDrink)

if (children == 'yes') and (adults == 'yes'):
    subtotal =  childTotalAmount + adultTotalAmount

if (children == 'yes') and (adults == 'no'):
    subtotal =  childTotalAmount

if (children == 'no') and (adults == 'yes'):
    subtotal =  adultTotalAmount

taxRate = float(input('\nWhat is the sales tax rate? '))
salesTax = subtotal * (taxRate / 100)

tip = input('\nAre you paying tip (yes/no)? ')
if tip == 'yes':
    tipPercentage = float(input('What is the tip percentage? '))
    tipAmount = subtotal * (tipPercentage / 100)
    total = subtotal + salesTax + tipAmount

if tip == 'no':
        total = subtotal + salesTax

print('\n===============================')
print('Order details:')
if children == 'yes':
    print (f'{childNum} children meals.') if childMeal > 0 else print('No children\'s meals.')
    print (f'{childNum} children drinks.') if childDrink > 0 else print('No children\'s drinks.')
if children == 'no':
    print('*No order for children*')
if adults == 'yes':
    print (f'{adultNum} adults meals.') if adultMeal > 0 else print('No children\'s meals.')
    print (f'{adultNum} adults drinks.') if adultDrink > 0 else print('No adult\'s drinks.')
if adults == 'no':
    print('*No order for adults*')
print('===============================')
print(f'Subtotal: ${subtotal:.2f}')
print(f'SalesTax: ${salesTax:.2f}')
print(f'Tip: ${tipAmount:.2f}') if tip == 'yes' else print('*No tips*')
print('-------------------------------')
print(f'Total: ${total:.2f}')
print('-------------------------------')

payAmount = float(input('\nWhat is the payment amount? '))
change = payAmount - total

print('-------------------------------')
print(f'Change: ${change:.2f}')
print('-------------------------------')