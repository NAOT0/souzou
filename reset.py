import tkinter
import openpyxl


def reset():
    root = tkinter.Tk()
    root.geometry("320x240")
    root.title('リセット')
    label = tkinter.Label(root, text='登録されている商品を消去しますか？\n削除した場合アプリを再起動してください', font=("", 10))

    def click():
        with open("today_kcal.txt", "w", encoding="utf_8") as g:
            g.write("")
        with open("ALL_kcal.txt", "w", encoding="utf_8") as g:
            g.write("")
        wb = openpyxl.load_workbook('jan_time.xlsx')
        ws = wb['Sheet1']

        for row in ws:
            for cell in row:
                cell.value = None

        wb.save("jan_time.xlsx")

        root.destroy()

    def quit():
        root.destroy()

    button_yes = tkinter.Button(root, text="はい", command=click)
    button_no = tkinter.Button(root, text="いいえ", command=quit)
    label.pack()
    button_yes.pack()
    button_no.pack()
