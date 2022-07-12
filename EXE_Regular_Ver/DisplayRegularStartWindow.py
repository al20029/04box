"""
******************************************************
*** File Name       :DisplayRegularStartWindow.py
*** Version         :V1.0
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :定期計測中画面を表示し、ユーザの入力を受け取る
*** 
******************************************************
"""

import tkinter
from InteractWithOS import InteractWithOS
from ManagementDownload import ManagementDownload
from MainMeasurement import MainMeasurement
from CompareWiFi import CompareWiFi
import subprocess
from ssh import ssh
import os

class DisplayRegularStartWindow:

    """
    *******************************************************************
    ***  Function Name  : RegularStartWindow
    ***  Version        : V1.0
    ***  Designer       : 
    ***  Date           : 2022.6.21
    ***  Purpose       	: 
    ***
    *******************************************************************/
    """

    def RegularStartWindow(data):
        Stop = False
        BestWiFiName = ""
        # ダウンロードする回数
        count = 10

        #空ダウンロード
        ManagementDownload.Donwload()

        # click時のイベント
        def btn_click():
            nonlocal Stop
            Stop = True
            tki.destroy()

        # 画面作成
        tki = tkinter.Tk()
        tki.withdraw()
        tki.deiconify()
        h = tki.winfo_screenheight() - 370
        w = tki.winfo_screenwidth() - 305
        tki.geometry('300x300+'+str(w)+"+"+str(h)) # 画面サイズの設定
        tki.title('定期計測中画面') # 画面タイトルの設定

        #題名表示
        SystemName = tkinter.Label(text = "速度計測中", font = ("MSゴシック", "30", "bold"))
        SystemName.place(x = 50, y = 10)

        #画像表示
        canvas = tkinter.Canvas(tki, width = 200, height = 200)
        canvas.place(x = 50, y = 60)

        _env = os.environ
        with open('out_UserName.txt', 'w') as nfp:
            subprocess.run('echo %USERNAME%', stdout = nfp, env = _env, shell = True)
        f = open("out_UserName.txt","r")
        Result_echo = f.read().splitlines()
        for s in Result_echo:
            if len(s) != 0:
                UserName = s.replace(' ', '').replace('  ', '')
                break
        print(UserName)
        wi_fi = tkinter.PhotoImage(file = r"C:\Users\\" + UserName + "\MAIFI\\wi-fi.png", width = 200, height = 200)
        canvas.create_image(0, 20, image = wi_fi, anchor = tkinter.NW)

        # ボタンの作成
        btn = tkinter.Button(tki, text = '計測中止', width = 10, height = 2, command = btn_click, font = ("MSゴシック", "10"))
        btn.place(x = 200, y = 250) #ボタンを配置する位置の設定

        # 繰り返しダウンロードする
        def Repeat_Download():
            nonlocal Stop
            nonlocal tki
            nonlocal count
            nonlocal BestWiFiName
            Stop = True
            count -= 1
            if MainMeasurement.Measurement(data) == -1:
                print("エラー通ってますよ")
                WiFiError()
            if count > 0:
                tki.after(1000, Repeat_Download)
            else:
                Stop = False
                ################# 変更点#################
                WiFiList = list()
                WiFiList = InteractWithOS.GetWiFi()
                # リストから現在のWi-Fi名を削除
                # 計測値の登録
                AverageSpeed = MainMeasurement.AverageSpeedMeasurement(data.ListInstantSpeed, len(data.ListInstantSpeed))
                Stability = MainMeasurement.cmpstability(data.ListInstantSpeed, len(data.ListInstantSpeed))
                WiFi = WiFiList.pop(0)
                #現在接続していないWiFiの中で接続可能なWiFiがない場合は現在接続しているWiFiを最適とする

                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                ssh.ParamikoReg(WiFi, AverageSpeed, Stability)
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                if len(WiFiList) == 0:
                    BestWiFiName = WiFi
                else:
                    BestWiFiName = CompareWiFi.CompareWiFi(WiFiList, AverageSpeed*Stability)
                    if BestWiFiName == None:
                        BestWiFiName = WiFi
                tki.destroy()

        def WiFiError():
            nonlocal Stop
            nonlocal tki
            nonlocal BestWiFiName
            tki.destroy()
            Stop = True
            BestWiFiName = InteractWithOS.GetWiFi().pop(0)
        tki.after(1000, Repeat_Download)
        
        # 画面をそのまま表示
        tki.mainloop()

        return Stop, BestWiFiName