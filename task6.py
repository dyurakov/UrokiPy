import time

A = ''
B = ''
C = ''

print(f'Содержимое переменной A: {A}')
print(f'Содержимое переменной B: {B}')
print(f'Содержимое переменной C: {C}')


A = int(input("Введите A: \n"))

B=A
print(f'Содержимое переменной B: {B}')
time.sleep(1)

C=B
print(f'Содержимое переменной C: {C}')
time.sleep(1)

A=C
print(f'Содержимое переменной A: {A}')
time.sleep(1)

A = 1
B = 2
C = 3