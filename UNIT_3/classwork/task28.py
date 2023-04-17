#
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda

lst = [123, 234, 345, 456]

lst_str = []
for i in range(len(lst)):
    lst_str.append(str(lst[i]))


summ = list(map(lambda x: int(x[0]) + int(x[1]) + int(x[2]), lst_str))


print(f'Вывод: {summ}')