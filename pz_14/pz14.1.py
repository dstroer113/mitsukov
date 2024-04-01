"""
Из исходного текстового файла из раздела "зарезервированные адреса"
перенести в первый файл строки с ненулевыми первыми и вторыми октетами,
а во второй все остальные. посчитать количество строк в каждом файле
"""

import re

file_path = 'pz_14/ip_adress.txt'

section_name = 'Зарезервированные адреса'

with open(file_path, 'r') as file:
    content = file.read()

start_index = content.find(section_name) + len(section_name)
end_index = len(content)

section_content = content[start_index:end_index]

pattern = re.compile(r'\b(?:25[1-5]|2[1-4][1-9]|[01]?[1-9][1-9]?)\.(?:25[1-5]|2[1-4][1-9]|[01]?[1-9][1-9]?)\.\d+\.\d+\b')

pattern2 = re.compile(r'\b(?:25[0-9]|2[0-4][0-4]|[01]?[0-9][0-9]?)\.(?:25[0-1]|2[0-1][0-1]|[01]?[0-1][0-1]?)\.\d+\.\d+\b')

nice = pattern.findall(section_content)
bad = pattern2.findall(section_content)

with open('without_zero.txt', 'w') as first:
    first.writelines(f"{item}\n" for item in nice)

with open('other.txt', 'w') as second:
    second.writelines(f"{item}\n" for item in bad)

with open('without_zero.txt', 'r') as first, open('other.txt', 'r') as second:
    firstlines = first.readlines()
    secondlines = second.readlines()

print("Количество строк в without_zero.txt:", len(firstlines))
print("Количество строк в other.txt:", len(secondlines))
