import datetime
from ManagementWiFi import ManagementWiFi
from ssh import ssh

class CompareWiFi():
    def CompareWiFi(WiFilist):
        ###################変更点#######################
        AverageSpeed = list()
        Stability = list()
        Calculation = list()
        date = datetime.datetime.now()
        # AverageSpeed, Stability = ManagementWiFi.SendRealtimeData(WiFilist, date)
        AverageSpeed, Stability = ssh.paramiko(2, WiFilist)
        Calculation = AverageSpeed*Stability
        return WiFilist.index(max(Calculation))

        ################################################