import paramiko

class ssh():
    ##################変更点###################
    ## データの登録
    def ParamikoReg(WiFiName, AverageSpeed, Stability):
        # ###############
        # print("pramikoRegPhase")
        # print(type(WiFiName), WiFiName)
        # print(type(AverageSpeed), AverageSpeed)
        # print(type(Stability), Stability)
        # ################
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77',username='root',password='pracb2022',port = 50422)
        ssh = client.get_transport().open_session()
        argument = WiFiName + " " +  str(AverageSpeed) + " " +  str(Stability)
        # client.exec_command("python3 MainManagementWiFi.py"  + " 1 " + argument)
        stdin, stdout, stderr = client.exec_command("python3 MainManagementWiFi.py"  + " 1 " + argument)
        # print(stderr.read().decode('utf-8'))
        print(stdout.read().decode('utf-8'))
        # print(stdout.read())
        client.close()

    ## 過去データの取得
    def ParamikoGetPast(WiFiName):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77',username='root',password='pracb2022',port = 50422)
        ssh = client.get_transport().open_session()
        argument = WiFiName
        stdin, stdout, stderr = client.exec_command("python3 MainManagementWiFi.py" + " 2 " + argument)
        # print(stdout.read().decode('utf-8'))
        ######変更点######
        ReturnValue = stdout.read().decode('UTF-8').split()
        BestAverageSpeed = ReturnValue[0]
        BestStability = ReturnValue[1]
        client.close()
        return BestAverageSpeed, BestStability
        ##################

    ## リアルタイムデータの取得
    def ParamikoGetReal(WiFiList):

        WiFiList.append("test78")

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77',username='root',password='pracb2022',port = 50422)
        ssh = client.get_transport().open_session()
        argument = " " + str(len(WiFiList)) + " " + " ".join(WiFiList)
        stdin, stdout, stderr = client.exec_command("python3 MainManagementWiFi.py"+ " 3 " + argument)
        # print(stdout.read().decode('utf-8'))
        ReturnValue = stdout.read().decode('UTF-8').splitlines()
        # ReturnValue = stdout.read().split('\n')

        ######変更点######
        print("GetReturn")
        print(ReturnValue)
        WiFiName = list()
        AverageSpeed = list()
        Stability = list()
        print("Data:")
        for s in ReturnValue:
            # print(s)
            Spl_s = s.split()
            WiFiName.append(Spl_s[0])
            AverageSpeed.append(Spl_s[1])
            Stability.append(Spl_s[2])
        print("GetList")
        print(WiFiName)
        print(AverageSpeed)
        print(Stability)
        # print(stdout.read())
        client.close()
        return WiFiName, AverageSpeed, Stability
        ##################
    ###########################################