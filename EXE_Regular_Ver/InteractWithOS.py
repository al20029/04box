"""
*******************************************************************
*** File Name       : InteractWithOS.py
*** Version         : V1.1
*** Designer        : 佐藤 光
*** Date            : 2022/06/14
*** Purpose         : Wi-Fiの変更を行う。
                      接続可能なWi-Fi名をlistとして取得する
*******************************************************************
"""


import subprocess
import os
import time

"""
*******************************************************************
*** Class Name      : InteractWithOS
*** Designer        : 佐藤 光
*** Date            : 2022/06/14
*** Purpose         : Wi-Fiの変更を行う。
                      接続可能なWi-Fi名をlistとして取得する
*******************************************************************
"""

class InteractWithOS:

    """
    *******************************************************************
    *** Fuunction Name  : GetWiFi
    *** Designer        : 佐藤 光
    *** Date            : 2022/06/14
    *** Function        : 接続可能なWi-Fi情報を取得する
    *** Return          : String CanConnectWiFiName  接続可能なWiFi名
    *******************************************************************
    """

    def GetWiFi():
        List_network = list()
        List_profiles = list()
        CanConnectWiFiName = list()

        #利用可能なネットワークの検索
        _env = os.environ

        ########テキストベースのやりかた
        with open('out_network.txt', 'w') as nfp:
            subprocess.run('netsh wlan show network', stdout = nfp, env = _env, shell = True)
            ######パターン1
        f = open("out_network.txt", "r")
        Result_network = f.read().splitlines()
            ######パターン2

        for s in Result_network:
            if 'SSID' in s:
                List_network.append(s[9:].replace(' ', '').replace('  ', ''))
        print("network = ")
        print(List_network)

        #過去に接続したネットワーク検索
        
        ########テキストベースのやりかた
        with open('out_profiles.txt', 'w') as pfp:
            subprocess.run('netsh wlan show profiles', stdout = pfp, env = _env, shell = True)
            ######パターン1
        f = open("out_profiles.txt","r")
        Result_profiles = f.read().splitlines()
            ######パターン2
        for s in Result_profiles:
            if 'All User Profile' in s:
                List_profiles.append(s[27:].replace(' ', '').replace('  ', ''))
            elif '    すべてのユーザー プロファイル     : ' in s:
                List_profiles.append(s[26:].replace(' ', '').replace('  ', ''))

        print("profiles = ")
        print(List_profiles)

        #現在接続しているWiFiの追加

        #######テキストベースのやり方
        with open('out_interface.txt', 'w') as ifp:
            subprocess.run('netsh wlan show interface', stdout = ifp, env = _env, shell = True)
            ######パターン1
        f = open("out_interface.txt", "r")
        Result_interface = f.read().splitlines()
            ######パターン2 
        ConnectingWiFiName = []
        for s in Result_interface:
            if '    Profile                : ' in s:
                ConnectingWiFiName = s[29:].replace(' ', '').replace('  ', '')
                break
            elif '    プロファイル           : ' in s:
                ConnectingWiFiName = s[23:].replace(' ', '').replace('  ', '')
                break
        print("Connecting_InteractWithOS")
        print(ConnectingWiFiName)

        #接続可能なネットワーク検索
        for lp in List_profiles:
            for ln in List_network:
                if ln == lp:
                    CanConnectWiFiName.append(ln)
        print("CanConnect_IntereactWithOS")
        print(CanConnectWiFiName)
        if len(ConnectingWiFiName) == 0:
            print("選ばれたのは")
            print(CanConnectWiFiName)
            ConnectingWiFiName = '接続されていません'
            CanConnectWiFiName.insert(0, ConnectingWiFiName)
        else: 
            print(ConnectingWiFiName)
            CanConnectWiFiName.remove(ConnectingWiFiName)
            CanConnectWiFiName.insert(0, ConnectingWiFiName)
        return CanConnectWiFiName

    """
    *******************************************************************
    ***  Function Name  : ChangeWiFiName
    ***  Designer       : 佐藤 光
    ***  Date           : 2022.6.21
    ***  Purpose       	: Wi-Fiの変更を行う
    *******************************************************************/
    """

    #Wi-Fi変更,接続が正常かを確認
    def ChangeWiFi(ChangeWiFiName):

        ######テキストベースのやり方
        _env = os.environ
        command = 'netsh wlan connect name=' + ChangeWiFiName
        Result_change = subprocess.run(command, env = _env, shell = True)
        while Result_change == None:
            print("未接続")
            Result_change = subprocess.run('netsh wlan show interface', env = _env, shell = True)

        time.sleep(10)
        
        return Result_change