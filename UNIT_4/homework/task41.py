#
#  В Python существуют ключевые слова, которые нельзя использовать для названия переменных, функций и классов.
#  Для получения списка всех ключевых слов можно воспользоваться атрибутом kwlist из модуля keyword.
#  Приведенный ниже код:
#  import keyword
#  print(keyword.kwlist)
#  выводит: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
#  'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#  Напишите программу, которая принимает строку текста и заменяет в ней все ключевые слова на <kw>.

import keyword

lst = ['False', 'Moms', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
       'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
       'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'Faza','yield']

# print(keyword.kwlist)

keyword_list = keyword.kwlist

keyword_slovar = {x: '<kw>' for x in keyword_list}

print(keyword_slovar)
new_list =[]

for i in range(len(lst)):
    if lst[i] in keyword_slovar:
        new_list.append(keyword_slovar.get(lst[i]))
    else:
        new_list.append(lst[i])

print(new_list)


