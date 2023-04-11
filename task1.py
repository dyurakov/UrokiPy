

x1=input("Введите число 1: \n")
x2=input("Введите число 2: \n")

def vicheslenie(a,b):
    a = float(a)
    b = float(b)
    print(f'Сумма {a+b}')
    print(f'Разность {a-b}')
    print(f'Возведение в степень {a ** b}')

    if int(b)==0:
        print("Делить на ноль нельзя")
    else:
        print(f'Частное {a/b}')
        print(f'Целочисленное деление {a // b}')
        print(f'Деление с остатком  {a % b}')


vicheslenie(x1, x2)