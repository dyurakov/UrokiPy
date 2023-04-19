# Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

import array as arr
list = [1,2,3,4,5,6,7,8,9,0]


massiv = arr.array('i',list)

print(massiv)


for i in range(len(massiv)):
    massiv[i] = massiv[i]+1
print(massiv)