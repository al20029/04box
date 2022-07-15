"""
******************************************************************
***  File Name		: MainMeasurement.py
***  Version		: V1.1
***  Designer		: 池戸 陸
***  Date			: 2022.06.02
***  Purpose        : 瞬間速度、平均速度、安定性を求め、UI処理部に返す.
*******************************************************************
*** Revision :
*** V1.1 : 池戸陸, 2022.07.01
"""

import time
from ManagementDownload import *
from UpdateGraph import UpdateGraph
import math

"""
*******************************************************************
***  Class Name		    : MainMeasurement
***  Designer		    : 池戸 陸
***  Date		        : 2022.06.02
***  Function			: 瞬間速度、平均速度、安定性を求め、UI処理部に返す.
*******************************************************************
"""

class MainMeasurement:

    """
    *******************************************************************
    ***  Function Name		: InstantSpeedMeasurement
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.06.12
    ***  Function			: 瞬間速度を計測する
    ***  Return      	    : float 瞬間速度
    *******************************************************************
    """

    def InstantSpeedMeasurement(FileSize, MeasurementTime):
        return  FileSize / MeasurementTime

    """
    *******************************************************************
    ***  Function Name		: AverageSpeed
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.06.12
    ***  Function			: 平均速度を計測する
    ***  Return      	    : float 平均速度
    *******************************************************************
    """

    def AverageSpeedMeasurement(InstantSpeed, FileGetNum):
        return sum(InstantSpeed) / FileGetNum

    """
    *******************************************************************
    ***  Function Name		: StabilityEvaluation
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.07.01
    ***  Function			: 安定性指数を決定する．
    ***  Return      	    : int 評価値
    *******************************************************************
    """

    def StabilityEvaluation(ev, stability):
        k = 0
        if(ev <= 4):
            k = 1
        elif(ev <= 8):
            k = 2
        elif(ev <= 12):
            k = 3
        elif(ev <= 16):
            k = 4
        elif(ev <= 20):
            k = 5
        return k

    """
    *******************************************************************
    ***  Function Name		: StabilityCalculation
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.07.01
    ***  Function			: 使用用途に応じた安定性を計算する.
    ***  Return      	    : int 安定性
    *******************************************************************
    """ 

    def StabilityCalculation(InstantSpeed, FileGetNum):
        # stability[0] = メール,LINE , [1] = ネット検索 , [2] = SNS , [3] = 動画視聴 , [4] = オンラインゲーム
        stability = [0, 0, 0, 0, 0]
        mail_ev = 0
        net_ev = 0
        sns_ev = 0
        movie_ev = 0
        game_ev = 0
        for i in range(FileGetNum):
            if InstantSpeed[i] >= 0.125:
                mail_ev += 1
                if InstantSpeed[i] >= 1:
                    mail_ev += 1
                    net_ev += 1
                    if InstantSpeed[i] >= 3:
                        sns_ev += 1
                        if InstantSpeed[i] >= 5:
                            movie_ev += 1
                            if InstantSpeed[i] >= 10:
                                net_ev += 1
                                sns_ev += 1
                                if InstantSpeed[i] >= 30:
                                    game_ev += 1
                                    movie_ev += 1
                                    if InstantSpeed[i] >= 100:
                                        game_ev += 1
        stability[0] = MainMeasurement.StabilityEvaluation(mail_ev, stability[0])
        stability[1] = MainMeasurement.StabilityEvaluation(net_ev, stability[1])
        stability[2] = MainMeasurement.StabilityEvaluation(sns_ev, stability[2])
        stability[3] = MainMeasurement.StabilityEvaluation(movie_ev, stability[3])
        stability[4] = MainMeasurement.StabilityEvaluation(game_ev, stability[4])
        return stability

    """
    *******************************************************************
    ***  Function Name      : Measurement
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.07.01
    ***  Function			: 計測時にダウンロード情報管理にファイルを要求し，
                              瞬間速度を求める．
    ***  Return      	    : float InstantSpeed 瞬間速度
    *******************************************************************
    """ 

    def Measurement(data):
        FileSize = 2 * 8 #単位はMbit
        FileGetNum = 1
        InstantSpeed = []
        InstantTime = time.time()
        
        if ManagementDownload.Donwload() == False:
            return -1
        MeasurementTime = time.time() - InstantTime
        InstantSpeed.append(MainMeasurement.InstantSpeedMeasurement(FileSize, MeasurementTime))
        UpdateGraph.UpdateGraph(InstantSpeed[-1], data)

        return InstantSpeed
    # InstantSpeedが10個の瞬間速度のリスト
    # AverageSpeedが平均速度
    # Stabilityがメール、ネット、sns、動画視聴、オンラインゲームの5項目を1~5段階に数値化したリスト
    # ManagementDownloadとの結合テスト完了

    """
    *******************************************************************
    ***  Function Name      : CmpStability
    ***  Designer		    : 池戸 陸
    ***  Date		        : 2022.07.01
    ***  Function			: 比較用の安定性を計算する．
    ***  Return      	    : float stablevel 安定性のレベル
    *******************************************************************
    """   

    def cmpstability(InstantSpeed, FileGetNum):
        average = MainMeasurement.AverageSpeedMeasurement(InstantSpeed, FileGetNum)
        squaresum = 0
        for i in range(FileGetNum):
            squaresum += InstantSpeed[i] ** 2
        squaresum = squaresum / FileGetNum
        deviation = math.sqrt((squaresum - average ** 2))
        cv = deviation / average
        if cv <= 0.2:
            stablevel = 1
        elif cv <= 0.4:
            stablevel = 0.9
        elif cv <= 0.6:
            stablevel = 0.8
        else:
            stablevel = 0.7
        print(stablevel)
        return stablevel