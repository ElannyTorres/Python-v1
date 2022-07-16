""" 
with open("courses.txt") as courses_file:
  for course in courses_file:
    print(course)
"""
#colors.split() => split the list for each whitespace
#color.split('e) => choosing how it will split
""" 
Removing whitespace from strings from the begin and the end
name.strip()
"""
""" with open("books.txt") as books_file:
  for book in books_file:
    book = book.strip()
    print(book) """

line = "     text"

line = line.strip()

print(line)