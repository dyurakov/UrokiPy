# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
#       слева направо и справа налево".

# Проверка на 4х значность
while True:
    chislo = input("Введите 4х значное число: ")

    # Заменяем запятую на точку если такая была
    if ',' in chislo:
        chislo = chislo.replace(',', '.')

    if len(chislo.replace('.',''))==4:
        print(f'Введено число: {chislo}')
        break
    else:
        print(f"Вы ввели {len(chislo.replace('.','')) }-значное число\nПовторите попытку\n")
        continue

# Проверка того что это будет действительно число
if type(float(chislo)):
    pass

# Функция проверки числа на чтение туда-сюда
def sravnenie(p_chislo):
    r_chislo = p_chislo[::-1]
    print(f'Обратное число {r_chislo}')

    if p_chislo.replace('.','') == r_chislo.replace('.',''):
        print(f'Данное четырехзначное число ({p_chislo}) читается одинаково слева направо и справа налево')
    else: print(f'Данное четырехзначное число ({p_chislo}) читается НЕ одинаково слева направо и справа налево')




'''
# Проверка на тип введённого числа (МОЖНО ВЫКИНУТЬ)
if len(str(float(chislo)).replace('.',''))==4:
    print(f'Введено число типа float')
    sravnenie(chislo)
else:
    print(f'Введено число типа int')
    sravnenie(chislo)
'''





        
        

