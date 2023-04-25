#  Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.


import calendar

year = 2023
month = 4


def return_dat(year, month):
    dat = calendar.monthrange(year, month)
    dats = [den for den in range(1, dat[1]+1)]
    return dats


print(return_dat(year, month))