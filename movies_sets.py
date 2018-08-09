lauren = {'Dumb & Dumber', 'Catch Me if You Can', 'Bridget Jones Diary'}
derek = {'Star Wars', 'Lord of the Rings', 'Dumb & Dumber'}

print('Here are my favorite movies:')
print(lauren)
print('Here are Dereks favorite movies:')
print(derek)

union = lauren.intersection(derek)
print('Here are the movies that we have in common:')
print(union)

lauren_only = lauren.difference(derek)
print('Here are the movies that Lauren likes but Derek doesnt:')
print(lauren_only)
