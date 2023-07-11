import tkinter as tk
import tkinter.ttk as ttk
import gui
import take_out
import reset
import expiry_date
import kcal_run


def home():
    root = tk.Tk()
    root.title("栄養管理アプリ")
    root.geometry("800x600")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, pady=20)
    with open('user.txt', 'r') as f:
        user = f.read().split("\n")
        user = list(filter(lambda x: x != "", user))
        user = user[0]
    label1_frame = ttk.Label(frame, text="《ホーム画面》", font=("Tahoma", 30))
    label1_frame2 = ttk.Label(frame, text="健康管理を頑張ろう"+user+"さん", font=("", 20))
    button_first = ttk.Button(frame, text="カロリー計算", command=kcal_run.kcal_run)
    button_change = ttk.Button(frame, text="商品入力", command=gui.ioi)
    button_take_out = ttk.Button(frame, text="商品取り出し", command=take_out.take_out)
    button_name = ttk.Button(frame, text="商品名", command=expiry_date.confirm)
    button_reset = ttk.Button(frame, text="リセット", command=reset.reset)

    label1_frame.pack()
    label1_frame2.pack()
    button_first.pack()
    button_change.pack()
    button_take_out.pack()
    button_name.pack()
    button_reset.pack()

    root.mainloop()
