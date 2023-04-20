# Заданы два списка. Необходимо их сериализовать в один файл.

import json
import pickle
import yaml

list_one = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
list_two = [False, 'Sparse is better than dense.', {'age': 90}]

stroka = list_one + list_two

with open(f'task35.json', 'wt') as f:
    json.dump(list_one, f, indent=4)
    json.dump(list_two, f, indent=4)


with open(f'task35_2.json', 'wt') as f:
    json.dump(stroka, f, indent=4)



with open('task35.pkl', 'wb') as f:
    pickle.dump(list_one, f)
    pickle.dump(list_two, f )


with open(f'task35.yaml', 'wt') as f:
    yaml.dump(list_one, f)
    yaml.dump(list_two, f)