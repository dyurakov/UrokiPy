#  На вход подается список, состоящий из списков чисел, например: [[1,5,3], [2,44,1,4], [3,3]].
#  Отсортируйте этот список по возрастанию общего количества цифр в каждом списке.
#  Каждый список отсортируйте по убыванию.

spisok = [[1, 5, 3, 0], [2, 44, 1, 4], [3, 10, 5, 9], [5], [1, 3]]


def sortByLength(inputStr):
    return len(inputStr)

for i in range(len(spisok)):
    spisok[i].sort(reverse=True)

spisok.sort( key = len)

print(spisok)



