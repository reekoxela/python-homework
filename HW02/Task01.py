#Вывести минимальное количество монет, которые нужно перевернуть
from random import randint as RI

coins_count = int(input("Укажите количество монеток: "))
heads = 0
tails = 0

for i in range(coins_count):
    coin = RI(0,1)
    print(coin, end = ' ')
    if coin == 0:
        heads += 1
    else:
        tails += 1

print("\n")

if heads > tails:
    print(f"Необходимо перевернуть {tails} монеток")
elif heads < tails:
    print(f"Необходимо перевернуть {heads} монеток")
else:
    print(f"Переверните {heads} монеток. Число гербов и решек равно!")