"""
Из списка: [Валентин', Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия"]
получить новый список, в котором длина слов не превышает 5 символов.

"""
names = ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин', 'Валерия', 'Юлия']
print()
i = 0
new_names = []
while i < len(names):
    if len(names[i]) < 5:
        new_names += [names[i]]
    else:
        new_names += [names[i][0:5]]
    i += 1
print('Новый список:', new_names)
