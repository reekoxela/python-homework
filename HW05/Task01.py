def degree(number, degree_number: int) -> int :
    if degree_number == 1:
        return number
    else:
        return number * degree(number,degree_number - 1)

number = int(input('Укажите число: '))
degree_number = int(input('Укажите степень числа: '))

print(f'{number}^{degree_number} = {degree(number, degree_number)}')
