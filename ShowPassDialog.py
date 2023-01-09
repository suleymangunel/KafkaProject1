import tkinter as tk
from tkinter import *


def main():
    window = tk.Tk()

    def button_click():
        window.destroy()

    def close_win(event):
        button_click()

    window.title('Amazon Login Password')
    window.geometry('200x80')
    b1 = Button(window, text="Tamam", font=('Helvetica bold', 10), command=button_click, width=20)
    b1.pack(side=BOTTOM, pady=5)
    l1 = Label(window, text="Parola: ")
    l1.pack(side=LEFT, anchor=NW, padx=10, pady=10)
    _password = StringVar()
    e1 = tk.Entry(window, show='*', font=('Arial', 14), bd=1, textvariable=_password)
    e1.focus_set()
    e1.pack(side=RIGHT, anchor=NE, padx=10, pady=10)
    window.bind('<Return>', close_win)
    window.mainloop()
    return _password.get()
