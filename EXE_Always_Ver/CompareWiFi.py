"""
*******************************************************************
***  File Name      : CompareWiFi.py
***  Version        : V1.1
***  Designer       : 太田 峻輔
***  Date           : 2022.6.14
***  Purpose       	: Wi-Fi情報管理から受け取った各Wi-Fiの代表値を比較し、
                      最も評価の高いWi-Fi名を返す
*******************************************************************/
"""

from ssh import ssh

"""
*******************************************************************
***  Class Name     : CompareWiFi
***  Designer       : 太田 峻輔
***  Date           : 2022.6.14
***  Purpose       	: Wi-Fi情報管理から受け取った各Wi-Fiの代表値を比較し、
                      最も評価の高いWi-Fi名を返す
*******************************************************************/
"""

class CompareWiFi():

    """
    *******************************************************************
    ***  Function Name  : CompareWiFi
    ***  Version        : V1.1
    ***  Designer       : 太田 峻輔
    ***  Date           : 2022.6.21
    ***  Purpose       	: Wi-Fi情報管理から受け取った各Wi-Fiの代表値を比較し、
                          最も評価の高いWi-Fi名を返す
    ***  Return         : String型 今よりも評価の高いWi-Fi名があるときはそのWi-Fi名
                          None 現在のが一番評価が高いときは返り値はNone
    *******************************************************************/
    """

    def CompareWiFi(WiFiList, MeasuredWiFiEval):
        WiFiNames = list()
        AverageSpeeds = list()
        Stabilities = list()
        Calculation = list()
        key, WiFiNames, AverageSpeeds, Stabilities = ssh.ParamikoGetReal(WiFiList)

        if key == 0:
            return None
        print("key = ")
        print(key)

        for i in range(len(AverageSpeeds)):
            Calculation.append(AverageSpeeds[i]*Stabilities[i])
        
        #接続可能なWiFiの中で最も評価の高い数値を求める
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
                EvalList.append(SumStab[i] / Count[i])
        if max(EvalList) < MeasuredWiFiEval:
            return None
        else:
            return WiFiList[EvalList.index(max(EvalList))]