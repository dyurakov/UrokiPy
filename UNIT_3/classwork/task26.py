#
#  Напишите функцию, которая принимает два аргумента, lst - список чисел и x – число.
#  Функция возвращает список, содержащий квадраты чисел из lst, которые больше числа x.
#  Сделайте несколько вариантов решений:
#  1) Просто цикл с условием.
#  2) Воспользуйтесь функцией filter, для чего создайте функцию проверки числа больше x

lst = [1, 3, 5, 6, 10,]
global x
x = 15


def func(lst, c):
    math = []

    for i in range(len(lst)):
        rez = lst[i]**2
        if rez > c:
            math.append(rez)

    return math

print(func(lst,x))


rez = list(map(lambda a: a**2,  list(filter(lambda lst: lst**2>x, lst))))

print(rez)