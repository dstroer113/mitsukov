import tkinter as tk


def get_th(num):
    if num > 999:
        th_place = int(str(num)[-4])
        return th_place
    else:
        return None


def on_button_click():
    num = int(entry.get())
    th_digits = get_th(num)
    if th_digits is not None:
        label.config(text=f"Цифра в разряде тысяч: {th_digits}")
    else:
        label.config(text="Число меньше 1000")


root = tk.Tk()
root.title("Цифра в разряде тысяч")
root.geometry("300x150")

label = tk.Label(root, text="Введите число больше 999:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Показать цифру", command=on_button_click)
button.pack(pady=5)

root.mainloop()
