import datetime
import xlrd
import tkinter as tk
import tkinter.ttk as ttk
import yhoo


dt_now = datetime.datetime.now()
now_month = dt_now.month
now_day = dt_now.day


def confirm():
    root = tk.Tk()
    root.geometry("800x600")
    root.title('経過時間の確認')
    tree = ttk.Treeview(root, columns=(1, 2, 3), show='headings')

    tree.column(1, width=165, anchor='center')
    tree.column(2, width=150, anchor='center')
    tree.column(3, width=100, anchor='center')

    tree.heading(1, text='商品名')
    tree.heading(2, text='~7月~入れた日(日)')
    tree.heading(3, text='経過日数(日)')
    tree.pack()
    Wb = xlrd.open_workbook("jan_time.xlsx")
    Sheet_1 = Wb.sheet_by_name('Sheet1')
    Sheet_Max = Sheet_1.nrows

    name = []
    in_time = []
    jan_name = []
    lost = []

    for i in range(1, Sheet_Max):
        name.append(int(Sheet_1.cell_value(i, 0)))
        in_time.append(int(Sheet_1.cell_value(i, 1)))

    for x in range(len(name)):
        jan_name.append(yhoo.reaaaad(name[x]))

    for o in range(len(in_time)):
        lost_time = now_day - in_time[o]
        lost.append(lost_time)

    in_time = in_time[::-1]
    lost = lost[::-1]
    jan_name = jan_name[::-1]

    for i in range(0, len(jan_name)):
        tree.insert('', '0', values=(jan_name[i], in_time[i], lost[i]))

    root.mainloop()
