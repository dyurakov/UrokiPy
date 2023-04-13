# На вход подается предложение из нескольких слов. Слова разделены пробелами.
# Напечатайте самое длинное слово в этом предложении.

# str = 'abc aaaaa fevfdvf bz fghjklkjhgfvbn'
str_ = input('Введите предложение: ')


def find_probel(stroka):
    all_probel = []
    for j in range(len(stroka)):
        if stroka[j] == ' ':
            all_probel = all_probel + [j]
            # print(all_probel)

    all_probel = all_probel + [0] + [len(stroka)]
    all_probel.sort()
    # print(all_probel)
    return all_probel


probel = find_probel(str_)

# Находим все слова
slovar = []
dlina = []
for i in range(len(probel) - 1):
    # print(i)
    slovo = str_[probel[i]:probel[i + 1]]
    slovar.append(slovo.replace(' ', ''))
    dlina.append(len(slovo.replace(' ', '')))

max_dl_slovo = slovar[dlina.index(max(dlina))]
print(f'Самое длинное слово из списка: {max_dl_slovo}')
