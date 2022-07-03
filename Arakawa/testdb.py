import ManagementWiFi

WiFiName = "test"
AverageSpeed = 15
Stability = 100
MeasureTime = 2022-7-3
ManagementWiFi.ManagementWiFi.RegisterData(WiFiName, AverageSpeed, Stability, MeasureTime)
ManagementWiFi.ManagementWiFi.SendPastData(WiFiName, AverageSpeed, Stability)