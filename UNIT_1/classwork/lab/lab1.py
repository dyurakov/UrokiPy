#!/usr/bin/python3

# todo: Необходимо реализовать консольную утилиту marge.py которая реализует функцию слияния
# содержимого файлов определенного типа с указанного каталога в один файл json при задании параметров:
'''
./ marge.py -v --root_dir=ROOT_FOLDER output.json

Где:
output.json Исходный файл
--root_dir  Директория для обработки

Структура каталогов выглядит следующим образом:
ROOT_FOLDER   -->   A  ---  w.txt
                         -  x.txt
                    B  ---  z.txt
                         -  y.txt

Результат: в файле output.json
{
  "VectorTelemetry": {
    "w": 74.72395045538597,
    "x": 74.72395045538597,
    "y": 74.72395045538597,
    "z": 74.72395045538597
  }
}
Примечание: О запуске и окончании утилиты информировать пользователя через логгер.

Перед тем как написать утилиту нужно решить локальные подзадачи в папке simple.
1. Посмотреть как работает логгер
2. Разобраться с передачей аргументов программе через коммандную строку
3. Понять как работает обход папок
Далее соединить полученные знания в утилите merge.py


Логирование
https://habr.com/ru/companies/wunderfund/articles/683880/

Парсер аргументов
https://habr.com/ru/companies/ruvds/articles/440654/
'''


import logging
import argparse
import os
import subprocess
import time
global all_files_in_root_dir
all_files_in_root_dir = []

logging.basicConfig(level=logging.INFO, filename="lab1.log",filemode="w", format="%(asctime)s %(levelname)s %(message)s")
logging.info('Скрипт запустился')
# ./ marge.py -v --root_dir=ROOT_FOLDER output.json
parser = argparse.ArgumentParser(description='Консольная утилита для выполнения слияния в один json-файл')
parser.add_argument('-rd', '--root_dir', type=str, default='./ROOT', help='Выбор директории с файлами для слияния')
parser.add_argument('-of', '--output_file', type=str, default='./output_file.json', help='Файл вывода')
parser.add_argument('-t', '--type_file', type=str, default='.txt', help='Выбор расширения файла')

arg = parser.parse_args()
global rash
rash = arg.type_file





def find_files(path):
    global all_files_in_root_dir
    '''

    :param path: Это дирректория где искать файлы
    :param rash: Файлы с каким расширением мы ищем
    :return: Возвращает найденные пути до файлов с расширением *.txt
    '''
    check_root_dir = os.listdir(f'{path}')

    sch_dir = sch_file = 0

    while True:
        # fixme: Придумать как искать файлы рекурсивно а не на два каталога во внутрь.
        for i in range(len(check_root_dir)):

            try:
                sch_dir = 0
                files = os.listdir(f'{path}/{check_root_dir[i]}/{}')
                #logging.info(f'{path}/{check_root_dir[i]} - является директорией')
                #print(files)
                for j in range(len(files)):
                    find_files(files[j])
                    logging.info(f'')

            except:
                sch_file=0
                file = f'{path}/{check_root_dir[i]}'
                logging.info(f'{file} - не является директорией')
                # Ищем файл по расширеню и добавляем его в списиок найденных
                if file[-4::]==rash:
                    if file not in all_files_in_root_dir:
                        logging.info(f'{check_root_dir[i]} - добавляется в переменную найденных файлов')
                        all_files_in_root_dir = all_files_in_root_dir + [file]
                        sch_file = 1
        time.sleep(0.1)


        # Проверка окончания поиска файлов
        #if sch_dir==0 or sch_file==0:
        #    logging.info(f'Найдены все файлы')
        #    break




    #return all_files_in_root_dir


print(find_files(arg.root_dir))

# files = find_files(arg.root_dir, arg.type_file)
'''

znachenie = []
# Читаем содержимое файлов
for i in range(len(files)):

    file = open(files[i])
    znachenie.append(file.read())
    #print(f'{files[i]} --- {file.read()}')

print(znachenie)

'''



'''
    all_files_in_root_dir = os.listdir(f'{path}')
    print(all_files_in_root_dir)

    for i in range(len(all_files_in_root_dir)):
        try:
            files = os.listdir(f'{path}/{all_files_in_root_dir[i]}')
            print(files)
        except:
            logging.warning(f'{path}/{all_files_in_root_dir[i]} - не является директорией')
'''





'''
file_antenna = open(f'/sys/class/net/{interface}/device/antenna_tx', 'w')
file_antenna.write(str(antenna_tx))
file_antenna.close()

os.popen(f'sudo chown -R {os.getlogin()}:{os.getlogin()} {path}')

'''



'''
try:
    sch_dir = 0
    files = os.listdir(f'{path}/{check_root_dir[i]}')
    logging.info(f'{path}/{check_root_dir[i]} - является директорией')
    for j in range(len(files)):
        file_d = f'{path}/{check_root_dir[i]}/{files[j]}'
        logging.info(f'{file_d} - найден файл')

        if file_d[-4::] == rash:
            if file_d not in all_files_in_root_dir:
                logging.info(f'{path}/{check_root_dir[i]}/{file_d} - добавляется в переменную найденных файлов')
                all_files_in_root_dir = all_files_in_root_dir + [file_d]
                sch_dir = 1
'''




logging.info('Скрипт выполнен')


