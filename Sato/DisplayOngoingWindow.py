from re import I
import tkinter
# from tkinter import ON, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
#from Data import Data 
from UpdateGraph import UpdateGraph
from MainMeasurement import MainMeasurement
import time
i = 1
y = []
count = 0
class DisplayOngoingWindow:
    def OngoingWindow(Data):
        # click時のイベント
        def btn_click():
            nonlocal Stop
            Stop = True
            #messagebox.showinfo("メッセージ", "ボタンがクリックされました")
            tki.destroy()
            
        # 追加
        MainMeasurement.Measurement(Data)

        Stop = False

        # 画面作成
        tki = tkinter.Tk()
        
        w = tki.winfo_screenwidth() - 515
        h = tki.winfo_screenheight() - 430
        tki.geometry('500x350+'+str(w)+"+"+str(h)) # 画面サイズの設定

        tki.title('計測中') # 画面タイトルの設定
        fig = plt.Figure() #描画の用意
        global y
        global i
        global count
        count = 0
        i = 1
        y = []
        x=np.arange(0,i,1, dtype=int) #x軸のデータ

        
        y=np.append(y,Data.ListInstantSpeed[i-1])

        ax = fig.add_subplot(111)
        ax.set_ylabel("speed / Mbps")#y軸のラベル
        ax.set_ylim(0,10)
        ax.set_xlabel("x / mm")#x軸のラベル
        ax.plot(x, y) #データの描画
        print(x)
        canvas = FigureCanvasTkAgg(fig, master=tki)
        canvas.draw()
        canvas.get_tk_widget().place(x=10,y=62,width=480,height=230)
        #題名表示
        SystemName = tkinter.Label(text="速度計測中", font=("MSゴシック", "30", "bold"))
        SystemName.place(x=135, y=10)


        # ボタンの作成
        btn = tkinter.Button(tki, text='計測中止', width = 10, height = 2, command = btn_click, font=("MSゴシック", "10"))
        btn.place(x=370, y=300) #ボタンを配置する位置の設定

        # 画面をそのまま表示
        #tki.mainloop()
        
        def repeat_func():
            global count
            global label
            global i
            global y
            count+=1
            i+=1
            #定期的に行いたい処理
            if count<10:
                
                # 追加
                MainMeasurement.Measurement(Data)
                
                fig = plt.Figure() #描画の用意
                
                x=np.arange(0,i,1)
                y=np.append(y,Data.ListInstantSpeed[i-1])
                ax = fig.add_subplot(111)
                ax.set_ylabel("speed / Mbps")#y軸のラベル
                ax.set_ylim(0,Data.MaxSpeed*1.1)
                ax.set_xlabel("x / mm")#x軸のラベル
                ax.plot(x, y) #データの描画
                canvas = FigureCanvasTkAgg(fig, master=tki)
                canvas.draw()
                canvas.get_tk_widget().place(x=10,y=62,width=480,height=230)
                print(count)
                print(x)
                print(y)
            
                tki.after(1000,repeat_func)
            else:
                time.sleep(2)
                tki.destroy()
                nonlocal Stop
                Stop = True
        tki.after(1000,repeat_func)
        tki.mainloop()
        return Stop