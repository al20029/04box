"""
******************************************************
*** File Name       :ManagementDownload.py
*** Version         :V1.0
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :MBのファイルをダウンロードする
*** 
******************************************************
"""

import urllib.request

class ManagementDownload:
    def Donwload():
        try:
            urllib.request.urlopen('https://al86-hs.github.io/DownloadTest/test2M').read()      
            return True
        except:
            return False