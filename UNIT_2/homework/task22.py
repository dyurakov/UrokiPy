# Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.




#stroka = 'qwertyuiopasdfghjklzxcvbnm'
#en_stroka = sorted(stroka)
n = 1


def shift_string(string, n):
    new_string = []
    # new_string = string[-n::] + string[0:-n]
    new_string = string[n::] + string[0:n]

    #for i in range(len(string)):
    #    new_string[i] = string[i+n]

    # print(new_string)
    return new_string


# print(shift_string(en_stroka,n))

    # for i in range(len(string))

def create_slovar(keys,value):
    slovar_caesar = {}
    for i in range(len(keys)):
        slovar_caesar[keys[i]] = value[i]

    return slovar_caesar


def code(string, n):
    pass
    stroka = 'qwertyuiopasdfghjklzxcvbnm'
    en_stroka = sorted(stroka)
    EN_STROKA = sorted(stroka.upper())
    en_stroka_caesar = shift_string(en_stroka, n)
    EN_STROKA_caesar = shift_string(EN_STROKA, n)

    en_stroka_caesar = create_slovar(en_stroka, en_stroka_caesar)
    EN_STROKA_caesar = create_slovar(EN_STROKA, EN_STROKA_caesar)

    en_stroka_caesar.update(EN_STROKA_caesar)
    # print(en_stroka_caesar)

    string_input = []
    for i in range(len(string)):

            # print(string[i])

            try:
                # print(en_stroka_caesar[string[i]])
                string_input.append(en_stroka_caesar[string[i]])

            except:
                string_input.append(string[i])
                # print(string[i])

    string_input = ''.join(map(str, string_input))

    print(f'String encode Caesar> {string_input}')


code('But what if the list contains both string and integer as its element. In those cases, above code won’t work.', n)



















