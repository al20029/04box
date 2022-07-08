import ManagementWiFi
import datetime

WiFiName = "TestA_1"
AverageSpeed = 40.0
Stability = 40
MeasurementTime = datetime.datetime.now()
ManagementWiFi.ManagementWiFi.RegisterData(WiFiName, AverageSpeed, Stability)
ManagementWiFi.ManagementWiFi.SendPastData(WiFiName)
CanConnectWiFiName = ["TestA_1","TestA_2","TestA_3"]
ManagementWiFi.ManagementWiFi.SendRealtimeData(CanConnectWiFiName)
