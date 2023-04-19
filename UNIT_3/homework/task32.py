# Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT

dnk = 'GGCTAA'

_dnk = 'GCTA'
_rnk = 'CGAT'

slovar = {}
for j in range(len(_dnk)):
    slovar[_dnk[j]] = _rnk[j]


def dnk2rnk(dnk, slovar):
    rnk = ''
    for i in range(len(dnk)):
        rnk = rnk + slovar.get(dnk[i])


    return rnk



print(f"ДНК: {dnk} \nРНК: {dnk2rnk(dnk, slovar)}")