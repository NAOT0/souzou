import GUI_l
import GUI_q
import tkinter as tk


def title():
    root1 = tk.Tk()

    root1.geometry('300x400')

    root1.title('ログイン画面')
    btn_n = tk.Button(root1, text='新規登録', command=GUI_q.first_question)

    btn_n.place(x=130, y=100)

    btn_l = tk.Button(root1, text='ログイン', command=GUI_l.login)
    btn_l.place(x=130, y=200)
    root1.mainloop()


title()
