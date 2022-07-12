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
*** V1.1 : 池戸陸
"""

from ast import Break
import subprocess
from tkinter import messagebox
from InteractWithOS import InteractWithOS
import tkinter
import tkinter.ttk as ttk
from ToolTip import *
import Data
import os

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
        list = CanConnectWiFiname
        WiFiName = ''
        check = ''
        WiFiList = []
        WiFiList = CanConnectWiFiname

        def btn_click_list_change():
            nonlocal combobox
            nonlocal list
            list = InteractWithOS.GetWiFi()
            combobox = ttk.Combobox(frm, height = 3, width = 30, values = list, state = "readonly")
            combobox.current(0)
            combobox.place(x = 50, y = 200)

        def btn_click():
            if combobox.get() == '接続されていません':
                messagebox.showerror('エラー', 'Wi-Fiが接続されていません')
                return 0
            InteractWithOS.ChangeWiFi(combobox.get())
            nonlocal WiFiName 
            nonlocal check
            WiFiName = combobox.get()
            nonlocal Start
            Start = True
            if bln.get():

                ############################変更########################
                # 自動起動のチェックが発動されたときの処理
                if check == 0:
                    _env = os.environ
                    with open('out_UserName.txt', 'w') as nfp:
                        subprocess.run('echo %USERNAME%', stdout = nfp, env = _env, shell = True)
                    f = open("out_UserName.txt", "r")
                    Result_echo = f.read().splitlines()

                    for s in Result_echo:
                        if len(s) != 0:
                            UserName = s.replace(' ', '').replace('  ', '')
                            break
                    print(UserName)
                    # copyするファイルを自動起動処理.exeに
                    CpExe = 'copy *.lnk C:\\Users\\' + UserName + '\\AppData\\Roaming\\Microsoft\\Windows\\\"Start Menu\"\\Programs\\Startup'
                    subprocess.run(CpExe, shell = True)

                print('チェックされています')
                f = open('checkbox.txt', 'w')
                f.write('1')
                f.close()    
            else:
                # 自動起動のチェックが消されたときの処理
                if check == 1:
                    _env = os.environ
                    with open('out_UserName.txt', 'w') as nfp:
                        subprocess.run('echo %USERNAME%', stdout = nfp, env = _env, shell = True)
                    f = open("out_UserName.txt", "r")
                    Result_echo = f.read().splitlines()
                    for s in Result_echo:
                        if len(s) != 0:
                            UserName = s.replace(' ', '').replace('  ', '')
                            break
                    print(UserName)
                    # delするファイルを自動起動処理.exeに
                    DelExe = 'del C:\\Users\\' + UserName + '\\AppData\\Roaming\\Microsoft\\Windows\\\"Start Menu\"\\Programs\\Startup\\*.lnk'
                    subprocess.run(DelExe, shell = True)
                print('チェックされていません')
                f = open('checkbox.txt','w')
                f.write('0')
                f.close()
            ################################################################
            frm.destroy()
        Start = False
        frm = tkinter.Tk()
        w = frm.winfo_screenwidth() - 515
        h = frm.winfo_screenheight() - 350
        frm.geometry('500x270+' +str(w)+"+"+str(h)) # 画面サイズの設定
        frm.title('計測開始画面')
        chk1 = tkinter.Label(frm,text = 'Wi-Fi速度計測システム', font = ('MSゴシック',35))
        chk1.place(x = 15, y = 85)
        bln = tkinter.BooleanVar()
        f = open("checkbox.txt","r")
        bln.set(f.read())
        check = bln.get()
        f.close
        
        chk2 = tkinter.Checkbutton(frm, variable = bln, text = '定期計測を利用する', font = ('MSゴシック', 10))
        chk2.place(x = 270, y = 30)
        chk3 = tkinter.Label(frm, text = '?', font = ('MSゴシック', 10))
        chk3.place(x = 410, y = 30)
        chk4 = tkinter.Label(frm, text = '現在接続しているWi-Fi', font = ('MSゴシック',15))
        chk4.place(x = 80, y = 170)

        combobox = ttk.Combobox(frm, height = 3, width = 30, values = list, state = "readonly")
        combobox.current(0)
        combobox.place(x = 50, y = 200)

        btn = tkinter.Button(frm, text='計測開始', width = 18,height = 2, command = btn_click, bg = '#808080', font = ('MSゴシック', 10))
        btn.place(x = 330, y = 200)

        # リスト更新ボタン
        btn2 = tkinter.Button(frm, text = '↺', width = 6, height = 1, command = btn_click_list_change, bg = '#808080', font = ('MSゴシック', 10))
        btn2.place(x = 260, y = 200)

        ToolTip(chk3, "一定の間隔で自動計測をして最適なWi-Fiを提案します")
        frm.mainloop()
        Break
        WiFiList = list
        return Start, WiFiName, WiFiList