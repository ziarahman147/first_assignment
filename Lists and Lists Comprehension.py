fruits = ['Avocado', 'Orange', 'Grape', 'pineapple', 'Blueberry']
print(fruits)
fruits_length = [len(i) for i in fruits]
print(f'Length of each fruit = {fruits_length}')
#New Fruit Appended
fruits.append('lemon')
fruits.sort()
#fruits.sort(reverse= True)
print(f'Sorted Fruits: {fruits}')