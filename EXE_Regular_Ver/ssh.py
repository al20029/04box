"""
*******************************************************************
***  File Name      : ssh.py
***  Version        : V1.1
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.14
***  Purpose       	: Paramikoを利用し,サーバにsshで接続し,
                      サーバにあるPythonファイルを実行する
*******************************************************************/
"""

import paramiko

"""
*******************************************************************
***  Class Name     : ssh
***  Designer       : 荒川 塁唯
***  Date           : 2022.6.14
***  Purpose       	: Paramikoを利用し,サーバにsshで接続し,
                      サーバにあるPythonファイルを実行する
*******************************************************************/
"""

class ssh():

    """
    *******************************************************************
    ***  Function Name  : ParamikoReg
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: サーバにあるファイルを実行し，計測データをサーバに登録する．
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
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: サーバにあるファイルを実行し,Wi-Fi情報管理にあるデータから,
                          リアルタイムデータとの比較に用いるデータの代表値を計算する.
    ***  Return         : float AverageSpeed 平均速度
                          int Stability 安定性
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
    ***  Designer       : 荒川 塁唯
    ***  Date           : 2022.6.21
    ***  Purpose       	: サーバにあるファイルを実行し,Wi-Fi情報管理にあるデータから, 
                          リアルタイムデータとの比較に用いるデータの代表値を計算する.
    ***  Return         : String WiFiName Wi-Fi名
                          float AverageSpeed 平均速度
                          int Stability 安定性
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