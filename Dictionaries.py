book = {
    'title' : 'The Silence of the Lambs',
    'author' : 'William Thomas Harris',
    'year' : '1988'
}
print(f'Values of the book = {list(book.values())}')
book['genre'] = 'Psychological Horror'
print('The Entire Updated Book is printed below:')
for i in book.items():
  print(i)