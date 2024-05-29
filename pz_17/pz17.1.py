from tkinter import *
from tkinter.ttk import Notebook
from tkinter import messagebox


def submit_form():
    messagebox.showinfo("Information", f"Регистрация прошла успешно!")


def cancel_form():
    messagebox.showwarning("Warning", "Вы отменили регистрацию!")


def add_placeholder(event):
    if text_widget.get("1.0", END) == "\n":
        text_widget.insert("1.0", placeholder)
        text_widget.config(fg='grey')


def clear_placeholder(event):
    if text_widget.get("1.0", END) == placeholder + "\n":
        text_widget.delete("1.0", END)
        text_widget.config(fg='black')


root = Tk()
root.title("Обработка формы - Mozilla Firefox")
root["bg"] = 'white'
root.geometry("650x750")

frame_config = Notebook(root)

frame1 = Frame(root, bg='white')
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root, bg='white')
frame3.pack()

label_frame2 = Label(frame2, text="\nФорма регистрации пользователя", font=('Times New Roman bold', 15))
label_frame2.pack()

frame_form = Frame(frame2, borderwidth=2, relief=GROOVE)
frame_form.pack()

label_name = Label(frame_form, text="Ваше имя:", font=('Arial bold', 12))
label_name.grid(row=0, column=0, padx=5, pady=10)
entry_name = Entry(frame_form, bg='#dbdbdb', width=42)
entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=3)
label_password = Label(frame_form, text="Пароль:", font=('Arial bold', 12))
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = Entry(frame_form, show='*', bg='#dbdbdb', width=42)
entry_password.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

label_age = Label(frame_form, text="Возраст:", font=('Arial bold', 12))
label_age.grid(row=2, column=0, padx=10, pady=10)
entry_age = Entry(frame_form, bg='#dbdbdb', width=42)
entry_age.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

label_pol = Label(frame_form, text="Пол:", font=('Arial bold', 12))
label_pol.grid(row=3, column=0, padx=10, pady=10)
gender_var = StringVar(value="men")
radio_men = Radiobutton(frame_form, text="Мужской", variable=gender_var, value="men")
radio_men.grid(row=3, column=1, padx=10, pady=5, sticky='e')
radio_girl = Radiobutton(frame_form, text="Женский", variable=gender_var, value="girl")
radio_girl.grid(row=3, column=3, padx=10, pady=5, sticky='w')

label_hobbies = Label(frame_form, text="Ваши увлечения:", font=('Arial bold', 12))
label_hobbies.grid(row=4, column=0, padx=10, pady=10)

checkbox_muzika = Checkbutton(frame_form, text="Музыка")
checkbox_muzika.grid(row=4, column=1, padx=10, pady=5, sticky='e')
checkbox_video = Checkbutton(frame_form, text="Видео")
checkbox_video.grid(row=4, column=2, padx=10, pady=5)
checkbox_risovanie = Checkbutton(frame_form, text="Рисование")
checkbox_risovanie.grid(row=4, column=3, padx=10, pady=5, sticky='w')

label_strana = Label(frame_form, text="Ваша страна:", font=('Arial bold', 12))
label_strana.grid(row=5, column=0, padx=10, pady=10)
country_var1 = StringVar(value="Выбрать страну")
option_menu1 = OptionMenu(frame_form, country_var1, "Россия", "Италия", "Франция", "Казахстан", "Азербайджан")
option_menu1.grid(row=5, column=1, padx=10, pady=5, columnspan=3)

label_city = Label(frame_form, text="Ваш город:", font=('Arial bold', 12))
label_city.grid(row=6, column=0, padx=10, pady=10)
country_var2 = StringVar(value="Выбрать город")
option_menu2 = OptionMenu(
    frame_form,
    country_var2,
    "Ростов-на-Дону", "Рим",
    "Париж", "Астана",
    "Баку"
)
option_menu2.grid(row=6, column=1, padx=10, pady=5, columnspan=3)

label_0_sebe = Label(frame_form, text="Кратко о себе:", font=('Arial bold', 12))
label_0_sebe.grid(row=7, column=0, padx=10, pady=10)
placeholder = "Краткая информация\n  о ваших увлечениях..."
text_widget = Text(frame_form, height=5, width=30)
text_widget.grid(row=8, column=1, padx=10, pady=5, sticky='w', columnspan=3)
text_widget.insert("1.0", placeholder)
text_widget.config(fg='grey')
text_widget.bind("<FocusIn>", clear_placeholder)
text_widget.bind("<FocusOut>", add_placeholder)

label_primer = Label(frame_form, text="Решите пример, запишите результат в поле ниже:", font=('Arial bold', 12))
label_primer.grid(row=10, column=0, padx=10, pady=10, columnspan=3)
entry_primer = Entry(frame_form, bg='#dbdbdb', width=42)
entry_primer.grid(row=11, column=1, padx=10, pady=10, columnspan=3)

btn1 = Button(frame_form, text="Отменить ввод", command=cancel_form)
btn1.grid(row=12, column=1, padx=10, pady=10)

btn2 = Button(frame_form, text="Данные подтверждаю", command=submit_form)
btn2.grid(row=12, column=2, padx=10, pady=10)


frame_config.add(frame1, text="Firefox ᐯ")
frame_config.add(frame2, text="⸬ Обработка формы")
frame_config.add(frame3, text="➕")
frame_config.pack(expand=1, fill='both')

root.mainloop()
