import ManagementWiFi
import time

WiFiName = "TestA_1"
AverageSpeed = 10.0
Stability = 10
MeasurementTime = time.time()
ManagementWiFi.ManagementWiFi.RegisterData(WiFiName, AverageSpeed, Stability, MeasurementTime)
ManagementWiFi.ManagementWiFi.SendPastData(WiFiName, AverageSpeed, Stability)
CanConnectWiFiName = ["TestA_1","TestA_2","TestA_3"]
ManagementWiFi.ManagementWiFi.SendRealtimeData(MeasurementTime, CanConnectWiFiName)
