"""
Создайте класс "Фигура", который содержит метод расчета площади фигуры.
Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса
"Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.
"""

class Figure:
    def __init__(self, dlina, shirina):
        self.dlina = dlina
        self.shirina = shirina


class Square(Figure):
    def __init__(self, dlina):
        self.dlina = dlina
    def ploshad(self):
        plosh = self.dlina * self.dlina
        print('Площадь квадрата:', plosh)


class Rectangle(Figure):
    def ploshad(self):
        x = self.dlina * self.shirina
        print('Площадь прямоугольника:', x)


rectangle1 = Rectangle(10, 5)
rectangle1.ploshad()
square1 = Square(7)
square1.ploshad()

