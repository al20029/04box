import sqlite3
# データベースの作成
db = sqlite3.connect('main.db')
# SQLite3を操作するカーソルの作成
c = db.cursor()
# テーブルの作成
c.execute('CREATE TABLE items(WiFiName text, AverageSpeed real, Stability integer, MeasureTime datetime)')
c.close()