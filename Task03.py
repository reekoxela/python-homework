#программа проверяет счастливость билета
number = int(input("Введите номер билета: "))
if number < 100000 or number > 999999:
    print("Ошибка: неверный номер билет! Номер должен быть шестизначным")
else:
    left_sum = number % 10
    number //= 10
    left_sum += number % 10
    number //= 10
    left_sum += number % 10
    number //= 10
    right_sum = number % 10
    number //= 10
    right_sum += number % 10
    right_sum += number // 10
    if left_sum == right_sum:
        print("Билет счастливый")
    else:
        print("Билет не счастливый")