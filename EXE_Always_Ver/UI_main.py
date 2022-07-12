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
from Data import Data

class UIMainProcess:
    
    def __init__(self):

        print("hello")

    def Always():

        list = []
        DataList =[]
        while len(list) == 0:
            list = InteractWithOS.GetWiFi()
        print(1)
        a = Data()
        DataList.append(a)
        get,WiFiName, WiFiList = DisplayStartWindow.StartWindow(list)
        list = []
        list.extend(WiFiList)
        if get == False:
            return
        print("listの内容")
        print(list)
        print("WiFinameの内容")
        print(WiFiName)
        a.WiFiName = WiFiName
        list.remove(WiFiName)
        list.insert(0, WiFiName)
        print(a.WiFiName)
        while(get):
            get = DisplayOngoingWindow.OngoingWindow(a)
            if get == True:
                if '接続されていません'in list:
                    list.remove('接続されていません')
                get, WiFiName, WiFiList = DisplayFinishWindow.FinishWindow(list, DataList)
                print("WiFiList_UIMAIN")
                print(WiFiList)
                print("List_UIMAIN")
                print(list)
                list = []
                list.extend(WiFiList)
                list.remove(WiFiName)
                list.insert(0, WiFiName)
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

    def Regular():

        a = Data()
        get,name = DisplayRegularStartWindow.RegularStartWindow(a)

        print("戻り値の出力")
        print(get)
        print(name)
        if get == False:
            DisplayRegularFinishWindow.RegularFinishWindow(name)