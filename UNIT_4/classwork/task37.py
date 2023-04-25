# Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import logging
global sch


slovar = {}

logging.basicConfig(level=logging.INFO, filename="task37.log", filemode="w", format=f"%(message)s %(asctime)s")





def decorator_render(func):
    global sch, slovar

    #print(func.__name__ in slovar)

    if (func.__name__ in slovar) == True:

        slovar[func.__name__] = slovar.get(func.__name__) + 1

    else:
        slovar[func.__name__] = 1

    logging.info(f"{func.__name__} , {slovar.get(func.__name__)}, ")

    def wrapper(text):
        print(f"Логика перед вызовом функции")
        func(text)
        print("Логика после вызова функции")
    return wrapper


for _ in range(5):
    @decorator_render
    def render(text,a):
        return print(text.upper())

for _ in range(7):
    @decorator_render
    def show(text):
        return print(text.upper())




