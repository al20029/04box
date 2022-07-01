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

import tkinter
import tkinter.ttk as ttk
from ToolTip import *

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
    def btn_click(frm):
        frm.destroy()
    frm = tkinter.Tk()
    frm.geometry('500x270')
    frm.title('計測開始画面')
    chk1 = tkinter.Label(frm,text = 'Wi-Fi速度計測システム', font = ('MSゴシック',35))
    chk1.place(x = 15, y = 85)
    bln = tkinter.BooleanVar()
    bln.set(True)
    chk2 = tkinter.Checkbutton(frm, variable = bln, text = '定期計測を利用する', font = ('MSゴシック',10))
    chk2.place(x = 270, y = 30)
    chk3 = tkinter.Label(frm, text = '?', font = ('MSゴシック',10))
    chk3.place(x = 410, y = 30)
    chk4 = tkinter.Label(frm, text = '現在接続しているWi-Fi', font = ('MSゴシック',15))
    chk4.place(x = 80,y = 170)

    list = ("AAA", "BBB", "CCC") #単体テスト用
    #list = CanConnectWiFiname

    combobox = ttk.Combobox(frm, height=3, width = 40, values = list, state = "readonly")
    combobox.place(x = 50, y = 200)

    btn = tkinter.Button(frm, text='計測開始',width = 18,height = 2, command = btn_click, bg='#808080', font = ('MSゴシック', 10))
    btn.place(x = 330, y = 200)

    ToolTip(chk3, "一定の間隔で自動計測をして最適なWi-Fiを提案します")
    frm.mainloop()
