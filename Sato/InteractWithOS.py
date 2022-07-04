"""
******************************************************
*** File Name       :UI_main.py
*** Version         :V1.0
*** Designer        :佐藤 光
*** Date            :2022/06/14
*** Purpose         :Wi-Fiの変更を行う。接続可能なWi-Fi名をlistとして取得する
*** 
******************************************************
"""

import subprocess
# import tkinter
# from tkinter import messagebox

class InteractWithOS:
    """
    ******************************************************
    *** File Name       :GetWi_fi
    *** Designer        :佐藤 光
    *** Date            :2022/06/14
    *** Purpose         :接続可能なWi-Fi情報を取得する
    *** 
    ******************************************************
    """
    def GetWiFi():
        List_network = list()
        List_profiles = list()
        CanConnectWiFiName = list()

        # while 1:
        #利用可能なネットワークの検索
        subprocess.run('chcp 437', shell=True)

        with open('out_network.txt', 'w') as nfp:
            subprocess.run('netsh wlan show network', encoding='utf-8', stdout=nfp, shell=True)

        with open('out_network.txt', 'r') as lines:
            Result_network = lines.read().splitlines()
        subprocess.run('del out_network.txt', shell=True)


        for s in Result_network:
            if 'SSID' in s:
                List_network.append(s[9:].replace(' ', '').replace('  ', ''))

        #過去に接続したネットワーク検索
        with open('out_profiles.txt', 'w') as pfp:
            subprocess.run('netsh wlan show profiles', encoding='utf-8', stdout=pfp, shell=True)

        with open('out_profiles.txt', 'r') as lines:
            Result_profiles = lines.read().splitlines()
        subprocess.run('del out_profiles.txt', shell=True)

        for s in Result_profiles:
            if 'All User Profile' in s:
                List_profiles.append(s[27:].replace(' ', '').replace('  ', ''))

                #現在接続しているWiFiの追加
        with open('out_interface.txt', 'w') as pfp:
            subprocess.run('netsh wlan show interface', encoding='utf-8', stdout=pfp, shell=True)

        with open('out_interface.txt', 'r') as lines:
            Result_interface = lines.read().splitlines()
        subprocess.run('del out_interface.txt', shell=True)

        ConnectingWiFiName = []
        for s in Result_interface:
            if '    Profile                : ' in s:
                ConnectingWiFiName = s[29:].replace(' ', '').replace('  ', '')
                break
        # print(len(ConnectingWiFiName))

        #接続可能なネットワーク検索
        for lp in List_profiles:
            for ln in List_network:
                if ln==lp:
                    # print(len(ln))
                    CanConnectWiFiName.append(ln)
        if len(ConnectingWiFiName) == 0:
            ConnectingWiFiName = '接続されていません'
            CanConnectWiFiName.insert(0, ConnectingWiFiName)
        else: 
            CanConnectWiFiName.remove(ConnectingWiFiName)
            CanConnectWiFiName.insert(0, ConnectingWiFiName)
        return CanConnectWiFiName

    """
    ******************************************************
    *** File Name       :ChangeWi_Fi
    *** Designer        :佐藤 光
    *** Date            :2022/06/14
    *** Purpose         :Wi-Fiの変更を行う
    *** 
    ******************************************************
    """

    #Wi-Fi変更,接続が正常かを確認
    def ChangeWiFi(ChangeWiFiName):
        command = 'netsh wlan connect name=' + ChangeWiFiName
        subprocess.run(command, shell=True)
        Result_change = str()
        while Result_change == None:
            Result_change = subprocess.run('netsh wlan show interface', encoding='utf-8', shell=True)
        # return Result_change

    GetWiFi()