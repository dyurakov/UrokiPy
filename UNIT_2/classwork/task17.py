# Вводится число, например: 1231.
# Вывести строчку, например: один два три один.
# Подсказка: создайте словарь


chislo = str(12310553.2)

dic = {
    '0': 'ноль',
    '1': 'один',
    '2': 'два',
    '3': 'три',
    '4': 'три',
    '5': 'три',
    '6': 'три',
    '7': 'три',
    '8': 'три',
    '9': 'три',
    '.': 'точка',
}

slovar = ''

for i in range(len(chislo)):
    slovar = slovar + f' {dic.get(chislo[i])}'
print(slovar)
