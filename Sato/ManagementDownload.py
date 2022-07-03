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

"""
******************************************************
*** File Name       :Download
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :MBのファイルをダウンロードする
*** 
******************************************************
"""

class ManagementDownload:
    def Donwload():
        try:
            urllib.request.urlopen('https://al86-hs.github.io/DownloadTest/test7M').read()
            return True
        except:
            return False

# print(ManagementDownload())