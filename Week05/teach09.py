#Start
print('Enter a list of numbers, type 0 when finished.')
numbers = []
number = -1
#Core
while number != 0:
    number = int(input('Enter number: '))
    if number != 0:
        numbers.append(number)

#sum
total = sum(numbers)
print(f'The sum is: {total}')

#average
average = total/len(numbers)
print(f'The average is : {average}')

#High
numbers.sort(reverse=True)
highest = numbers[0]
print(f'The largest number is : {highest}')

#Small Positive
least = highest
for num in numbers:
    if num < least and num > 0:
        least = num
print(f'The smallest positive number is: {least}')

#Sort
print('The sorted list is:')
numbers.sort()
for num in numbers:
    print(num)