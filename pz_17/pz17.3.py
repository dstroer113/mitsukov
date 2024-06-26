"""
Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
оформленный согласно требованиям. Все задания выполняются c использованием модуля
OS:
     перейдите в каталог PZ11. Выведите список всех файлов в этом каталоге. Имена
вложенных подкаталогов выводить не нужно.
     перейти в корень проекта, создать папку с именем test. В ней создать еще одну папку
test1. В папку test переместить два файла из ПЗ6, а в папку test1 - один файл из ПЗ7.
Файл из ПЗ7 переименовать в test.txt. Вывести в консоль информацию о размере
файлов в папке test.
     перейти в папку с PZ11, найти там файл с самым коротким именем, имя вывести в
консоль. Использовать функцию basename () (os.path.basename()).
     перейти в любую папку где есть отчет в формате .pdf и «запустите» файл в
привязанной к нему программе. Использовать функцию os.startfile().
     удалить файл test.txt.
"""
import os
import subprocess
import random

# 1
os.chdir('../pz_11')

files = [f for f in os.listdir() if os.path.isfile(f)]
print("Список файлов в каталоге pz_11:", files)

# 2
os.chdir('..')

os.makedirs('test/test1', exist_ok=True)

os.rename('pz_6/pz6.1.py', 'test/pz6.1.py')
os.rename('pz_6/pz6.2.py', 'test/pz6.2.py')

os.rename('pz_7/pz7.1.py', 'test/test1/test.txt')

test_files = [f for f in os.listdir('test') if os.path.isfile(os.path.join('test', f))]
for file in test_files:
    size = os.path.getsize(os.path.join('test', file))
    print(f"Размер файла {file}: {size} байт")

# 3
os.chdir('pz_11')

shortest_name = min([f for f in os.listdir() if os.path.isfile(f)], key=len)
print("Файл с самым коротким именем:", os.path.basename(shortest_name))

# 4
os.chdir('../reports')

pdf_file = [file for file in os.listdir() if file.endswith('.pdf')]
path = pdf_file[random.randint(0, len(pdf_file)-1)]

p = subprocess.Popen([path])

# 5
os.chdir('../test/test1')

os.remove('test.txt')
print("Файл test.txt был удален")
