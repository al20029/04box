"""
******************************************************
*** File Name       :UI_main.py
*** Version         :V1.0
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :Windowを表示しその戻り値をもとに他のコンポーネント、OSとやり取りをする
*** 
******************************************************
"""

from DisplayStartWindow import DisplayStartWindow
from DisplayFinishWindow import DisplayFinishWindow
from DisplayOngoingWindow import DisplayOngoingWindow
from DisplayRegularStartWindow import DisplayRegularStartWindow
from DisplayRegularFinishWindow import DisplayRegularFinishWindow
from InteractWithOS import InteractWithOS
# from MainMeasurement import MainMeasurement
from Data import Data
from GetSendDB import GetSendDB
# from ManagementWiFi import ManagementWiFi
import time

"""
******************************************************
*** File Name       :UIMainProcess
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :Windowを表示しその戻り値をもとに他のコンポーネント、OSとやり取りをする
*** 
******************************************************
"""

class UIMainProcess:
    def __init__(self):
        print("hello")
    def Always():
        # データベースの取得
        GetSendDB.download()

        list = []
        DataList =[]
        while len(list) == 0:
            list = InteractWithOS.GetWiFi()
        print(1)
        a = Data()
        DataList.append(a)
        get,WiFiname = DisplayStartWindow.StartWindow(list)
        a.WiFiname = WiFiname
        list.remove(WiFiname)
        list.insert(0, WiFiname)
        print(a.WiFiname)
        while(get):
            get = DisplayOngoingWindow.OngoingWindow(a)
            if get == True:
                if '接続されていません'in list:
                    list.remove('接続されていません')
                get,WiFiname = DisplayFinishWindow.FinishWindow(list,DataList)
                list.remove(WiFiname)
                list.insert(0, WiFiname)
                a = Data()
                DataList.append(a)
                for data in (DataList):
                    if data.WiFiname == WiFiname:
                        a = data
                        a.ListInstantSpeed = []
                        a.MaxSpeed = 0
                    else:
                        a.WiFiname = WiFiname

        # データベースの送信
        GetSendDB.upload()

    def Regular():
        # データベースの取得
        # GetSendDB.download()

        # サーバ使わないパターン
        Fastest_WiFi = ""
        fastest = 0
        a = Data()
        WiFiList = list()
        WiFiList = InteractWithOS.GetWiFi()
        for s in WiFiList:
            # print(s)
            InteractWithOS.ChangeWiFi(s)
            time.sleep(1)
            get, fast = DisplayRegularStartWindow.RegularStartWindow(a)

            print(get)
            if get == True:
                break
            if fast[0] > fastest:
                fastest = fast[0]

            if fast > fastest:
                fastest = fast
                Fastest_WiFi = s
        # get = True

        # リアルタイムデータから最適なWi-Fiを探す
        # ManagementWiFi.SendRealtimeData(a.ListInstantSpeed[1])
        name = Fastest_WiFi


        if get == False:
            DisplayRegularFinishWindow.RegularFinishWindow(name)

        # データベースの送信
        # GetSendDB.upload()

        
# UIMainProcess.Always()
# UIMainProcess.Regular()