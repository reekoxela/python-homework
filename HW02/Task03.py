limit = int(input("Укажите число: "))

count = 0
result = 1

print(f"Все целые степени двойки, не превосходящие числа {limit}: ")
while result < limit:
    result = 1
    for i in range(count):
        result *= 2
    count += 1
    if result < limit:
        print(result, end = " ")
