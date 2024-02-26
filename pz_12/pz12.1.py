"""
В последовательности на и целых элементов в последней ее половине найти сумму элементов.
"""
import functools
import random
numbers = [random.randint(-100, 100) for i in range(int(input('Введите число n:')))]
print('Последовательность:', numbers)

scnd_part = numbers[len(numbers)//2:len(numbers)]
print('Сумма второй половины последовательности:', functools.reduce(lambda a, b: a + b, scnd_part))
