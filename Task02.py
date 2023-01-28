#Задача про журавликов
num_cranes = int(input("Сколько журавликов сделали дети вместе: "))
petya_serg = num_cranes / 6
katya = num_cranes - 2 * petya_serg   #katya = petya_serg * 4
print(f"Петя сделал {petya_serg} журавликов")
print(f"Сережа сделал {petya_serg} журавликов")
print(f"Катя сделала {katya} журавликов")
