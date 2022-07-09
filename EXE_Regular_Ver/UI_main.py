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

# from cv2 import compare
from DisplayStartWindow import DisplayStartWindow
from DisplayFinishWindow import DisplayFinishWindow
from DisplayOngoingWindow import DisplayOngoingWindow
from DisplayRegularStartWindow import DisplayRegularStartWindow
from DisplayRegularFinishWindow import DisplayRegularFinishWindow
from InteractWithOS import InteractWithOS
# from MainMeasurement import MainMeasurement
from Data import Data
# from GetSendDB import GetSendDB
from ManagementWiFi import ManagementWiFi
# import time
from CompareWiFi import CompareWiFi

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
        # GetSendDB.download()

        list = []
        DataList =[]
        while len(list) == 0:
            list = InteractWithOS.GetWiFi()
        print(1)
        a = Data()
        DataList.append(a)
        get,WiFiName = DisplayStartWindow.StartWindow(list)
        a.WiFiName = WiFiName
        list.remove(WiFiName)
        list.insert(0, WiFiName)
        print(a.WiFiName)
        while(get):
            get = DisplayOngoingWindow.OngoingWindow(a)
            if get == True:
                if '接続されていません'in list:
                    list.remove('接続されていません')
                get,WiFiName = DisplayFinishWindow.FinishWindow(list,DataList)
                list.remove(WiFiName)
                list.insert(0, WiFiName)
                print(WiFiName)
                a = Data()
                print("P1")
                for data in (DataList):
                    print(data.WiFiName)
                for data in (DataList):
                    if data.WiFiName == WiFiName:
                        a = data
                        a.ListInstantSpeed = []
                        a.MaxSpeed = 0
                        break
                    elif data == DataList[-1]:
                        a.WiFiName = WiFiName
                        DataList.append(a)
                print("P2")
                for data in (DataList):
                    print(data.WiFiName)

        # データベースの送信
        # GetSendDB.upload()

    def Regular():
        # データベースの取得
        # GetSendDB.download()

        # サーバ使わないパターン
        # Fastest_WiFi = ""
        # fastest = 0
        # for s in WiFiList:
        #     # print(s)
        #     InteractWithOS.ChangeWiFi(s)
        #     time.sleep(1)

        #     print(get)
        #     if get == True:
        #         break
        #     if fast[0] > fastest:
        #         fastest = fast[0]
        #         Fastest_WiFi = s
        # get = True

        a = Data()
        # WiFiList = list()
        # WiFiList = InteractWithOS.GetWiFi()
        get,name = DisplayRegularStartWindow.RegularStartWindow(a)

        # リアルタイムデータから最適なWi-Fiを探す
        # ManagementWiFi.SendRealtimeData(WiFiList)
        # name = CompareWiFi()
        # Fastest_WiFi()

        print("戻り値の出力")
        print(get)
        print(name)
        if get == False:
            DisplayRegularFinishWindow.RegularFinishWindow(name)

        # データベースの送信
        # GetSendDB.upload()

        
# UIMainProcess.Always()
# UIMainProcess.Regular()