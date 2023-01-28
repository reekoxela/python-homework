#Сумма цифр трехзначного числа
number = int(input("Введите трехзначное число: "))
if number < 100 or number > 999:
    print("Ошибка: вы ввели не трехзначное число!")
else:
    sum = number % 10
    ost_num = number // 10
    sum += ost_num % 10
    ost_num //= 10
    sum += ost_num
    print(f"Сумма цифр числа {number} равна {sum}")