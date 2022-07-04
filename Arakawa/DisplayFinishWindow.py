"""
*******************************************************************
***  File Name      : DisplayFinishWindow.py
***  Version        : V1.0
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.14
***  Purpose       	: 計測終了画面を表示し, ユーザの入力を受け取る.
***
*******************************************************************/
"""

import tkinter
import tkinter.ttk as ttk
import subprocess
import time
from InteractWithOS import InteractWithOS
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from ToolTip import *

class DisplayFinishWindow:
    def FinishWindow(CanConnectWiFiname,DataList):
        # クリック時のイベント
        def btn_click():
            # InteractWithOS.ChangeWiFi(combobox.get())
            
            #WiFi変更が完了するまで待機 
            # Result_change = str()
            # while Result_change == None:
            #     Result_change = subprocess.run('netsh wlan show interface', encoding='utf-8', shell=True)
            time.sleep(1)

            nonlocal Start
            Start = True
            frm.destroy()

        Start = False
        # 画面作成
        frm = tkinter.Tk()
        frm.geometry('800x500') #画面サイズ
        frm.title()

        # 題名表示
        SystemName = tkinter.Label(text="計測終了", font=("MSゴシック", "30", "bold"))
        SystemName.place(x=160, y=10)

        # グラフ表示
        fig = plt.Figure() #描画の用意
       
        ax = fig.add_subplot(111)
        ax.set_ylabel("speed / Mbps")#y軸のラベル
        ax.set_xlabel("x / times")#x軸のラベル
        ymax = 0
        for data in DataList:
            x=np.arange(0,len(data.ListInstantSpeed),1) #x軸のデータ
            y=data.ListInstantSpeed
            if(ymax < data.MaxSpeed):
                ymax = data.MaxSpeed
                ax.set_ylim(0,data.MaxSpeed*1.1)    
            ax.plot(x, y) #データの描画
        canvas = FigureCanvasTkAgg(fig, master=frm)
        canvas.draw()
        canvas.get_tk_widget().place(x=10,y=62,width=660,height=380)

        # Wi-Fi名プルタブ配置
        list = CanConnectWiFiname
        combobox = ttk.Combobox(frm, height=3, width = 30, values = list, state = "readonly")
        combobox.current(0)
        combobox.place(x = 440, y = 455)
        # pulltub = tkinter.Label(text="(Wi-Fi名)", font=("MSゴシック", "13"))
        # pulltub.place(x=170, y=305)

        # ボタンの作成
        btn = tkinter.Button(frm, text='計測開始', width = 10, height = 2, command = btn_click, font=("MSゴシック", "10"))
        btn.place(x=670, y=450) #ボタンを配置する位置の設定

        # 画面をそのまま表示
        frm.mainloop()

        return Start
    # FinishWindow()
