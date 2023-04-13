#todo: Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка lst.
# B Python есть функция min, которая решает эту задачу. Но напишите свою функцию, которая не использует функцию min.






lst = [1, 20, 3, 5, 4.4, 11, 0]

def find_min(lst):

    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            save = lst[i]

            print(lst[i])










print(find_min(lst))