# import datetime
from re import X
from ManagementWiFi import ManagementWiFi
from ssh import ssh

class CompareWiFi():
    def CompareWiFi(WiFiList, MeasuredWiFiEval):
        ###################変更点#######################
        WiFiNames = list()
        AverageSpeeds = list()
        Stabilities = list()
        Calculation = list()
        # date = datetime.datetime.now()
        # AverageSpeed, Stability = ManagementWiFi.SendRealtimeData(WiFilist, date)
        # AverageSpeed, Stability = ssh.ParamikoGetReal(2, WiFilist)
        key, WiFiNames, AverageSpeeds, Stabilities = ssh.ParamikoGetReal(WiFiList)

        if key == 0:
            return None
        print("key = ")
        print(key)

        for i in range(len(AverageSpeeds)):
            Calculation.append(AverageSpeeds[i]*Stabilities[i])
        
        ################################################
        #接続可能なWiFiの中で最も評価の高い数値を求める#
        ################################################
        Count = [0] * len(WiFiList)
        SumStab = [0] * len(WiFiList)
        for t in range(len(WiFiNames)):
            for j in range(len(WiFiList)):
                if WiFiNames[t] == WiFiList[j]:
                    Count[j] += 1
                    SumStab[j] += Calculation[t]
        EvalList = list()
        for i in range(len(Count)):
            if Count[i] == 0:
                EvalList.append(0)
            else:
                EvalList.append(SumStab[i]/Count[i])
        if max(EvalList) < MeasuredWiFiEval:
            # print("今の方がいい")
            return None
        else:
            # print("変えた方がいい")
            return WiFiList[EvalList.index(max(EvalList))]
        ################################################