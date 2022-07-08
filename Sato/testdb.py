import ManagementWiFi
import datetime

WiFiName = "TestA_1"
AverageSpeed = 10.0
Stability = 10
MeasurementTime = datetime.datetime.now()
ManagementWiFi.ManagementWiFi.RegisterData(WiFiName, AverageSpeed, Stability)
ManagementWiFi.ManagementWiFi.SendPastData(WiFiName)
CanConnectWiFiName = ["TestA_1","TestA_3"]
ManagementWiFi.ManagementWiFi.SendRealtimeData(CanConnectWiFiName)
