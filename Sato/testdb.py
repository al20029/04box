import ManagementWiFi
import time

WiFiName = "test1"
AverageSpeed = 45
Stability = 200
MeasureTime = time.time()
ManagementWiFi.ManagementWiFi.RegisterData(WiFiName, AverageSpeed, Stability, MeasureTime)
ManagementWiFi.ManagementWiFi.SendPastData(WiFiName, AverageSpeed, Stability)