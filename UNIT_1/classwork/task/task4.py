# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().


a = float(input("Введите A: \n"))
b = float(input("Введите B: \n"))

def urovnenie(A, B):
    if A != 0:
        return (-B)/A
    else: print('A = 0 | Решение невозможно')


print(f'\nx = {urovnenie(a, b)}')
