import tkinter
from tkinter.ttk import Notebook


def razrad():
    a = int(input('число(больше 999)='))
    if a > 999:
        b = 1000
        c = a//b
        s = c % 10
        print("цифра разряда тысяч=",s)
    else:
        print('введите число больше 999')


root = tkinter.Tk()
root.title("pz2")
root["bg"] = 'white'
root.geometry("300x200")

frame_config = Notebook(root)

frame1 = tkinter.Frame(root, bg='white')
frame1.pack()

frame_config.add(frame1)

root.mainloop()