import random

bushes = int(input("Укажите количество кустов на грядке: "))

berries = []
for i in range(bushes):
    berries.append(random.randint(1,100))

print(f"Наша грядка: {berries}")

berries.append(berries[0])
berries.append(berries[1])

max_berries = 0

for i in range(bushes):
    sum = berries[i] + berries[i + 1] + berries[i + 2]
    if sum > max_berries:
        max_berries = sum
print(f"Максимальное число ягод за один заход - {max_berries}")
