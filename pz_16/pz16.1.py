"""
Создайте класс "Животное" с атрибутами "имя" и "вид". Напишите метод, который
выводиг информацию о животном в формате "Имя: имя, Вид: вид".
"""


import pickle


class Animal:
    def __init__(self, name="имя", vid="вид"):
        self.name = name
        self.vid = vid

    def out(self):
        name = self.name
        vid = self.vid
        print('Имя:', name)
        print('Вид:', vid)


def save_def(animal, filename):
    with open(filename, 'wb') as file:
        pickle.dump(animal, file)


def load_def(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data.out()


dog1 = Animal('Перун', 'Амстафф')
bird1 = Animal('Сигурд', 'Снегирь')
cat1 = Animal('Локи', 'Персидский')

save_def(bird1, 'sf.bin')

load_def('sf.bin')






