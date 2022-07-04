# リアルタイムデータの送信    
# def SendRealtimeData(MeasurementTime):
class RealTimeTest:
    def SendRealtimeData(): 
        # データベースの作成（仮）
        # db = sqlite3.connect('main.db')
        # db.row_factory = sqlite3.Row

        # listの宣言
        list1 = [] # Wi-Fi名, 平均速度, 安定性の二次元配列
        list2 = [] # 同じWi-Fi名ごとの配列
        SumRow1 = [] #同じWi-Fi名ごとの平均速度の合計     
        SumRow2 = [] #同じWi-Fi名ごとの安定性の合計
        BestRow1 = [] #同じWi-Fi名ごとの平均速度の平均値
        BestRow2 = [] #同じWi-Fi名ごとの安定性の平均値
        SameName = [] #同じWi-Fi名ごとのデータ数
        # i = 0
        # l = 0
        m = 0
        
        # # SQLite3を操作するカーソルの作成
        # c = db.cursor()
        # # データ検索
        # c.execute('SELECT * FROM items')
        # 直近一時間の計測データの探索
        # for row in c:
        #     if row[3].date == MeasurementTime.date:
        #         if row[3].datetime.hour > MeasurementTime.hour - 1:
        #             list1[i][0] = row[0]
        #             list1[i][1] = row[1]
        #             list1[i][2] = row[2]
        #             i = i+1
        # c.close()
        # 同じWi-Fi名ごとのリスト格納
        for test in range(20):
            if test % 4 == 0:
                list1[test][0] = "a"
            if test % 4 == 1:
                list1[test][0] = "b"
            if test % 4 == 2:
                list1[test][0] = "c"
            if test % 4 == 3:
                list1[test][0] = "d"
            list1[test][1] = test * 10 % 3 + 1
            list2[test][2] = test + 4
        for j in range(20):
            list2[j] = list1[j][0]
            SumRow1[j] = list1[j][1]
            SumRow2[j] = list1[j][2]
            SameName[j-m] = 1
            for k in range(j):
                # 同じWi-Fi名のリストがあった時の処理
                if list2[j] == list2[k]:
                    SumRow1[k] = SumRow1[k] + list[j][1]
                    SumRow2[k] = SumRow2[k] + list[j][2]
                    SameName[k] = SameName[k] + 1
                    del SameName[j-m]
                    m = m + 1
        for n in range(len(SameName)):
            BestRow1[n] = SumRow1[n] / SameName[n]
            BestRow2[n] = SumRow2[n] / SameName[n]    
            print(BestRow1[n], BestRow2[n])
        # return BestRow1, BestRow2