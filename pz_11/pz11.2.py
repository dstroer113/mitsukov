# Из предложенного текстового файла (text18-23.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках.
# Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно заменив символы верхнего регистра на нижний.
import string
# Открытие и чтение содержимого из файла
with open('text18-23.txt', 'r', encoding='UTF-16') as file:
    content = file.read()

# Вывод содержимого файла
print("Содержимое файла:")
print(content)

# Подсчет знаков пунктуации в первых четырех строках
punctuation_count = 0
lines = content.split('\n')[:4]
for line in lines:
    for char in line:
        if char in string.punctuation:
            punctuation_count += 1

print("Количество знаков пунктуации в первых четырёх строках:", punctuation_count)

# Замена символов верхнего регистра на нижний и запись в новый файл
new_content = content.lower()

with open('new_text.txt', 'w') as new_file:
    new_file.write(new_content)

print("Текст успешно записан в файл 'new_text.txt'")
