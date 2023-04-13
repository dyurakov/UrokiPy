"""
# Ввод: 2 слова, разделенных пробелами. Для ввода используем функцию s = input().split()
# Определить, являются ли эти слова анаграммами (словами с одинаковым набором букв). Если да, то True. Если нет, то False.
# (Примеры: АКВАРЕЛИСТ-КАВАЛЕРИСТ, АНТИМОНИЯ-АНТИНОМИЯ, АНАКОНДА-КАНОНАДА, ВЕРНОСТЬ-РЕВНОСТЬ, ВЛАДЕНИЕ-ДАВЛЕНИЕ, ЛЕПЕСТОК-ТЕЛЕСКОП)
"""

# s = input('Введите 2 слова через пробел: ').split()
s = ['ВеРнОСТЬ', 'РЕВНОСТь']


if len(s) != 2:
    print('Ошибка! - введено не 2 слова')


def razbienie_slov(slovo):

    razbitoe_slovo = []
    for i in slovo:
        razbitoe_slovo = razbitoe_slovo + [i.lower()]
    return razbitoe_slovo


nojestvo1 = set(razbienie_slov(s[0]))
nojestvo2 = set(razbienie_slov(s[1]))


subset_check = nojestvo1.issubset(nojestvo2)
print(subset_check)
