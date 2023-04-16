# Написать игру "Поле чудес"
'''
Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
либо победы.

Пример вывода:

"Это слово обозначает наименьшую автономную часть языка программирования"

▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

Введите букву: O

O  ▒  ▒  ▒  ▒  ▒  O  ▒


Введите букву: Я

Нет такой буквы.
У вас осталось 9 попыток !
Введите букву:

'''
import random

number=random.randint(0,2)


words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "Инструкция, которую интерпретатор может выполнить", "Как в языке Python называется экземпляр класса или любая другая переменная, которая может иметь атрибуты и методы?" ]

slovo = words[number]

#slovo = words[0]
#print(slovo)

print(desc_[number])

p= 10

# Функция поиска буквы в слове
def finf_bukv(sl,bukv):
    open_bukv = []
    for i in range(len(sl)):
        if bukv == sl[i]:
            open_bukv.append(i)
    return open_bukv


def dev_sikret_slovo(sl,open_bukv):
    sikret_slovo = ''
    #print(open_bukv)
    for i in range(len(sl)):
        if i in open_bukv:
            sikret_slovo = sikret_slovo + f'{sl[i]}'
        else:
            sikret_slovo = sikret_slovo + '▒'
    return sikret_slovo




#print(finf_bukv(slovo,'о'))

#print(dev_sikret_slovo(slovo,[1,5,6]))

histori = '' # Переменная история букв
o_bukv = [] # Индексы открытых букв

while p!=0:


    bukva = input('Введите букву: ')

    # Ищем букву в слове
    a = finf_bukv(slovo, bukva)

    # Если буква не найдена
    if len(finf_bukv(slovo, bukva)) == 0:
        print('Нет такой буквы :(')
        p=p-1

        # Если попытки кончились
        if p == 0:
            print('Вы проиграли!')
            exit(0)

        print(f'Осталось {p} попыток')
        continue

    # Если буква найдена
    else:

        if bukva in histori:
            print('\nЭта буква уже была')
            p = p - 1
            print(f'Осталось {p} попыток\n')

        else:
            histori = histori+bukva
            o_bukv = o_bukv + a

            print(dev_sikret_slovo(slovo, o_bukv))

            if len(o_bukv) == len (slovo):

                print(f'Угаданное слово: {dev_sikret_slovo(slovo, o_bukv)}')
                print(f'Вы выиграли со счётом {p} баллов/балл')

                exit(0)












