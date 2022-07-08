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

# class MainManagementWiFi:
# def main():
args = sys.argv
print(args)
if args[1] == "1":
    print(1)
    ManagementWiFi.ManagementWiFi.RegisterData(args[2], float(args[3]), int(args[4]))
elif args[1] == "2":
    print(2)
    ManagementWiFi.ManagementWiFi.SendPastData(args[2])
elif args[1] == "3":
    print(3)
    CanConnectWiFiName = list()
    for i in range(3, 3+int(args[2])):
        CanConnectWiFiName.append(args[i])
    ManagementWiFi.ManagementWiFi.SendRealtimeData(CanConnectWiFiName)
