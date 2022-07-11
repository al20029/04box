"""
******************************************************
*** File Name       : ManagementDownload.py
*** Version         : V1.0
*** Designer        : 佐藤 光
*** Date            : 2022/06/14
*** Purpose         : MBのファイルをダウンロードする
*** 
******************************************************
"""

import urllib.request

class ManagementDownload:

    """
    *******************************************************************
    ***  Function Name  : Download
    ***  Version        : V1.0
    ***  Designer       : 
    ***  Date           : 2022.6.21
    ***  Purpose       	: 
    ***
    *******************************************************************/
    """

    def Donwload():
        try:
            urllib.request.urlopen('https://al86-hs.github.io/DownloadTest/test2M').read()
            return True
        except:
            return False