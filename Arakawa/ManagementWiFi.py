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

import sqlite3
import numpy as np
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
        # テーブルの作成
        # c.execute('CREATE TABLE items(WFN text, IPA integer, AS real, S integer, MT datetime)')
        # 登録
        c.execute('INSERT INTO items (WiFiName, AverageSpeed, Stability, MeasureTime)values(?,?,?,?)',[WiFiName, AverageSpeed, Stability, MeasureTime])
        db.commit()
        c.close()
        #済

    """
    *******************************************************************
    ***  Func Name      : SendPastData
    ***  Version        : V1.0
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: Wi-Fi情報管理にある過去のWi-Fiデータを, UI処理部に送る.
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
        # テーブルの作成
        # c.execute('CREATE TABLE items(WFN text, IPA integer, AS real, S integer, MT integer)')

        # リストを定義
        list1 = np.zeros([1,3])

        # データ検索
        c.execute('SELECT * FROM items')
        for row in c:   
            if row[0] == WiFiName: 
                print(row[0], row[1], row[2])
                list1[0].append(row[0])
                list1[1].append(row[1])
                list1[2].append(row[2])
        c.close()
        print(list1[0],list[1],list[2])
        return list1
        #済

    """
    *******************************************************************
    ***  Func Name      : BestValue
    ***  Version        : V1.0
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: Wi-Fi情報管理にあるデータから, リアルタイムデータとの比較に用いるデータの代表値を計算し, SendRealtimeDataクラスに返す.
    ***
    *******************************************************************/
    """

    # 代表値の計算
    def CalculateBestValue(WiFiName):
       # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        # SQLite3を操作するカーソルの作成
        c = db.cursor()
        # データ検索
        c.execute('SELECT * FROM items where WiFiName = WFN')

        # 計算
        BestValue = 1
        return BestValue

    """
    *******************************************************************
    ***  Func Name      : SendRealtimeData
    ***  Version        : V1.0
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: 定期計測時に, 同時刻に計測された各Wi-Fiの代表値を比較処理部に返す.
    ***
    *******************************************************************/
    """

    # リアルタイムデータの送信    
    # def SendRealtimeData(BestValue):
    #     WiFiName = 1
    #     return WiFiName, BestValue