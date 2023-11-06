n=input('chislo')
k=1
while type(n) !=int:
    try:
        n=int(n)
    except ValueError:
        print("Неправильно ввели!")
        n=input("Введите число: ")
while n>=k**2:
    k=k+1
print(k-1)
