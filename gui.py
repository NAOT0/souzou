import tkinter
import yhoo
import datetime
import openpyxl


def ioi():
    root = tkinter.Tk()
    root.geometry("320x240")
    root.title('商品入力')
    label = tkinter.Label(root, text='<バーコード入力をしてください>', font=("", 10))
    label1 = tkinter.Label(root, text='一度に3個入力できます', font=("", 10))
    label.pack()
    label1.pack()
    entry1 = tkinter.Entry(root)
    entry1.pack()

    entry2 = tkinter.Entry(root)
    entry2.pack()

    entry3 = tkinter.Entry(root)
    entry3.pack()

    button = tkinter.Button(root, text="OK")
    button.pack()

    def on_key1(event):
        entry2.focus_set()

    def on_key2(event):
        entry3.focus_set()

    def on_key3(event):
        button.focus_set()

    entry1.bind("<Key-Return>", on_key1)
    entry2.bind("<Key-Return>", on_key2)
    entry3.bind("<Key-Return>", on_key3)

    def click():
        a.append(int(entry1.get()))
        a.append(int(entry2.get()))
        a.append(int(entry3.get()))
        in_code1 = str(entry1.get())
        in_code2 = str(entry2.get())
        in_code3 = str(entry3.get())

        jan = a
        jancode_management = a
        jancode_management = str(jancode_management)
        re = []

        for x in range(len(jan)):
            re.append(yhoo.reaaaad(jan[x]))
        re = str(re)
        # 商品名test.txt

        dt_now = datetime.datetime.now()
        now_day = dt_now.day

        book = openpyxl.load_workbook('jan_time.xlsx')
        "最大行の取得"
        book_row = book['Sheet1'].max_row

        book_row = book_row + 1
        book_row2 = book_row+1
        book_row3 = book_row2+1

        x = "A"+str(book_row)
        x2 = "A"+str(book_row2)
        x3 = "A"+str(book_row3)

        y = "B"+str(book_row)
        y2 = "B"+str(book_row2)
        y3 = "B"+str(book_row3)

        sheet = book['Sheet1']
        sheet[x] = int(in_code1)
        sheet[x2] = int(in_code2)
        sheet[x3] = int(in_code3)
        sheet[y] = now_day
        sheet[y2] = now_day
        sheet[y3] = now_day

        book.save("jan_time.xlsx")

        entry1.delete(0, tkinter.END)
        entry2.delete(0, tkinter.END)
        entry3.delete(0, tkinter.END)

    a = []
    button["command"] = click
    root.mainloop()
