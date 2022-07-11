"""
******************************************************
*** File Name       : DisplayRegularFinishWindow.py
*** Version         : V1.0
*** Designer        : 佐藤 光
*** Date            : 2022/06/14
*** Purpose         : 定期計測終了画面を表示し、ユーザの入力を受け取る
*** 
******************************************************
"""

import tkinter
from tkinter import messagebox
from InteractWithOS import InteractWithOS

class DisplayRegularFinishWindow:

    """
    *******************************************************************
    ***  Function Name  : RegularFinishWindow
    ***  Version        : V1.0
    ***  Designer       : 
    ***  Date           : 2022.6.21
    ***  Purpose       	: 
    ***
    *******************************************************************/
    """

    def RegularFinishWindow(BestWiFiName):
        # click時のイベント
        def btn_click():
            # messagebox.askyesno("wi-fi変更中", "停止しますか")
            InteractWithOS.ChangeWiFi(BestWiFiName)
            messagebox.showinfo("メッセージ", "Wi-Fi変更を終了しました")
            # tki.quit()
            tki.destroy()

        # 画面作成
        tki = tkinter.Tk()
        h = tki.winfo_screenheight() - 370
        w = tki.winfo_screenwidth() - 405
        tki.geometry('400x300+'+str(w)+"+"+str(h)) # 画面サイズの設定
        tki.title('定期計測終了画面') # 画面タイトルの設定

        #題名表示
        SystemName = tkinter.Label(text="計測終了", font=("MSゴシック", "30", "bold"))
        SystemName.place(x=110, y=10)

        #メッセージ表示
        SystemName = tkinter.Label(text = "最も最適なWi-Fiは", font = ("MSゴシック", "20"))
        SystemName.place(x = 70, y = 80)
        SystemName = tkinter.Label(text = "です", font = ("MSゴシック", "20"))
        SystemName.place(x = 70, y = 190)

        #最適なWi-Fi名の表示
        msg = BestWiFiName
        SystemName = tkinter.Label(text = msg, font = ("MSゴシック", "30"))
        SystemName.place(x = 110, y = 130)
        SystemName.pack(anchor = 'center',expand = 1)

        # ボタンの作成
        btn = tkinter.Button(tki, text = 'Wi-Fi変更', width = 10, height = 2, command = btn_click, font = ("MSゴシック", "10"))
        btn.place(x = 280, y = 250) #ボタンを配置する位置の設定

        # 画面をそのまま表示
        tki.mainloop()