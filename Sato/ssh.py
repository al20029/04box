import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect(hostname = '160.16.141.77',username='root',password='pracb2022',port = 22)
ssh = client.get_transport().open_session()
stdin, stdout, stderr = client.exec_command("python3 hello.py")
client.close()
