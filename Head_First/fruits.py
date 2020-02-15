fruits = {}
fruits['apples'] = 10

if 'bananas' in fruits:
    fruits['bananas'] += 1
else:
    fruits['bananas'] = 1

fruits.setdefault('pears', 0)
fruits['pears'] += 1

print(fruits)