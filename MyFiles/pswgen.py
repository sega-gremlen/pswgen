import string
import random
from tkinter import *
import pyperclip
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def generate_random_password():
    passwords = []

    if symbol_cb.get() == 1:
        characters = list(string.ascii_letters + string.digits + '%*)?@#$~')

        while len(passwords) != 10:
            random.shuffle(characters)
            psw = characters[:10]
            flag1, flag2, flag3, flag4, count = False, False, False, False, 0

            for i in psw:
                if i.isdigit():
                    count += 1
                    if count == 2:
                        flag1 = True
                if i.isupper():
                    flag2 = True
                if i.islower():
                    flag3 = True
                if i in '%*)?@#$~':
                    flag4 = True

            if flag1 and flag2 and flag3 and flag4:
                passwords.append(''.join(psw))

    else:
        characters = list(string.ascii_letters + string.digits)

        while len(passwords) != 10:
            random.shuffle(characters)
            psw = characters[:10]
            flag1, flag2, flag3, count = False, False, False, 0

            for i in psw:
                if i.isdigit():
                    count += 1
                    if count == 2:
                        flag1 = True
                if i.isupper():
                    flag2 = True
                if i.islower():
                    flag3 = True

            if flag1 and flag2 and flag3:
                passwords.append(''.join(psw))

    return passwords


def clear_passwords(*args):
    for i in args:
        i['text'] = ''


def make_psw_form(win):
    global click_count
    click_count += 1
    win.geometry('200x453')
    passwords = generate_random_password()
    global psw_0, psw_1, psw_2, psw_3, psw_4, psw_5, psw_6, psw_7, psw_8, psw_9

    if click_count > 1:
        clear_passwords(psw_0, psw_1, psw_2, psw_3, psw_4, psw_5, psw_6, psw_7, psw_8, psw_9)

    psw_0 = Label(win, text='', font=('Times', 15))
    psw_0 = Label(win, text=passwords[0], font=('Times', 15))
    psw_0.grid(row=2, sticky=W, pady=5, padx=5)
    copy_button_0 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[0]),
                           highlightthickness=0, bd=0)
    copy_button_0.grid(row=2, sticky=E, pady=5, padx=20)

    psw_1 = Label(win, text=passwords[1], font=('Times', 15))
    psw_1.grid(row=3, sticky=W, pady=5, padx=5)
    copy_button_1 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[1]),
                           highlightthickness=0, bd=0)
    copy_button_1.grid(row=3, sticky=E, pady=5, padx=20)

    psw_2 = Label(win, text=passwords[2], font=('Times', 15))
    psw_2.grid(row=4, sticky=W, pady=5, padx=5)
    copy_button_2 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[2]),
                           highlightthickness=0, bd=0)
    copy_button_2.grid(row=4, sticky=E, pady=5, padx=20)

    psw_3 = Label(win, text=passwords[3], font=('Times', 15))
    psw_3.grid(row=5, sticky=W, pady=5, padx=5)
    copy_button_3 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[3]),
                           highlightthickness=0, bd=0)
    copy_button_3.grid(row=5, sticky=E, pady=5, padx=20)

    psw_4 = Label(win, text=passwords[4], font=('Times', 15))
    psw_4.grid(row=6, sticky=W, pady=5, padx=5)
    copy_button_4 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[4]),
                           highlightthickness=0, bd=0)
    copy_button_4.grid(row=6, sticky=E, pady=5, padx=20)

    psw_5 = Label(win, text=passwords[5], font=('Times', 15))
    psw_5.grid(row=7, sticky=W, pady=5, padx=5)
    copy_button_5 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[5]),
                           highlightthickness=0, bd=0)
    copy_button_5.grid(row=7, sticky=E, pady=5, padx=20)

    psw_6 = Label(win, text=passwords[6], font=('Times', 15))
    psw_6.grid(row=8, sticky=W, pady=5, padx=5)
    copy_button_6 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[6]),
                           highlightthickness=0, bd=0)
    copy_button_6.grid(row=8, sticky=E, pady=5, padx=20)

    psw_7 = Label(win, text=passwords[7], font=('Times', 15))
    psw_7.grid(row=9, sticky=W, pady=5, padx=5)
    copy_button_7 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[7]),
                           highlightthickness=0, bd=0)
    copy_button_7.grid(row=9, sticky=E, pady=5, padx=20)

    psw_8 = Label(win, text=passwords[8], font=('Times', 15))
    psw_8.grid(row=10, sticky=W, pady=5, padx=5)
    copy_button_8 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[8]),
                           highlightthickness=0, bd=0)
    copy_button_8.grid(row=10, sticky=E, pady=5, padx=20)

    psw_9 = Label(win, text=passwords[9], font=('Times', 15))
    psw_9.grid(row=11, sticky=W, pady=5, padx=5)
    copy_button_9 = Button(win, image=copy_img, command=lambda: pyperclip.copy(passwords[9]),
                           highlightthickness=0, bd=0)
    copy_button_9.grid(row=11, sticky=E, pady=5, padx=20)


# Настройки окна
win = Tk()
photo = PhotoImage(file=resource_path('window_icon.png'))
win.iconphoto(False, photo)
win.title('PSW GEN')
win.geometry('200x77')
win.resizable(False, False)

win.columnconfigure(0, weight=20)

# Надписи
c_label = Label(win, text='Спец. символы % * ) ?@ # $ ~', font=('Times', 10))
c_label.grid(column=0, row=0, sticky=W, pady=5, padx=5)

# Флажок
symbol_cb = IntVar()
Checkbutton(win, onvalue=1, offvalue=0, variable=symbol_cb).grid(column=0, row=0, sticky=E, pady=5)

# Кнопки
copy_img = PhotoImage(file=resource_path('copy_button.png'))
button = Button(win, font=('Times', 15), width=190, command=lambda: make_psw_form(win), text='▼ Создать пароли ▼')
button.grid(row=1)
click_count = 0

# Запуск
win.mainloop()
