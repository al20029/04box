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
import datetime

class ManagementWiFi:
 
    """
    *******************************************************************
    ***  Function Name      : Register
    ***  Designer           : 荒川 塁唯
    ***  Date               : 2022.6.21
    ***  Function       	: 計測されたWi-Fi情報を, Wi-Fi情報管理に登録する.
    ***  Return             : 
    ***
    *******************************************************************/
    """

    # 計測データの登録
    def RegisterData(WiFiName, AverageSpeed, Stability):

        ###########デバッグ用########
        print(type(WiFiName), WiFiName)
        print(type(AverageSpeed), AverageSpeed)
        print(type(Stability), Stability)
        #############################

        # 計測時刻の取得
        MeasurementTime = datetime.datetime.now()

        # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        
        # SQLite3を操作するカーソルの作成
        c = db.cursor()

        # 登録
        c.execute('INSERT INTO items (WiFiName, AverageSpeed, Stability, MeasurementTime)values(?,?,?,?)', [WiFiName, AverageSpeed, Stability, MeasurementTime])
        # テスト
        c.execute('SELECT * FROM items')     
        for row in c:
            print(row)
            db.commit()
        c.close()

    """
    *******************************************************************
    ***  Function Name  : SendPastData
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Function      	: Wi-Fi情報管理にある過去のWi-Fiデータの代表値を, UI処理部に送る.
    ***  Return         : 代表平均速度, 代表安定性 
    ***
    *******************************************************************/
    """

    # 過去データの送信
    def SendPastData(WiFiName):

        # データベースの作成（仮）
        db = sqlite3.connect('main.db')
        db.row_factory = sqlite3.Row

        # SQLite3を操作するカーソルの作成
        c = db.cursor()

        # 平均速度, 平均安定性の定義
        SumAverageSpeed = 0
        SumStability = 0
        n = 0
        BestAverageSpeed = 0
        BestStability = 0

        # データ検索
        c.execute('SELECT * FROM items WHERE (WiFiName == ?)', (WiFiName))
        for row in c:   
            if row[0] == WiFiName: 
                print(row[0], row[1], row[2])
                SumAverageSpeed = SumAverageSpeed + row[1]
                SumStability = SumStability + row[2]
                n = n + 1
        c.close()
        BestAverageSpeed = SumAverageSpeed / n
        BestStability = SumStability / n
        print(BestAverageSpeed, BestStability)

    """
    *******************************************************************
    ***  Function Name  : SendRealtimeData
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Function      	: 定期計測時に, 他に計測された一時間以内の接続可能なWi-Fi情報の代表値を, 比較処理部に返す.
    ***  Return         :  
    ***
    *******************************************************************/
    """

    # リアルタイムデータの送信    
    def SendRealtimeData(CanConnectWiFiName):

        # 計測時刻の取得
        ####変更点######
        MeasurementTime = datetime.datetime.now() - datetime.timedelta(hours = 1)
        ################

        # データベースの作成
        db = sqlite3.connect('main.db')
        db.row_factory = sqlite3.Row

        # listの宣言
        SumAverageSpeed = [0]*len(CanConnectWiFiName) # Wi-Fi名ごとの平均速度の和
        SumStability =  [0]*len(CanConnectWiFiName) # Wi-Fi名ごとの安定性の和
        BestAverageSpeed = [0]*len(CanConnectWiFiName)
        BestStability = [0]*len(CanConnectWiFiName)
        count = [0]*len(CanConnectWiFiName)

        # SQLite3を操作するカーソルの作成
        c = db.cursor()
        # データ検索
        for i in range(len(CanConnectWiFiName)):
            c.execute('SELECT * FROM items WHERE (MeasurementTime >= ?) AND (WiFiName == ?)', (MeasurementTime, CanConnectWiFiName[i]))
            # 直近一時間の計測データの探索
            for row in c:
                print(row[0], row[1], row[2])
                for j in range(len(CanConnectWiFiName)):
                    if row[0] == CanConnectWiFiName[j]:
                        SumAverageSpeed[j] = SumAverageSpeed[j] + row[1]
                        SumStability[j] = SumStability[j] + row[2]
                        count[j] = count[j] + 1
        for k in range(len(CanConnectWiFiName)):
            if count[k] != 0:
                BestAverageSpeed[k] = SumAverageSpeed[k] / count[k]
                BestStability[k] = SumStability[k] / count[k]
                print(CanConnectWiFiName[k], BestAverageSpeed[k], BestStability[k])
        c.close()