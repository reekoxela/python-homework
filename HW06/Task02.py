from random import randint as RI

#my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

list_size = int(input('Укажите длину списка: '))
my_list = []
for _ in range(list_size):
    my_list.append(RI(-50,50))

print(f'Список: {my_list}')

min_range = int(input('Укажите минимум диапазона: '))
max_range = int(input('Укажите максимум диапазона: '))

index_list = []
for item in range(len(my_list)):
    if min_range <= my_list[item] <= max_range:
        index_list.append(item)

print(f'Индексы элементов списка, значения которых принадлежат диапазону [{min_range} .. {max_range}] -> {index_list}')
