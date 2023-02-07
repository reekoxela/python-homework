from random import randint as RI

length_list = int(input("Укажите длину списка: "))

my_list = []
for i in range(length_list):
    my_list.append((RI(0,10)))
print(f"Список: {my_list}")

req_number = int(input("Укажите искомое число: "))

count = 0
for i in my_list:
    if i == req_number:
        count += 1

if count > 0:
    print(f"Число {req_number} встречается в заданном списке {count} раз(а)")
else:
    my_dict = {}
    for i in my_list:
        my_dict[i] = abs(i - req_number)

    nearest_num = set()
    min_value = min(my_dict.values())
    for i in my_dict.items():
        if i[1] == min_value:
            nearest_num.add(i[0])
    print(f"Максимально близкое к {req_number} - {nearest_num}")
