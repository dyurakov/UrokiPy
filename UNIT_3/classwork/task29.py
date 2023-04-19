#
#  Реализуйте функцию convert(), которая принимает один аргумент:
#  number — целое число
#  Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
#  двоичное представление числа number в виде строки без префикса 0b
#  восьмеричное представление числа number в виде строки без префикса 0o
#  шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x
#  Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().
#  Задачу решить доступным способом
#  Задачу решить с помощью применения функции map и lambda

number = 4

def conver(number):

    cb = str(bin(number))[2::]
    co = str(oct(number))[2::]
    ch = str(hex(number))[2::]
    convert = (cb, co, ch)

    return convert


def converting(number):



    convert = (bin, oct, hex)
    convert = list(map(lambda fn: fn(x)[2::], convert ))

    return convert



print(converting(number))