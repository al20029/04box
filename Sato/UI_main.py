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