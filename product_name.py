import yhoo
import tkinter as tk


def product_name():
    re = []
    with open('jancode_management.txt', 'r') as f:
        name_to_jancode = f.read().split("\n")
        name_to_jancode = list(filter(lambda x: x != "", name_to_jancode))
        name_to_jancode = [int(s, 0) for s in name_to_jancode]

    jan = name_to_jancode
    for x in range(len(jan)):
        re.append(yhoo.reaaaad(jan[x]))

    window = tk.Tk()
    window.geometry('320x240')
    window.title('商品一覧')
    # リストボックスの作成
    label1 = tk.Label(window, text="《商品名》", font=("Tahoma", 20))
    listbox = tk.Listbox(window, height=30, width=50)

    # リストの要素をリストボックスに追加
    for item in re:
        listbox.insert(tk.END, item)

    # リストボックスをウィンドウに配置
    label1.pack()
    listbox.pack()

    # GUIウィンドウのメインループ
    window.mainloop()
