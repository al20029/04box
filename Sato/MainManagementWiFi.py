"""
*******************************************************************
***  File Name      : MainManagementWiFi.py
***  Version        : V1.0
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.21
***  Purpose       	: Wi-Fi情報管理の動作を決定する.
***
*******************************************************************/
"""
import ManagementWiFi
import sys
# from Arakawa.ManagementWiFi import ManagementWiFi

class MainManagementWiFi:
    def main():
        args = sys.argv
        if args[1] == 1:
            ManagementWiFi.ManagementWiFi.RegisterData()
        elif args[2] == 2:
            ManagementWiFi.ManagementWiFi.SendPastData()
        elif args[3] == 3:
            ManagementWiFi.ManagementWiFi.SendRealtimeData()