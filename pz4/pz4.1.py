n,k=input('Конечное число '),input('Cтепень ')
while type(n) !=int:
    try:
        n=int(n)
    except ValueError:
        print("Неправильно ввели!")
        a=input("Введите число: ")
while type(k) !=int:
    try:
        k=int(k)
    except ValueError:
        print("Неправильно ввели!")
        a=input("Введите число: ")
res=0
for i in range(1,n+1):
    res=res+i**k
print(res)