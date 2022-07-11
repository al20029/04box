"""
*******************************************************************
***  File Name      : ssh.py
***  Version        : V1.0
***  Designer       : 
***  Date           : 2022.6.14
***  Purpose       	: 
***
*******************************************************************/
"""

import paramiko

class ssh():

    """
    *******************************************************************
    ***  Function Name  : ParamikoReg
    ***  Version        : V1.0
    ***  Designer       : 
    ***  Date           : 2022.6.21
    ***  Purpose       	: 
    ***
    *******************************************************************/
    """

    ## データの登録
    def ParamikoReg(WiFiName, AverageSpeed, Stability):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77',username = 'root', password = 'pracb2022', port = 50422)
        ssh = client.get_transport().open_session()
        argument = WiFiName + " " +  str(AverageSpeed) + " " +  str(Stability)
        stdin, stdout, stderr = client.exec_command("python3 MainManagementWiFi.py"  + " 1 " + argument)
        print(stdout.read().decode('utf-8'))
        client.close()

    """
    *******************************************************************
    ***  Function Name  : ParamikoGetPast
    ***  Version        : V1.0
    ***  Designer       : 
    ***  Date           : 2022.6.21
    ***  Purpose       	: 
    ***
    *******************************************************************/
    """

    ## 過去データの取得
    def ParamikoGetPast(WiFiName):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77', username = 'root', password = 'pracb2022', port = 50422)
        ssh = client.get_transport().open_session()
        argument = WiFiName
        stdin, stdout, stderr = client.exec_command("python3 MainManagementWiFi.py" + " 2 " + argument)
        ReturnValue = stdout.read().decode('UTF-8').split()
        AverageSpeed = float(ReturnValue[1])
        Stability = float(ReturnValue[2])
        client.close()
        return AverageSpeed, Stability

    """
    *******************************************************************
    ***  Function Name  : ParamikoGetReal
    ***  Version        : V1.0
    ***  Designer       : 
    ***  Date           : 2022.6.21
    ***  Purpose       	: 
    ***
    *******************************************************************/
    """

    ## リアルタイムデータの取得
    def ParamikoGetReal(WiFiList):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname = '160.16.141.77', username = 'root', password = 'pracb2022', port = 50422)
        ssh = client.get_transport().open_session()
        argument = " " + str(len(WiFiList)) + " " + " ".join(WiFiList)
        stdin, stdout, stderr = client.exec_command("python3 MainManagementWiFi.py"+ " 3 " + argument)
        ReturnValue = stdout.read().decode('UTF-8').splitlines()

        WiFiName = list()
        AverageSpeed = list()
        Stability = list()

        #サーバに目的のWiFiデータが存在しない場合
        if ReturnValue == "":
            return 0, WiFiName, AverageSpeed, Stability
        
        print("Data:")
        for s in ReturnValue:
            Spl_s = s.split()
            WiFiName.append(Spl_s[0])
            AverageSpeed.append(float(Spl_s[1]))
            Stability.append(float(Spl_s[2]))
        client.close()
        return 1, WiFiName, AverageSpeed, Stability