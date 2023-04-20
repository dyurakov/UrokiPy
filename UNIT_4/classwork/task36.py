#
# Реализовать декоратор, который подсчитывает время выполнения функции.

import time

def decorator_render(func):
    print("Call decorator function")
    def wrapper(text):
        print(f"Логика перед вызовом функции")
        start_time = time.time()
        func(text)
        end_time = time.time() - start_time
        print(f'Время выполнеия {end_time}')
        print("Логика после вызова функции")
    return wrapper


@decorator_render
def render(text):
    return print(text.upper())

render('аргумент1')