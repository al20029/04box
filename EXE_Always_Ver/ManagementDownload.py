"""
******************************************************
*** File Name       :ManagementDownload.py
*** Version         :V1.1
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :2MBのファイルをダウンロードする
******************************************************
"""

import urllib.request

"""
******************************************************
*** Class Name      :ManagementDownload
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :2MBのファイルをダウンロードする
******************************************************
"""

class ManagementDownload:

    """
    *******************************************************************
    ***  Function Name      : Download
    ***  Designer		    : 佐藤 光
    ***  Date		        : 2022.07.01
    ***  Function			: 2MBのファイルをダウンロードする
    ***  Return      	    : Bool エラーのチェック
    *******************************************************************
    """  

    def Donwload():
        try:
            urllib.request.urlopen('https://al86-hs.github.io/DownloadTest/test2M').read()      
            return True
        except:
            return False