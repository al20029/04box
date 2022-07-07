import ManagementWiFi
import time

# WiFiName = "TestA_1"
# AverageSpeed = 30.0
# Stability = 30
MeasurementTime = time.time()
# ManagementWiFi.ManagementWiFi.RegisterData(WiFiName, AverageSpeed, Stability, MeasurementTime)
# ManagementWiFi.ManagementWiFi.SendPastData(WiFiName, AverageSpeed, Stability)
CanConnectWiFiName = ["TestA_1","TestA_3"]
ManagementWiFi.ManagementWiFi.SendRealtimeData(MeasurementTime, CanConnectWiFiName)