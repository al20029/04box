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

# import window
# import window2
# import window3
# from typing import List
from DisplayStartWindow import DisplayStartWindow
from DisplayFinishWindow import DisplayFinishWindow
from DisplayOngoingWindow import DisplayOngoingWindow
from DisplayRegularStartWindow import DisplayRegularStartWindow
from DisplayRegularFinishWindow import DisplayRegularFinishWindow
from IntractWithOS import IntractWithOS

# window.test()
# window2.test()
# window3.test()

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
    for s in IntractWithOS.GetWiFi():
        print(s)
    get = DisplayRegularStartWindow.RegularStartWindow()
    # get = True
    name = "SRAS2G"
    if get == False:
        DisplayRegularFinishWindow = DisplayRegularFinishWindow.RegularFinishWindow(name)

        
maintest = UIMainProcess()