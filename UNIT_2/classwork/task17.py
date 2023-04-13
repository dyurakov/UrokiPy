# Вводится число, например: 1231.
# Вывести строчку, например: один два три один.
# Подсказка: создайте словарь


chislo = str(1231)



dic = {
    '1': 'один',
    '2': 'два',
    '3': 'три'
}

slovar = ''

for i in range(len(chislo)):
    slovar = slovar + f' {dic.get(chislo[i])}'

print(slovar)