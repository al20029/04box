import ManagementWiFi
import datetime

WiFiName = "TestA_1"
AverageSpeed = 30.0
Stability = 30
MeasurementTime = datetime.datetime.now()
ManagementWiFi.ManagementWiFi.RegisterData(WiFiName, AverageSpeed, Stability)
ManagementWiFi.ManagementWiFi.SendPastData(WiFiName, AverageSpeed, Stability)
# CanConnectWiFiName = ["TestA_1","TestA_3"]
# ManagementWiFi.ManagementWiFi.SendRealtimeData(MeasurementTime, CanConnectWiFiName)