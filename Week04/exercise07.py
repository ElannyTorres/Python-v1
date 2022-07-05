# loop
""" items = ['crayon', 'scissors', 'paper', 'glitter glue', 'markers', 'pens']

for item in items:
  print(f'The item is: {item}') """

#looping through numbers
#first way
""" numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
  print(f'The number is: {number}') """
#easier way:
#range(10) creates a list of number that starts at 0 and goes up until, but not includding, 10
""" for number in range(11):
  print(f'The number is: {number}') """
# range(start_num, end_num)
""" for i in range(100, 200):
  print(i) """
# range(start_num, end_num, gap)
""" for i in range(10, 200, 10):
  print(i) """
# Loops within loops
""" for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f"--{j}") """

#Looping through strings
""" first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}") """

# Access a letter by its index
#first_name = "Brigham"
""" fourth_letter = first_name[3]
print(fourth_letter) """
""" for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")

dog_name = input("What is your dog's name? ")
letter_count = len(dog_name)
print(f"Your dog's name has {letter_count} letters") """

first_name = "Brigham"
total_letters = len(first_name)

for i in range(total_letters):
    letter = first_name[i]
    print(f"The letter is: {letter}")