from Data import Data
DataList = []
a = Data()
a.WiFiname='Wi-Fi:A'
DataList.append(a)
for i in range(10):
    a.ListInstantSpeed.append(i)
# print(DataList[0].ListInstantSpeed)
print(a.ListInstantSpeed)
print(DataList[0].ListInstantSpeed)
print(DataList[0].WiFiname)