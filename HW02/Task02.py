LIMIT = 1000

sum = int(input("Сумма чисел: "))
composition = int(input("Произведение чисел: "))

for x in range(LIMIT):
    for y in range(LIMIT):
        if (x + y == sum) and (x * y == composition):
            print(f"Задуманные числаx: {x} и {y}")
            exit()
else:
    print("Указанные сумма или произведение не соответствует загаданным числам")

