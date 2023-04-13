# Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).

from my_func import razbienie_slov

alfavit = 'йцукенгшщзхъфывапролджэячсмитьбюё'

# stroka = ' вапролджэяч см1234567890/*-+.?,!@# $%^&*итьб юёйцукенгшщзхъфыа фвмыаиапи grtgberbmm,mkwemvqe,v,,'
stroka = input('Введите строку: ')

# print(razbienie_slov(alfavit))

mnojestvo_s = set(razbienie_slov(stroka))
mnojestvo_a = set(razbienie_slov(alfavit))


# Находим пересечение множеств
peresechenie = mnojestvo_s.intersection(mnojestvo_a)
# print(peresechenie)

# Проверяем объединение множеств
check = mnojestvo_a.issubset(peresechenie)

if check is True:
    print('\nВведённая строка является панграммой (т.е. в ней содержатся все 33 буквы русского алфавита)')
else:
    print('Введённая строка НЕ является панграммой (т.е. в ней НЕ содержатся все 33 буквы русского алфавита)')