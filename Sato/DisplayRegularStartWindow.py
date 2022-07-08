"""
******************************************************
*** File Name       :DisplayRegularStartWindow.py
*** Version         :V1.0
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :定期計測中画面を表示する
*** 
******************************************************
"""

import tkinter

import paramiko
# from tkinter import messagebox
from ManagementWiFi import ManagementWiFi
from InteractWithOS import InteractWithOS
from ManagementDownload import ManagementDownload
# from ManagementDownload import ManagementDownload
from MainMeasurement import MainMeasurement
from CompareWiFi import CompareWiFi
from ssh import ssh

"""
******************************************************
*** File Name       :DisplayRegularStartWindow
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :定期計測中画面を表示し、ユーザの入力を受け取る
*** 
******************************************************
"""

class DisplayRegularStartWindow:
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
            # Y_N = messagebox.askyesno("確認中", "停止しますか")
            # if Y_N == True:   
            Stop = True
            tki.quit()
                # tki.destroy()

        # 画面作成
        tki = tkinter.Tk()
        tki.withdraw()
        tki.deiconify()
        h = tki.winfo_screenheight() - 370
        w = tki.winfo_screenwidth() - 305
        tki.geometry('300x300+'+str(w)+"+"+str(h)) # 画面サイズの設定
        tki.title('定期計測中画面') # 画面タイトルの設定

        #題名表示
        SystemName = tkinter.Label(text="速度計測中", font=("MSゴシック", "30", "bold"))
        SystemName.place(x=50, y=10)

        #画像表示
        canvas = tkinter.Canvas(tki, width=200, height=200)
        canvas.place(x=50, y=60)
        wi_fi = tkinter.PhotoImage(file = "wi-fi.png", width=200, height=200)
        canvas.create_image(0, 20, image = wi_fi, anchor = tkinter.NW)

        # ボタンの作成
        btn = tkinter.Button(tki, text='計測中止', width = 10, height = 2, command = btn_click, font=("MSゴシック", "10"))
        btn.place(x=200, y=250) #ボタンを配置する位置の設定

        # 繰り返しダウンロードする
        def Repeat_Download():
            nonlocal tki
            nonlocal count
            nonlocal BestWiFiName

            count -= 1
            MainMeasurement.Measurement(data)
            # faster,a,b = MainMeasurement.Measurement(a)
            # print(MainMeasurement.Measurement(a))
            if count > 0:
                tki.after(1000, Repeat_Download)
            else:
                
                ################# 変更点#################
                WiFiList = list()
                WiFiList = InteractWithOS.GetWiFi()
                # リストから現在のWi-Fi名を削除
                # 計測値の登録
                AverageSpeed = MainMeasurement.AverageSpeedMeasurement(data.ListInstantSpeed, len(data.ListInstantSpeed))
                Stability = MainMeasurement.StabilityCalculation(data.ListInstantSpeed, len(data.ListInstantSpeed))
                print(WiFiList[0])
                print(AverageSpeed)
                print(Stability)
                ssh.ParamikoReg(WiFiList.pop(0), int(AverageSpeed), sum(Stability)/len(Stability))
                # ManagementWiFi.RegisterData(WiFiList.pop(0), AverageSpeed, Stability)
                # リアルタイムデータから最適なWi-Fiを探す
                # ManagementWiFi.SendRealtimeData(WiFiList)
                BestWiFiName = CompareWiFi.CompareWiFi(WiFiList)

                ########################################
                tki.destroy()
                # tki.quit()

        # 繰り返しダウンロードする
        tki.after(1000, Repeat_Download)


        # ################# 変更点#################
        # WiFiList = list()
        # WiFiList = InteractWithOS.GetWiFi()
        # # リストから現在のWi-Fi名を削除
        # # 計測値の登録
        # AverageSpeed = MainMeasurement.AverageSpeedMeasurement(data.ListInstantSpeed, len(data.ListInstantSpeed))
        # Stability = MainMeasurement.StabilityCalculation(data.ListInstantSpeed, len(data.ListInstantSpeed))
        # ManagementWiFi.RegisterData(WiFiList.pop(0), AverageSpeed, Stability)
        # # リアルタイムデータから最適なWi-Fiを探す
        # # ManagementWiFi.SendRealtimeData(WiFiList)
        # BestWiFiName = CompareWiFi(WiFiList)

        # #########################################
        
        # 画面をそのまま表示
        tki.mainloop()

        

        return Stop, BestWiFiName