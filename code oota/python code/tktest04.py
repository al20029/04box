# -*- coding:utf-8 -*-
import tkinter

# 秒数をカウントする変数
count = 0

# 定期的に実行する関数
def repeat_func():
    global app
    global label
    global count

    # 定期的に行いたい処理
    count += 1
    label.config(
        text=str(count)
    )

    # 再度repeat_funcが実行されるようにafter実行
    app.after(1000, repeat_func)

# メインウィンドウの作成
app = tkinter.Tk()
app.geometry("300x200")

# ラベルウィジェット作成
label = tkinter.Label(
    app,
    width=15,
    height=1,
    text="0",
    font=("", 50)
)
label.pack()

# 1000ms後にrepeat_func関数を実行
app.after(1000, repeat_func)

# メインループ
app.mainloop()