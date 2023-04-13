# todo: Напишите калькулятор (простой). На вход подается строка, например:
#   1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
#   Вывод: сосчитать и напечатать результат операции.
#   Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.


in_string = input('Вычислить: ')
# print(in_string)


def find_probel(stroka):
    all_probel = []
    for j in range(len(stroka)):
        if stroka[j] == ' ':
            all_probel = all_probel + [j]
            # print(all_probel)

    all_probel = all_probel + [0] + [len(stroka)]
    all_probel.sort()
    # print(all_probel)
    if len(all_probel) != 4:
        print('Программа остановлена (Введена не верная операция)\n Пример: <5 + 9>')
        exit(0)

    return all_probel

# разбираю строку на операнды и операции
def parsing_string(probel, in_string):
    operacii = ['+', '-', '*', '/']
    operand1 = float(in_string[probel[0]:probel[1]])
    operand2 = float(in_string[probel[-2]:probel[-1]])
    operaciya = in_string[probel[1]:probel[-2]].replace(' ','')

    # Проверяем знак операции
    if len(operaciya) > 1:
        print('Программа остановлена (введена не верная операция)\nДопустимые знаки операций: + - * /')
        exit(0)

    if operaciya not in operacii:
        print('Программа остановлена (введена не верная операция)\nДопустимые знаки операций: + - * /')
        exit(0)

    # print(operand1)
    # print(operand2)
    # print(operaciya)
    return operand1, operand2, operaciya


operand1, operand2, operaciya = parsing_string(find_probel(in_string),in_string)

# Вычисляю (функция не обязательна здесь, но решил всё черз них писать)
def vicheslenie(operand1, operand2, operaciya):
    match operaciya:
        case '+':
            return operand1 + operand2
        case '-':
            return operand1 - operand2
        case '*':
            return operand1 * operand2
        case '/':
            # Проверяем деление на ноль
            if operand2 == 0:
                print('На ноль делить нельзя')
                exit(0)
            else:
                return operand1 / operand2



print(f'{in_string} = {vicheslenie(operand1, operand2, operaciya)}')







"""
def parsing_string(in_str):

    # Узнаём какую орерацию выбрали для вычисления
    sch = 0
    
    for i in operaciya:
        if i in in_str:
            print(in_str.index(i))
            operaciya = in_str[in_str.index(i)]

            print(operaciya)
            sch += 1
    if len(operaciya)>1 or sch >=2:
        print('Программа остановлена (Введена не верная операция)')

"""








