def sum(a,b :int) -> int:
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)

a = int(input('Введите а = '))
b = int(input('Введите b = '))

print(sum(a,b))