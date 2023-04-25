#todo 1: создайте модуль serializer
# В модуле реализуйте три функции сериализации
# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"

import pickle
import json
import yaml
from yaml.loader import SafeLoader


obj = {"one": 123, "two": [1, 2, 3]}

file = "task39"




def to_pickle(obj, file):

    file = open(f'{file}.pkl', "wb")
    pickle.dump(obj, file)
to_pickle(obj, file)

#  Функция сериализует объект в json
def to_json(obj, file):
    with open(f'{file}.json', "wt") as f:
        json.dump(obj, f, indent=4)


to_json(obj, file)


# Функция сериализует объект в yaml
def to_yaml(obj, file):
    with open(f'{file}.yaml', 'wt') as f:
        yaml.dump(obj, f)

to_yaml(obj, file)

#todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции десериализации


# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    with open(f'{file}.pkl', "rb") as f:
        obj = pickle.load(f)
        print(obj)
    # ваш код

from_pickle(file)


# Функция десериализует объект из файла типа json
def from_json(file):
    with open(f'{file}.json', "rt") as f:
        obj = json.load(f)

    print(obj)


from_json(file)


# Функция десериализует объект из файла типа yaml
def from_yaml(file):
    with open(f'{file}.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)
    print(obj)


from_yaml(file)

#todo 3: Cоздайте пакет из двух модулей serializer и deserializer.

# Импортируйте модули пакета в отдельный файл и протестируйте все функции.