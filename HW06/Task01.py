first_element = int(input('Первый элемент списка: '))
difference = int(input('Укажите разность: '))
list_size = int(input('Размер списка: '))

print('Арифметическая прогрессия', end = ': ')
for i in range(list_size):
    print(first_element + i * difference, end = ' ')