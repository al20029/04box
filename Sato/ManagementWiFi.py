"""
*******************************************************************
***  File Name      : ManagementWiFi.py
***  Version        : V1.0
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.21
***  Purpose       	: 計測されたWi-Fi情報を管理する.
***
*******************************************************************/
"""

# from multiprocessing import _JoinableQueueType
import sqlite3
# import datetime
# import numpy as np
# from testdb import *
# from UI_main import UI_main
# from MainMeasurement import MainMeasurement

class ManagementWiFi:
 
    """
    *******************************************************************
    ***  Func Name      : Register
    ***  Version        : V1.0
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: 計測されたWi-Fi情報を, Wi-Fi情報管理に登録する.
    ***
    *******************************************************************/
    """

    # 計測データの登録
    def RegisterData(WiFiName, AverageSpeed, Stability, MeasureTime):
    # def RegisterData():

        # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        
        # SQLite3を操作するカーソルの作成
        c = db.cursor()

        # 登録
        c.execute('INSERT INTO items (WiFiName, AverageSpeed, Stability, MeasureTime)values(?,?,?,?)',[WiFiName, AverageSpeed, Stability, MeasureTime])
        # テスト
        c.execute('SELECT * FROM items')     
        for row in c:
            print(row)
            db.commit()
        c.close()

    """
    *******************************************************************
    ***  Func Name      : SendPastData
    ***  Version        : V1.0
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: Wi-Fi情報管理にある過去のWi-Fiデータの代表値を, UI処理部に送る.
    ***
    *******************************************************************/
    """

    # 過去データの送信
    def SendPastData(WiFiName, AveregeSpeed, Stability):
        # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        db.row_factory = sqlite3.Row

        # SQLite3を操作するカーソルの作成
        c = db.cursor()

        # 平均速度, 平均安定性の定義
        SumAverageSpeed = 0
        SumStability = 0
        n = 0
        BestAvrageSpeed = 0
        BestStability = 0
        # データ検索
        c.execute('SELECT * FROM items')
        for row in c:   
            if row[0] == WiFiName: 
                print(row[0], row[1], row[2])
                SumAverageSpeed = SumAverageSpeed + row[1]
                SumStability = SumStability + row[2]
                n = n + 1
        c.close()
        BestAvrageSpeed = SumAverageSpeed / n
        BestStability = SumStability / n
        print(BestAvrageSpeed, BestStability)
        return BestAvrageSpeed, BestStability

    """
    *******************************************************************
    ***  Func Name      : SendRealtimeData
    ***  Version        : V1.0
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: 定期計測時に, 他に計測された直近10個のWi-Fi情報を比較処理部に返す.
    ***
    *******************************************************************/
    """

    # リアルタイムデータの送信    
    def SendRealtimeData(MeasurementTime):
        # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        db.row_factory = sqlite3.Row

        # listの宣言  
        list1 = [] # Wi-Fi名, 平均速度, 安定性の二次元配列
        list2 = [] # 直近10個のデータの二次元配列
        i = 0
        k = 0

        # SQLite3を操作するカーソルの作成
        c = db.cursor()
        # データ検索
        c.execute('SELECT * FROM items WHERE MeasurementTime-3600 < ?', MeasurementTime)
        # 直近一時間の計測データの探索
        for row in c:
            if row[3].date == MeasurementTime.date:
                if row[3].datetime.hour > MeasurementTime.hour - 1:
                    list1[i] = [row[0],row[1],row[2]]
                    i = i+1
        c.close()
        if i > 10:
            k = 10
        for j in range(k):
            list2[j] = list1[i-k]
            print(list2[j])
        return list2