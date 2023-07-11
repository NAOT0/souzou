import tkinter as tk
import openpyxl


def first_question():
    def btn_click():
        name = str(txt_n.get())
        age = int(txt_a.get())
        sex = int(txt_s.get())
        if (age >= 15 and age <= 17 and sex == 1):
            cal = 2850

        elif (age >= 15 and age <= 17 and sex == 2):
            cal = 2300

        elif (age >= 18 and age <= 29 and sex == 1):
            cal = 2650

        elif (age >= 18 and age <= 29 and sex == 2):
            cal = 1950

        elif (age >= 30 and age <= 49 and sex == 1):
            cal = 2650

        elif (age >= 30 and age <= 49 and sex == 2):
            cal = 2000

        elif (age >= 50 and age <= 69 and sex == 1):
            cal = 2450

        elif (age >= 50 and age <= 69 and sex == 2):
            cal = 1900

        elif (age >= 70 and sex == 1):
            cal = 2200

        elif (age >= 70 and sex == 2):
            cal = 1750

        txt_c.insert(0, (cal))
        book = openpyxl.load_workbook("user_data.xlsx")

        book_row = book['Sheet1'].max_row
        print(book_row)
        book_row = book_row + 1

        namae = "A"+str(book_row)
        nennrei = "B"+str(book_row)
        seibetu = "C"+str(book_row)
        karori = "D"+str(book_row)

        print(book_row)

        sheet = book['Sheet1']
        sheet[namae] = name
        sheet[nennrei] = age
        sheet[seibetu] = sex
        sheet[karori] = cal
        book.save("user_data.xlsx")
        root.destroy()

    root = tk.Tk()

    root.geometry('300x400')

    root.title('初期質問')

    lbl_n = tk.Label(root, text='名前', foreground='White', background='Gray')
    lbl_n.place(x=30, y=50)

    lbl_a = tk.Label(root, text='年齢', foreground='White', background='Gray')
    lbl_a.place(x=30, y=100)

    lbl_x = tk.Label(root, text='(1:男2:女)', foreground='Black')
    lbl_x.place(x=28, y=172)

    lbl_s = tk.Label(root, text='性別', foreground='White', background='Gray')
    lbl_s.place(x=30, y=150)

    lbl_c = tk.Label(root, text='カロリー', foreground='White', background='Gray')
    lbl_c.place(x=30, y=200)

    txt_n = tk.Entry(root, width=25)
    txt_n.place(x=90, y=50)

    txt_a = tk.Entry(root, width=25)
    txt_a.place(x=90, y=100)

    txt_s = tk.Entry(root, width=25)
    txt_s.place(x=90, y=150)

    txt_c = tk.Entry(root, width=25)
    txt_c.place(x=90, y=200)

    btn = tk.Button(root, text='OK', command=btn_click)

    btn.place(x=130, y=300)
    root.mainloop()
