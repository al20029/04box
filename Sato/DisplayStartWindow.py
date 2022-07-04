"""
******************************************************************
***  File Name		: DisplayStartWindow.py
***  Version		: V1.0
***  Designer		: 池戸 陸
***  Date			: 2022.07.01
***  Purpose        : 計測開始画面
***
*******************************************************************
*** Revision :
*** V1.1 : 池戸陸,
"""

from ast import Break
import subprocess
import time
from InteractWithOS import InteractWithOS
import tkinter
import tkinter.ttk as ttk
from ToolTip import *
import Data

"""
*******************************************************************
***  Class Name		: DisplayStartWindow
***  Designer		    : 池戸 陸
***  Date		        : 2022.07.01
***  Function			: 計測開始画面を表示する
***  Return      	    : -1 エラー
                          0以上 画面表示
***
*******************************************************************
"""
class DisplayStartWindow:
    def StartWindow(CanConnectWiFiname):
        def btn_click():
            InteractWithOS.ChangeWiFi(combobox.get())

            #WiFi変更が完了するまで待機 
            # Result_change = str()
            # while Result_change == None:
            #     Result_change = subprocess.run('netsh wlan show interface', encoding='utf-8', shell=True)
            time.sleep(1)

            nonlocal Start
            Start = True
            if bln.get():
                print('チェックされています')
                f = open('checkbox.txt','w')
                f.write('1')
                f.close()    
            else:
                print('チェックされていません')
                f = open('checkbox.txt','w')
                f.write('0')
                f.close()
            frm.destroy()
        Start = False
        frm = tkinter.Tk()
        frm.geometry('500x270')
        frm.title('計測開始画面')
        chk1 = tkinter.Label(frm,text = 'Wi-Fi速度計測システム', font = ('MSゴシック',35))
        chk1.place(x = 15, y = 85)
        bln = tkinter.BooleanVar()
        f = open("checkbox.txt","r")
        bln.set(f.read())
        f.close
        #bln.set(Data.Data.checkbox)
        chk2 = tkinter.Checkbutton(frm, variable = bln, text = '定期計測を利用する', font = ('MSゴシック',10))
        chk2.place(x = 270, y = 30)
        chk3 = tkinter.Label(frm, text = '?', font = ('MSゴシック',10))
        chk3.place(x = 410, y = 30)
        chk4 = tkinter.Label(frm, text = '現在接続しているWi-Fi', font = ('MSゴシック',15))
        chk4.place(x = 80,y = 170)

        list = CanConnectWiFiname

        combobox = ttk.Combobox(frm, height=3, width = 40, values = list, state = "readonly")
        combobox.current(0)
        combobox.place(x = 50, y = 200)

        btn = tkinter.Button(frm, text='計測開始',width = 18,height = 2, command = btn_click, bg='#808080', font = ('MSゴシック', 10))
        btn.place(x = 330, y = 200)

        ToolTip(chk3, "一定の間隔で自動計測をして最適なWi-Fiを提案します")
        frm.mainloop()
        Break
        return Start