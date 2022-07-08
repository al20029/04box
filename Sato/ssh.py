import paramiko

class ssh():
    ##################変更点###################
    ## データの登録
    def ParamikoReg(WiFiName, AverageSpeed, Stability):
        ###############
        print("pramikoRegPhase")
        print(type(WiFiName), WiFiName)
        print(type(AverageSpeed), AverageSpeed)
        print(type(Stability), Stability)
        ################
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77',username='root',password='pracb2022',port = 50422)
        ssh = client.get_transport().open_session()
        argument = WiFiName + " " +  str(AverageSpeed) + " " +  str(Stability)
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
        print(stdout.read().decode('utf-8'))
        client.close()

    ## リアルタイムデータの取得
    def ParamikoGetReal(WiFiList):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77',username='root',password='pracb2022',port = 50422)
        ssh = client.get_transport().open_session()
        argument = " " + str(len(WiFiList)) + " " + " ".join(WiFiList)
        stdin, stdout, stderr = client.exec_command("python3 MainManagementWiFi.py"+ " 3 " + argument)
        print(stdout.read().decode('utf-8'))
        # print(stdout.read())
        client.close()
    ###########################################