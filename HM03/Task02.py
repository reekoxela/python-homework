ru = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
en = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

en_letters = {1: "A,E,I,O,U,L,N,S,T,R", 2: "D,G", 3: "B,C,M,P", 4: "F,H,V,W,Y", 5: "K", 8: "J,X", 10: "Q,Z"}
ru_letters = {1: "А,В,Е,И,Н,О,Р,С,Т", 2: "Д,К,Л,М,П,У", 3: "Б,Г,Ё,Ь,Я", 4: "Й,Ы", 5: "Ж,З,Х,Ц,Ч", 8: "Ш,Э,Ю", 10: "Ф,Щ,Ъ"}

word = input("Введите слово: ").upper()

ru_letter = 0
en_letter = 0
for letter in word:
    if letter in ru:
        ru_letter += 1
    elif letter in en:
        en_letter += 1
    else:
        print("Словно введено не верно")
        exit()

if ru_letter > 0 and en_letter == 0:
    ru_flag = True
elif ru_letter == 0 and en_letter > 0:
    ru_flag = False
else:
    print("Словно введено не верно")
    exit()

sum = 0

for letter in word:
    if ru_flag:
        for symbol in ru_letters.items():
            if letter in symbol[1]:
                sum += symbol[0]
    else:
        for symbol in en_letters.items():
            if letter in symbol[1]:
                sum += symbol[0]

print(f"Стоимость слова {sum} очков")



