#  Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#       Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
#       Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)

'''
# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
>4

#Введите  массу тела
>1

Ответ: 1000 кг
'''


while True:
    print('Введите единицу массы, где: \n 1 — килограмм\n 2 — миллиграмм\n 3 — грамм\n 4 — тонна\n 5 — центнер\n 0 — Выход\n')
    menu = int(input('Ввод: '))
    if menu in range(1,5+1,1):
        print()
    elif menu == 0:
        exit(0)
    else:
        print('Повторите попытку!\n\n')
        continue

    print(f'Введите массу')
    massa = float(input('Ввод: '))

    match menu:
        case 1:
            print(f'Ответ: {massa} кг\n\n\n\n')
        case 2:
            print(f'Ответ: {massa / 1e6} кг\n\n\n\n')
        case 3:
            print(f'Ответ: {massa / 1e3} кг\n\n\n\n')
        case 4:
            print(f'Ответ: {massa * 1e3} кг\n\n\n\n')
        case 5:
            print(f'Ответ: {massa * 1e2 } кг\n\n\n\n')











