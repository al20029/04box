"""
*******************************************************************
***  File Name      : DisplayOngoingWindow.py
***  Version        : V1.0
***  Designer       : 
***  Date           : 2022.6.14
***  Purpose       	: 
***
*******************************************************************/
"""

from re import I
import tkinter
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from UpdateGraph import UpdateGraph
from MainMeasurement import MainMeasurement
from ManagementDownload import ManagementDownload
import time
i = 1
y = []
count = 0
color_list = ["r", "b", "g", "y", "m", "c", "k"]
class DisplayOngoingWindow:
    def OngoingWindow(Data):
        # click時のイベント
        def btn_click():
            nonlocal RUN
            RUN = True
            tki.destroy()
            
        RUN = False

        # 画面作成
        tki = tkinter.Tk()       
        w = tki.winfo_screenwidth() - 515
        h = tki.winfo_screenheight() - 430
        tki.geometry('500x350+'+str(w)+"+"+str(h)) # 画面サイズの設定
        tki.title('計測中画面') # 画面タイトルの設定
        fig = plt.Figure() # 描画の用意
        global y
        global i
        global count
        global color_list
        count = 0
        i = 1
        y = []
        
        ax = fig.add_subplot(111)
        ax.set_ylabel("speed / Mbps")#y軸のラベル
        ax.set_ylim(0, 10)
        ax.set_xlabel("x / mm")#x軸のラベル
        if Data.color == '':
            Data.color = color_list.pop(0)
            color_list.append(Data.color)

        #題名表示
        SystemName = tkinter.Label(text="速度計測中", font=("MSゴシック", "30", "bold"))
        SystemName.place(x = 135, y = 10)

        # ボタンの作成
        btn = tkinter.Button(tki, text = '計測中止', width = 10, height = 2, command = btn_click, font = ("MSゴシック", "10"))
        btn.place(x = 370, y = 300) #ボタンを配置する位置の設定

        #空ダウンロード
        ManagementDownload.Donwload()
        
        #1回目の計測
        if MainMeasurement.Measurement(Data) == -1:
            messagebox.showerror('エラー', 'Wi-Fiの変更に失敗しました。')
            tki.destroy()
            return False

        x = np.arange(0, i, 1, dtype = int) #x軸のデータ
        y = np.append(y, Data.ListInstantSpeed[i-1])

        ax.plot(x, y, color = Data.color) #データの描画

        print(x)
        canvas = FigureCanvasTkAgg(fig, master = tki)
        canvas.draw()
        canvas.get_tk_widget().place(x = 10, y = 62, width = 480, height = 230)
        
        def repeat_func():
            global count
            global i
            global y
            count += 1
            i += 1
            #定期的に行いたい処理
            if count < 10:
                
                # 追加

                if MainMeasurement.Measurement(Data) == -1:
                    messagebox.showerror('エラー', 'Wi-Fiの接続が切れました。')
                    tki.destroy()
                    return False
                
                fig = plt.Figure() #描画の用意
                
                x = np.arange(0, i, 1)
                y = np.append(y, Data.ListInstantSpeed[i-1])
                ax = fig.add_subplot(111)
                ax.set_ylabel("speed / Mbps")#y軸のラベル
                ax.set_ylim(0, Data.MaxSpeed*1.1)
                ax.set_xlabel("x / mm")#x軸のラベル
                ax.plot(x, y, color = Data.color) #データの描画
                canvas = FigureCanvasTkAgg(fig, master=tki)
                canvas.draw()
                canvas.get_tk_widget().place(x=10, y=62, width=480, height=230)
                print(count)
                print(x)
                print(y)
            
                tki.after(1000, repeat_func)
            else:
                time.sleep(2)
                tki.destroy()
                nonlocal RUN
                RUN = True
        tki.after(1000, repeat_func)
        tki.mainloop()
        return RUN