chose_scripture = input('Which volume of scriptures would you like to learn about? ')

max_chapters = -1
book_max = ""

with open('books_and_chapters.txt') as f:
  
  for line in f:

    line = line.strip()
    parts = line.split(':')
    
    book = parts[0].strip()
    chapters = int(parts[1])
    scripture = parts[2].strip()
    
    if scripture.lower() == chose_scripture.lower():
      if chapters > max_chapters:
        max_chapters = chapters
        book_max = book

print(f"The book with the most chapters is: {book_max}")
print(f"It has {max_chapters} chapters.")