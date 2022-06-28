"""
******************************************************************
***  File Name		: MainMeasurement.py
***  Version		: V1.0
***  Designer		: 池戸 陸
***  Date			: 2022.06.02
***  Purpose        : 計測処理
***
*******************************************************************
*** Revision :
*** V1.0 : 池戸陸, 2022.06.02
"""

import urllib.request
import time
#import ManagementDownload


"""
*******************************************************************
***  Class Name		: MainMeasurement
***  Designer		    : 池戸 陸
***  Date		        : 2022.06.02
***  Function			: 計測時にダウンロード情報管理にファイルを要求する
                          瞬間速度、平均速度、安定性を求める
***  Return      	    : -1 エラー
                          0以上 計測結果
***
*******************************************************************
"""

class MainMeasurement:

    """
    *******************************************************************
    ***  Func Name		    : InstantSpeed
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.06.12
    ***  Function			: 瞬間速度を計測する
    ***  Return      	    : 瞬間速度
    ***
    *******************************************************************
    """

    def InstantSpeedMeasurement(FileSize,MeasurementTime):
        return  FileSize / MeasurementTime

    """
    *******************************************************************
    ***  Func Name		    : AverageSpeed
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.06.12
    ***  Function			: 平均速度を計測する
    ***  Return      	    : 平均速度
    ***
    *******************************************************************
    """

    def AverageSpeedMeasurement(InstantSpeed,FileGetNum):
        return sum(InstantSpeed) / FileGetNum

    """
    *******************************************************************
    ***  Func Name		    : StabilityCalculation
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.06.12
    ***  Function			: 安定性を計算する
    ***  Return      	    : 安定性
    ***
    *******************************************************************
    """

    
    def StabilityCalculation(InstantSpeed,AverageSpeed):
        #評価値を計算する
        

        stability = 0
        return stability


























    def Measurement():
        FileSize = 7 * 8 #単位はMbps
        FileGetNum = 10
        InstantSpeed = []

        #ManagementDownload()
        for i in range(FileGetNum):
            #if ManagementDownload() == 1:
                #return -1
            url = "https://al86-hs.github.io/DownloadTest/test7M"
            InstantTime = time.time()
            data = urllib.request.urlopen(url).read()
            MeasurementTime = time.time() - InstantTime
            InstantSpeed.append(MainMeasurement.InstantSpeedMeasurement(FileSize,MeasurementTime))

        AverageSpeed = MainMeasurement.AverageSpeedMeasurement(InstantSpeed,FileGetNum)
        #Stability = StabilityCalculation(InstantSpeed,AverageSpeed)
        print(InstantSpeed,end = "Mbps\n")
        print(AverageSpeed,end = "Mbps\n")

       #return InstantSpeed,AverageSpeed,Stability

MainMeasurement.Measurement()

