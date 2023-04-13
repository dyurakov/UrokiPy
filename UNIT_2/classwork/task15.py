# todo: Дан кортеж (123, 234, 345, 456, 567, 678, 789, 890).
#  Вводится ещё одно целое число больше 0.
#  Создайте новый кортеж из первого кортежа и введенного числа, чтобы в новом кортеже числа не убывали.


cortej = (123, 234, 345, 456, 567, 678, 789, 890)

'''
print( 'Введите число болше 0')
while True:
    chislo = float(input('input --> '))
    if chislo > 0:
        break
    else:
        print('Число должно быть больше 0!')
        continue
'''


chislo = 54


new_cortej = cortej[:] + (chislo,)

print(f'Старый кортеж: {cortej}')
print(f'Новый кортеж: {tuple(sorted(new_cortej )) }')