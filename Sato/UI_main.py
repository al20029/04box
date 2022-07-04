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
    def Always():
        list = []
        DataList =[]
        while len(list) == 0:
            list = InteractWithOS.GetWiFi()
        print(1)
        get = DisplayStartWindow.StartWindow(list)
        print(2)
        if get == True:
            a = Data()
            DataList.append(a)
            print(3)
            get = DisplayOngoingWindow.OngoingWindow(a)
            print(4)
            print("a:",DataList[0].ListInstantSpeed)
            if get == True:
                print(5)
                get = DisplayFinishWindow.FinishWindow(list,DataList)
                print(6)
                while(get):
                    print(7)
                    b = Data()
                    DataList.append(b)
                    get = DisplayOngoingWindow.OngoingWindow(b)
                    print(8)
                    if get == True:
                        print(9)
                        get = DisplayFinishWindow.FinishWindow(list,DataList)
                        print(10)
    def Regular():
        for s in InteractWithOS.GetWiFi():
            print(s)
        get = DisplayRegularStartWindow.RegularStartWindow()
        # get = True
        name = "SRAS2G"
        if get == False:
            DisplayRegularFinishWindow.RegularFinishWindow(name)

        
UIMainProcess.Always()
# UIMainProcess.Regular()