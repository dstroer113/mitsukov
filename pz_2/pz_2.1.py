#Разработать программу, выводящую цифру соответствующую разряду тысяч в записи данного числа ,
#большего 999 , и использующую одну операцию деления и одну операцию взятия остатка от деления.
#вводится число для обработки
a=int(input('число(больше 999)='))
#обработка исключений
if a>999:
    #работа с числом
    b=1000
    c=a//b
    s=c%10
    print("цифра разряда тысяч=",s)
#обработка исключений
else:
    print('введите число больше 999')
