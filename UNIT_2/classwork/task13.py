# todo:  Ввести число n. Напечатать треугольник из символов +.
#  Пример для n = 5:
'''
+
++
+++
++++
+++++
'''


n = 6

def treugolnic(chislo):
    e='*'
    for i in range(chislo):
        if i == 0:
            print(e)
        else:
            e = e + '*'
            print(e)

treugolnic(n)


