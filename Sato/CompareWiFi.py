import datetime
from ManagementWiFi import ManagementWiFi

class CompareWiFi():
    def CompareWiFi(WiFilist):
        ###################変更点#######################
        AverageSpeed = list()
        BestStability = list()
        date = datetime.datetime.now()
        AverageSpeed, BestStability = ManagementWiFi.SendRealtimeData(WiFilist, date)
        return 

        ################################################