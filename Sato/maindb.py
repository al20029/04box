"""
*******************************************************************
***  File Name      : MainDB.py
***  Version        : V1.0
***  Designer       : 荒川 塁唯
***  Date           : 2022.7.3
***  Purpose       	: 計測されたWi-Fi情報を管理するデータベースを設定する.
***
*******************************************************************/
"""

import sqlite3
# データベースの作成
db = sqlite3.connect('main.db')
# SQLite3を操作するカーソルの作成
c = db.cursor()
# テーブルの作成 (Wi-Fi名, 平均速度, 安定性, 計測時刻)
c.execute('CREATE TABLE items(WiFiName text, AverageSpeed real, Stability integer, MeasurementTime datetime)')
c.close()