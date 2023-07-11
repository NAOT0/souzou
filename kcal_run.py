import tkinter


def kcal_run():
    today = 0
    with open('ALL_kcal.txt', 'r') as f:
        all_kcal = f.read().split("\n")
        all_kcal = list(filter(lambda x: x != "", all_kcal))

        all_kcal = [int(s, 0) for s in all_kcal]

    with open('today_kcal.txt', 'r') as f:
        today_kcal = f.read().split("\n")
        today_kcal = list(filter(lambda x: x != "", today_kcal))

        today_kcal = [int(s, 0) for s in today_kcal]

    all = today_kcal[0]
    "今日の総カロリー"
    for i in range(len(all_kcal)):
        today = all_kcal[i]+today
    "残り接種可能カロリー計算"
    for i in range(len(all_kcal)):
        all = all-all_kcal[i]

    root = tkinter.Tk()
    root.geometry("320x240")
    root.title('本日の摂取カロリー')
    labelx = tkinter.Label(root, text='', font=("", 20))
    labelx.pack()
    label = tkinter.Label(root, text='今日摂取したカロリーは'+str(today)+"kcalです", font=("", 10))
    label.pack()
    labelx = tkinter.Label(root, text='', font=("", 20))
    labelx.pack()
    label2 = tkinter.Label(root, text='あなたの年齢・性別をもとに考えると', font=("", 10))
    label2.pack()
    label3 = tkinter.Label(root, text='本日の取得可能カロリーは'+str(all)+"kcalです", font=("", 10))
    label3.pack()
    root.mainloop()
