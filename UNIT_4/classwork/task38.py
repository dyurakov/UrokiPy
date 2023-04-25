#  Задача 1. Транспонирование матрицы, transpose(matrix)
#  Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10


list = [x for x in range(10+1) for _ in range(x) ]





# Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||

matrix = [[1, 2, 3], [4, 5, 6]]


def transpose(matrix):
    transp = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transp



print(transpose(matrix))

# Задача 3. Найти сумму элементов матрицы
# Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)


def msum(matrix):
    matr = sum(col for row in matrix for col in row)
    return matr


print(msum(matrix))
