"""
*******************************************************************
*** File Name       : UI_main.py
*** Version         : V1.1
*** Designer        : 佐藤 光
*** Date            : 2022/06/14
*** Purpose         : 通常計測，定期計測の二つに分けて，処理を行う．
*******************************************************************
"""

from DisplayStartWindow import DisplayStartWindow
from DisplayFinishWindow import DisplayFinishWindow
from DisplayOngoingWindow import DisplayOngoingWindow
from DisplayRegularStartWindow import DisplayRegularStartWindow
from DisplayRegularFinishWindow import DisplayRegularFinishWindow
from InteractWithOS import InteractWithOS
from Data import Data

"""
*******************************************************************
*** Class Name      : UIMainProcess
*** Designer        : 佐藤 光
*** Date            : 2022/06/14
*** Purpose         : 通常計測，定期計測の二つに分けて，処理を行う．
*******************************************************************
"""

class UIMainProcess:
    
    def __init__(self):
        print("hello")

    """
    *******************************************************************
    *** Function Name   : Always
    *** Designer        : 佐藤 光
    *** Date            : 2022/06/14
    *** Purpose         : 通常計測で行う処理をする. Windowを表示し
                          その戻り値をもとに他のコンポーネントやOSとやり取りをする.
    *******************************************************************
    """

    def Always():

        list = []
        DataList =[]
        while len(list) == 0:
            list = InteractWithOS.GetWiFi()
        a = Data()
        DataList.append(a)
        get,WiFiName, WiFiList = DisplayStartWindow.StartWindow(list)
        list = []
        list.extend(WiFiList)
        if get == False:
            return
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
                list = []
                list.extend(WiFiList)
                list.remove(WiFiName)
                list.insert(0, WiFiName)
                a = Data()
                for data in (DataList):
                    if data.WiFiName == WiFiName:
                        a = data
                        a.ListInstantSpeed = []
                        a.MaxSpeed = 0
                        break
                    elif data == DataList[-1]:
                        a.WiFiName = WiFiName
                        DataList.append(a)
                for data in (DataList):
                    print(data.WiFiName)

    """
    *******************************************************************
    *** Function Name   : Regular
    *** Designer        : 佐藤 光
    *** Date            : 2022/06/14
    *** Purpose         : 定期計測で行う処理をする。Windowを表示し
                          その戻り値をもとに他のコンポーネント、OSとやり取りをする.
    *******************************************************************
    """

    def Regular():

        a = Data()
        get,name = DisplayRegularStartWindow.RegularStartWindow(a)

        print("戻り値の出力")
        print(get)
        print(name)
        if get == False:
            DisplayRegularFinishWindow.RegularFinishWindow(name)