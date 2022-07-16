people = [
  "Stephanie 36",
  "John 29",
  "Emily 24",
  "Gretchen 54",
  "Noah 12",
  "Penelope 32",
  "Michael 2",
  "Jacob 10"
]

youngest_age = 9999
younges_name = ''

#Iterate through the list and display each string to the screen.
for person in people:
  #Split the string into a name and age and print them to the screen.
  person = person.split(' ')
  #print(person)
  #variables
  name = person[0]
  age = int(person[1])

  #find the youngest
  if age < youngest_age:
    youngest_age = age
    younges_name = name

print(f'The youngest person is: {younges_name} with an age of {youngest_age}')