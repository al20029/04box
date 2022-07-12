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
from asyncio.windows_events import NULL
import subprocess
import time
from tkinter import messagebox
from InteractWithOS import InteractWithOS
import tkinter
import tkinter.ttk as ttk
from ToolTip import *
import Data

class DisplayStartWindow:

    """
    *******************************************************************
    ***  Function Name  : StartWindow
    ***  Version        : V1.0
    ***  Designer       : 
    ***  Date           : 2022.6.21
    ***  Purpose       	: 
    ***
    *******************************************************************/
    """

    def StartWindow(CanConnectWiFiname):
        WiFiName = ''
        check = ''
        # WiFiList = CanConnectWiFiname
        def btn_click():
            if combobox.get() == '接続されていません':
                messagebox.showerror('エラー', 'Wi-Fiが接続されていません')
                return 0
            InteractWithOS.ChangeWiFi(combobox.get())
            nonlocal WiFiName 
            nonlocal check
            WiFiName = combobox.get()

            time.sleep(3)

            nonlocal Start
            Start = True
            if bln.get():
                # 自動起動のチェックが発動されたときの処理
                if check == 0:
                    with open('out_UserName.txt', 'w') as pfp:
                        subprocess.run('echo %USERNAME%', encoding = 'utf-8', stdout = pfp, shell = True)
                    with open('out_UserName.txt', 'r') as lines:
                        Result_echo = lines.read().splitlines()
                    for s in Result_echo:
                        if len(s) != 0:
                            UserName = s.replace(' ', '').replace('  ', '')
                            break
                    print(UserName)

                    # copyするファイルを自動起動処理.exeに
                    ins = 'copy a.txt C:\\Users\\' + UserName + '\\AppData\\Roaming\\Microsoft\\Windows\\\"Start Menu\"\\Programs\\Startup'
                    print(ins)
                    subprocess.run(ins, encoding='utf-8', shell = True)
                print('チェックされています')
                f = open('checkbox.txt', 'w')
                f.write('1')
                f.close()    
            else:
                # 自動起動のチェックが消されたときの処理
                if check == 1:
                    with open('out_UserName.txt', 'w') as pfp:
                        subprocess.run('echo %USERNAME%', encoding = 'utf-8', stdout = pfp, shell = True)
                    with open('out_UserName.txt', 'r') as lines:
                        Result_echo = lines.read().splitlines()
                    subprocess.run('del out_UserName.txt', shell = True)
                    for s in Result_echo:
                        if len(s) != 0:
                            UserName = s.replace(' ', '').replace('  ', '')
                            break
                    print(UserName)

                    # delするファイルを自動起動処理.exeに
                    ins = 'del C:\\Users\\' + UserName + '\\AppData\\Roaming\\Microsoft\\Windows\\\"Start Menu\"\\Programs\\Startup\\a.txt'
                    print(ins)
                    subprocess.run(ins, encoding = 'utf-8', shell = True)
                print('チェックされていません')
                f = open('checkbox.txt', 'w')
                f.write('0')
                f.close()
            frm.destroy()
        Start = False
        frm = tkinter.Tk()
        frm.geometry('500x270')
        frm.title('計測開始画面')
        chk1 = tkinter.Label(frm,text = 'Wi-Fi速度計測システム', font = ('MSゴシック', 35))
        chk1.place(x = 15, y = 85)
        bln = tkinter.BooleanVar()
        f = open("checkbox.txt", "r")
        bln.set(f.read())
        check = bln.get()
        f.close
        chk2 = tkinter.Checkbutton(frm, variable = bln, text = '定期計測を利用する', font = ('MSゴシック', 10))
        chk2.place(x = 270, y = 30)
        chk3 = tkinter.Label(frm, text = '?', font = ('MSゴシック', 10))
        chk3.place(x = 410, y = 30)
        chk4 = tkinter.Label(frm, text = '現在接続しているWi-Fi', font = ('MSゴシック', 15))
        chk4.place(x = 80, y = 170)

        list = CanConnectWiFiname

        combobox = ttk.Combobox(frm, height = 3, width = 40, values = list, state = "readonly")
        combobox.current(0)
        combobox.place(x = 50, y = 200)

        btn = tkinter.Button(frm, text = '計測開始', width = 18, height = 2, command = btn_click, bg = '#808080', font = ('MSゴシック', 10))
        btn.place(x = 330, y = 200)

        ToolTip(chk3, "一定の間隔で自動計測をして最適なWi-Fiを提案します")
        frm.mainloop()
        Break
        return Start, WiFiName