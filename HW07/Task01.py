
chant = input("Кричалка Винни-Пуха: ")
chant_list = chant.upper().split()

count_syllable = lambda item: sum(1 for letter in item if letter in "АЕЁИОУЫЭЮЯ")
first_phrase = count_syllable(chant_list[0])

matches = True
for item in range(1, len(chant_list)):
    if count_syllable(chant_list[item]) != first_phrase:
        matches = False
        break

if matches:
    print("Парам пам-пам")
else:
    print("Пам парам")


