# Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка lst.
# B Python есть функция min, которая решает эту задачу. Но напишите свою функцию, которая не использует функцию min.






lst = [-10000, -20000, 3, 0, -100, 5, 10, -5000, -2000]
global save

def min_znach(list):
    list.sort()
    return list[0]
print(f'Минимальный элемент по функции sort: {min_znach(lst)}')


def find_min(list):
    i = 0
    vozmojno_min = []


    for j in range(len(list)):
        if list[i] < list[j]:
            vozmojno_min = vozmojno_min + [list[i]]
            i += 1


    if len(vozmojno_min) == 1:
        #print(vozmojno_min[0])
        save = vozmojno_min[0]
        return save

    else:
        return find_min(vozmojno_min)
        """
            Эта функция не работает корректно, потому что в случае, когда вызывается функция find_min(vozmojno_min) 
            внутри самой себя, её результат не возвращается во внешний вызов рекурсии.
            Чтобы исправить эту проблему, в строке find_min(vozmojno_min) нужно добавить оператор return перед вызовом функции:
        """



print(f'Минимальный элемент по функции перебора: {find_min(lst)}')

