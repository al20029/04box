"""
*******************************************************************
***  File Name      : DisplayFinishWindow.py
***  Version        : V1.1
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.14
***  Purpose       	: 計測終了画面を表示し、ユーザの入力を受け取り、
                      UI 処理部に返す.
*******************************************************************
"""

import tkinter
import tkinter.ttk as ttk
import time
from InteractWithOS import InteractWithOS
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from ToolTip import *
from MainMeasurement import MainMeasurement
from ssh import ssh

"""
*******************************************************************
***  Class Name     : DisplayFinishWindow
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.14
***  Purpose       	: 計測終了画面を表示し、ユーザの入力を受け取り、
                      UI 処理部に返す.
*******************************************************************
"""
class DisplayFinishWindow:

    """
    *******************************************************************
    ***  Function Name  : FinishWindow
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: 計測終了画面を定義する
    ***  Return         : Bool Start  再計測かどうか
                          String WiFiName  再計測するWiFi名
                          list WiFiList  現在接続可能なWiFi名のリスト
    *******************************************************************
    """

    def FinishWindow(CanConnectWiFiname, DataList):
        list = CanConnectWiFiname
        WiFiName = ''
        WiFiList = []
        WiFiList = CanConnectWiFiname
        # リスト更新ボタンクリックのイベント
        def btn_click_list_change():
            nonlocal combobox
            nonlocal list
            list = InteractWithOS.GetWiFi()
            combobox = ttk.Combobox(frm, height = 3, width = 30, values = list, state = "readonly")
            combobox.current(0)
            combobox.place(x = 440, y = 455)
        # クリック時のイベント
        def btn_click():
            InteractWithOS.ChangeWiFi(combobox.get())
            nonlocal WiFiName
            WiFiName = combobox.get()
            #WiFi変更が完了するまで待機 
            time.sleep(3)

            nonlocal Start
            Start = True
            frm.destroy()

        Start = False

        # DBへ計測済みデータを登録

        RegData = DataList[0]
        for data in DataList:
            if(CanConnectWiFiname[0]==data.WiFiName):
                RegData = data
                break
        if len(RegData.ListInstantSpeed) == 10:
            RegAvg = MainMeasurement.AverageSpeedMeasurement(RegData.ListInstantSpeed,len(RegData.ListInstantSpeed))
            RegStab = MainMeasurement.cmpstability(RegData.ListInstantSpeed, len(RegData.ListInstantSpeed))
            ssh.ParamikoReg(CanConnectWiFiname[0], RegAvg, RegStab)

        # 画面作成
        frm = tkinter.Tk()
        w = frm.winfo_screenwidth() - 915
        h = frm.winfo_screenheight() - 580
        frm.geometry('900x500+' +str(w)+"+"+str(h)) # 画面サイズの設定
        frm.title('計測終了画面')

        # 題名表示
        SystemName = tkinter.Label(text="計測終了", font=("MSゴシック", "30", "bold"))
        SystemName.place(x=380, y=10)
        
        # グラフ表示
        fig = plt.Figure() #描画の用意
       
        ax = fig.add_subplot(111)
        ax.set_ylabel("speed / Mbps") #y軸のラベル
        ymax = 0
        for data in DataList:
            x=np.arange(0, len(data.ListInstantSpeed), 1) #x軸のデータ
            y=data.ListInstantSpeed
            if(ymax < data.MaxSpeed):
                ymax = data.MaxSpeed
                ax.set_ylim(0, data.MaxSpeed*1.1)    
            ax.plot(x, y, data.color) #データの描画
        
      
        canvas = FigureCanvasTkAgg(fig, master=frm)
        canvas.draw()
        canvas.get_tk_widget().place(x = 10, y = 62, width = 390, height = 380)

        style = ttk.Style()

        #結果表

        # バグ対応用の関数
        def fixed_map(option):
            return [elm for elm in style.map('Treeview', query_opt=option) if
            elm[:2] != ('!disabled', '!selected')]

        column = ('WiFi名', 'Speed', 'stab0', 'stab1', 'stab2', 'stab3', 'stab4')
        tree = ttk.Treeview(frm, columns=column)

        tree.column('#0', width = 0, stretch = 'no')
        tree.column('WiFi名', anchor ='center', width = 110)
        tree.column('Speed', anchor = 'center', width = 60)
        tree.column('stab0', anchor = 'center', width = 40)
        tree.column('stab1', anchor = 'center', width = 60)
        tree.column('stab2', anchor = 'center', width = 40)
        tree.column('stab3', anchor = 'center', width = 60)
        tree.column('stab4', anchor = 'center', width = 90) 

        tree.heading('WiFi名', text = 'WiFi名', anchor = 'center')
        tree.heading('Speed', text = 'Speed', anchor = 'center')
        tree.heading('stab0', text = 'メール', anchor = 'center')
        tree.heading('stab1', text = 'ネット検索', anchor = 'center')
        tree.heading('stab2', text = 'SNS', anchor = 'center')
        tree.heading('stab3', text = '動画視聴', anchor = 'center')
        tree.heading('stab4', text = 'オンラインゲーム', anchor = 'center')

        
        style.map('Treeview', foreground = fixed_map('foreground'), background = fixed_map('background'))

        tree.tag_configure("r", foreground = 'red')
        tree.tag_configure("b", foreground = 'blue')
        tree.tag_configure("g", foreground = 'green')
        tree.tag_configure("y", foreground = 'yellow')
        tree.tag_configure("m", foreground = 'magenta')
        tree.tag_configure("c", foreground = 'cyan')
        tree.tag_configure("k", foreground = 'black')

        treecount = 0
        for Data in DataList:
            WiFiName = Data.WiFiName
            avgspeed = round(MainMeasurement.AverageSpeedMeasurement(Data.ListInstantSpeed,len(Data.ListInstantSpeed)),1)
            speed = str(avgspeed) +'Mbps'
            if len(Data.ListInstantSpeed) != 10:
                stab =[-1, -1, -1, -1, -1]
            else:
                stab = MainMeasurement.StabilityCalculation(Data.ListInstantSpeed, 10)

            # 過去データの取得
            PastAvg, PastStab = ssh.ParamikoGetPast(WiFiName)
            PastAvg = round(PastAvg, 1)
            PastSpeed = '(' + str(PastAvg) +'Mbps' +')'
            PastWiFiName = '(' + WiFiName + ')'
            PastStab = '(' + str(PastStab) + ')'

            tree.insert(parent='', index ='end', iid = treecount, values = (WiFiName, speed, stab[0], stab[1], stab[2], stab[3], stab[4]), tags = Data.color)
            tree.insert(parent='', index ='end', iid = treecount+1, values = (PastWiFiName, PastSpeed, '-', '-', '-', '-', '-'), tags = Data.color)
            treecount += 2
        tree.place(x=420, y=80)     

        #安定性の説明
        notes = tkinter.Label(text = "※\'メール\'～\'オンラインゲーム\'は用途における安定性の目安\n  1～5の値を取り，値が大きいほど良い\n計測を途中で中止したときは-1の値を取る",font=('MSゴシック','13'))
        notes.place(x = 430, y = 320)

        #過去データの説明
        notes = tkinter.Label(text = "※過去データは(Wi-Fi名)で表現している\n",font=('MSゴシック','13'))
        notes.place(x = 430, y = 380)

        # Wi-Fi名プルタブ配置
        combobox = ttk.Combobox(frm, height = 3, width = 30, values = list, state = "readonly")
        combobox.current(0)
        combobox.place(x = 440, y = 455)

        # ボタンの作成
        btn = tkinter.Button(frm, text='再計測開始', width = 10, height = 2, command = btn_click, font = ("MSゴシック", "10"))
        btn.place(x = 750, y = 450) #ボタンを配置する位置の設定

        # リスト更新ボタン
        btn2 = tkinter.Button(frm, text = '↺',width = 6,height = 1, command = btn_click_list_change, bg = '#808080', font = ('MSゴシック', 10))
        btn2.place(x = 670, y = 455)

        # 画面をそのまま表示
        frm.mainloop()

        WiFiList = list
        return Start, WiFiName, WiFiList