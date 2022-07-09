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
import os
import time
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

        
        #############################変更点###############################
        def subprocess_args(include_stdout=True):
            # The following is true only on Windows.
            if hasattr(subprocess, 'STARTUPINFO'):
                # Windowsでは、PyInstallerから「--noconsole」オプションを指定して実行すると、
                # サブプロセス呼び出しはデフォルトでコマンドウィンドウをポップアップします。
                # この動作を回避しましょう。
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                # Windowsはデフォルトではパスを検索しません。環境変数を渡してください。
                env = os.environ
            else:
                si = None
                env = None

            # subprocess.check_output()では、「stdout」を指定できません。
            #
            #   Traceback (most recent call last):
            #     File "test_subprocess.py", line 58, in <module>
            #       **subprocess_args(stdout=None))
            #     File "C:Python27libsubprocess.py", line 567, in check_output
            #       raise ValueError('stdout argument not allowed, it will be overridden.')
            #   ValueError: stdout argument not allowed, it will be overridden.
            #
            # したがって、必要な場合にのみ追加してください。
            if include_stdout:
                ret = {'stdout': subprocess.PIPE}
            else:
                ret = {}

            # Windowsでは、「--noconsole」オプションを使用してPyInstallerによって
            # 生成されたバイナリからこれを実行するには、
            # OSError例外「[エラー6]ハンドルが無効です」を回避するために
            # すべて（stdin、stdout、stderr）をリダイレクトする必要があります。
            ret.update({'stdin': subprocess.PIPE,
                        'stderr': subprocess.PIPE,
                        'startupinfo': si,
                        'env': env})
            return ret
        #########################################################################


        #利用可能なネットワークの検索
        e = subprocess.run('chcp 437', shell=True)

        # with open('out_network.txt', 'w') as nfp:
        Result_network = subprocess.run('netsh wlan show network', **subprocess_args(True)).stdout.decode('utf-8', errors='ignore').splitlines()
        # Result_network = subprocess.run('netsh wlan show network', **subprocess_args(True)).stdout.decode('utf-8').splitlines()
        

        # with open('out_network.txt', 'r') as lines:
        #     Result_network = lines.read().splitlines()
        # subprocess.run('del out_network.txt', shell=True)


        for s in Result_network:
            if 'SSID' in s:
                # List_network.append(s[9:].replace(' ', '').replace('  ', '').decode('utf-8'))
                List_network.append(s[9:].replace(' ', '').replace('  ', ''))

        #過去に接続したネットワーク検索
        # with open('out_profiles.txt', 'w') as pfp:
        Result_profiles = subprocess.run('netsh wlan show profiles', **subprocess_args(True)).stdout.decode('utf-8', errors='ignore').splitlines()
        # Result_profiles = subprocess.run('netsh wlan show profiles', **subprocess_args(True)).stdout.decode('utf-8').splitlines()

        # with open('out_profiles.txt', 'r') as lines:
        #     Result_profiles = lines.read().splitlines()
        # subprocess.run('del out_profiles.txt', shell=True)

        for s in Result_profiles:
            if 'All User Profile' in s:
                # List_profiles.append(s[27:].replace(' ', '').replace('  ', '').decode('utf-8'))
                List_profiles.append(s[27:].replace(' ', '').replace('  ', ''))

        #現在接続しているWiFiの追加
        # with open('out_interface.txt', 'w') as pfp:
        Result_interface = subprocess.run('netsh wlan show interface', **subprocess_args(True)).stdout.decode('utf-8', errors='ignore').splitlines()
        # Result_interface = subprocess.run('netsh wlan show interface', **subprocess_args(True)).stdout.decode('utf-8').splitlines()

        # with open('out_interface.txt', 'r') as lines:
        #     Result_interface = lines.read().splitlines()
        # subprocess.run('del out_interface.txt', shell=True)

        ConnectingWiFiName = []
        for s in Result_interface:
            if '    Profile                : ' in s:
                # ConnectingWiFiName = s[29:].replace(' ', '').replace('  ', '').decode('utf-8')
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
        #############################変更点###############################
        def subprocess_args(include_stdout=True):
            # The following is true only on Windows.
            if hasattr(subprocess, 'STARTUPINFO'):
                # Windowsでは、PyInstallerから「--noconsole」オプションを指定して実行すると、
                # サブプロセス呼び出しはデフォルトでコマンドウィンドウをポップアップします。
                # この動作を回避しましょう。
                si = subprocess.STARTUPINFO()
                si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                # Windowsはデフォルトではパスを検索しません。環境変数を渡してください。
                env = os.environ
            else:
                si = None
                env = None

            # subprocess.check_output()では、「stdout」を指定できません。
            #
            #   Traceback (most recent call last):
            #     File "test_subprocess.py", line 58, in <module>
            #       **subprocess_args(stdout=None))
            #     File "C:Python27libsubprocess.py", line 567, in check_output
            #       raise ValueError('stdout argument not allowed, it will be overridden.')
            #   ValueError: stdout argument not allowed, it will be overridden.
            #
            # したがって、必要な場合にのみ追加してください。
            if include_stdout:
                ret = {'stdout': subprocess.PIPE}
            else:
                ret = {}

            # Windowsでは、「--noconsole」オプションを使用してPyInstallerによって
            # 生成されたバイナリからこれを実行するには、
            # OSError例外「[エラー6]ハンドルが無効です」を回避するために
            # すべて（stdin、stdout、stderr）をリダイレクトする必要があります。
            ret.update({'stdin': subprocess.PIPE,
                        'stderr': subprocess.PIPE,
                        'startupinfo': si,
                        'env': env})
            return ret
        #########################################################################

        command = 'netsh wlan connect name=' + ChangeWiFiName
        Result_change = subprocess.run(command, **subprocess_args(True)).stdout.decode('utf-8', errors='ignore').splitlines()
        # Result_change = subprocess.run(command, **subprocess_args(True)).stdout.decode('utf-8').splitlines()
        # Result_change = str()

        while Result_change == None:
            print("未接続")
            Result_change = subprocess.run(command, **subprocess_args(True)).stdout.decode('utf-8', errors='ignore').splitlines()
            # Result_change = subprocess.run(command, **subprocess_args(True)).stdout.decode('utf-8').splitlines()
        # return Result_change

        time.sleep(2)

    GetWiFi()