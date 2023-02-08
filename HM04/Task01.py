# set_A = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
# set_B = {3, 6, 9, 12, 15, 18}
# print(set_A)
# print(set_B)
# z = set_A.intersection(set_B)
# print(sorted(z))

# set_a = [2,4,6,8,10,12,10,8,6,4,2]
# set_b = [3,6,9,12,15,18]

n = int(input("Количество элементов первого множества: "))
m = int(input("Количество элементов второго множества: "))

set_a = []
set_b = []

print("Элементы первого множества: ")
for i in range(n):
    set_a.append(int(input(f"Введите {i + 1} - элемент: ")))

print("Элементы второго множества: ")
for i in range(m):
    set_b.append(int(input(f"Введите {i + 1} - элемент: ")))

print(f"Первое множество: {set_a}")
print(f"Второе множество: {set_b}")

my_set = set()
for i in set_a:
    for j in set_b:
        if i == j:
            my_set.add(i)

print(f"Числа, встречающиеся в обоих наборах: {sorted(my_set)}")

