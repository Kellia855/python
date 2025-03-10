#!/usr/bin/env python3
LibraryBooks = {'Never never','November 9','Verity','Safe harbor', 'Malala','The Egyptian'}
Book = input('What is th title of the book?')
print('checking if the book is in the library catalog...')
for Book in LibraryBooks:
     print(Book)
     if Book in LibraryBooks:
         print('Book found')
else:
        print('Book not found')
        