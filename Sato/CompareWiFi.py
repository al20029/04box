import datetime
from ManagementWiFi import ManagementWiFi

class CompareWiFi():
    def CompareWiFi():
        date = datetime.datetime.now()
        return ManagementWiFi.SendRealtimeData(date)