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
        get = DisplayStartWindow.StartWindow(InteractWithOS.GetWiFi())
        if get == True:
            get = DisplayOngoingWindow.OngoingWindow()
        if get == False:
            DisplayFinishWindow.FinishWindow


    def Regular():
        InteractWithOS.GetWiFi()
        get = DisplayRegularStartWindow.RegularStartWindow()
        # 
        name = "SRAS2G"
        if get == False:
            DisplayRegularFinishWindow.RegularFinishWindow(name)
