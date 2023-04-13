#На вход подается предложение из нескольких слов. Слова разделены пробелами.
# Напечатайте самое длинное слово в этом предложении.


str = 'abc aaaaa fevfdvf bz fghjklkjhgfvbn'

def find_probel(srt):
    all_probel = []
    for i in range(len(str)):
        if str[i]==' ':
            all_probel = all_probel+[i]
            #print(all_probel)

    all_probel = all_probel + [0] + [len(str)]
    all_probel.sort()
    #print(all_probel)
    return all_probel

probel = find_probel(str)


# Находим все слова
slovar = []
dlina = []
for i in range(len(probel)-1):
    #print(i)
    slovo = str[probel[i]:probel[i+1]]
    slovar.append(slovo.replace(' ',''))
    dlina.append(len(slovo.replace(' ','')))


max_dl_slovo = slovar[dlina.index(max(dlina))]


print(f'Самое длинное слово из списка: {max_dl_slovo}')

