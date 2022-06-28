"""
*******************************************************************
***  File Name      : ManagementWi-Fi.py
***  Version        : V1.0
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.21
***  Purpose       	: 計測されたWi-Fi情報を管理する.
***
*******************************************************************/
"""

import sqlite3

class ManagementWiFi:

    # 計測データの登録
    def RegisterData(WiFiName, IPAddress, AverageSpeed, Stability, MeasureTime):
        # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        # SQLite3を操作するカーソルの作成
        c = db.cursor()
        # テーブルの作成
        c.execute('CREATE TABLE items(WFN text, IPA integer, AS real, S integer, MT integer)')

        # 登録
        c.excute = ('INSERT INTO items values(WiFiName, IPAddress, AverageSpeed, Stability, MeasureTime)')
        db.comitt()
        c.close()

    # 過去データの送信
    def SendPastData(WFN, IPA, AS, S):
        # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        db.row_factory = sqlite3.Row
        c = db.cursor()

        # データ検索
        c.execute('SELECT * FROM items where WiFiName = WFN')
        for row in c:    
           print(row[0], row[1], row[2], row[3])
        WiFiName = row[0]
        IPAddress = row[1]
        AverageSpeed = row[2]
        Stability = row[3]


    # リアルタイムデータの送信    
    def SendRealtimeData(BestValue):
        WiFiName = 1
        return WiFiName, BestValue

    # 代表値の計算
    def BestValue():
       # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        # SQLite3を操作するカーソルの作成
        c = db.cursor()
        # テーブルの作成
        c.execute('CREATE TABLE items(id integer, name text)')

        # 計算
        BestValue = 1
        return BestValue