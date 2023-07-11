import tkinter
import openpyxl
from pykakasi import kakasi
import pandas as pd
import yhoo


def kcal():
    root = tkinter.Tk()
    root.geometry("320x240")
    root.title('商品取り出し')
    label = tkinter.Label(root, text='何グラムか入力してください', font=("", 10))
    label.pack()
    entry1 = tkinter.Entry(root)
    entry1.pack()
    button = tkinter.Button(root, text="OK")
    button.pack()

    def click():
        g = int(entry1.get())
        g = g/100
        jancode_management = int(entry1.get())

        df = pd.read_excel('eiyouso2.xlsx', sheet_name=0)
        list = []
        B = []
        for row in df.values:
            list.append(f'{row[0]}')

        A = list
        kaki = kakasi()
        kaki.setMode('J', 'H')
        kaki.setMode("K", "H")
        conv = kaki.getConverter()
        sr = []
        sr.append(yhoo.reaaaad(jancode_management))

        X1 = sr[0]

        X1 = conv.do(X1)
        B.append(X1)

        Wb = openpyxl.load_workbook('eiyouso2.xlsx')
        Sheet_1 = Wb['シート1']

        data = []
        for i in range(len(A)):
            if A[i] in B[0]:
                data.append(Sheet_1["A"+str(i+2)].value)
                data.append(Sheet_1["B"+str(i+2)].value)

        Wb.save("eiyouso2.xlsx")
        all = data[1]
        all_kcal = all*g
        print(all_kcal)

    button["command"] = click
    root.mainloop()
