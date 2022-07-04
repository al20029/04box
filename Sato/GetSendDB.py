import subprocess

class GetSendDB:
    def download():
        print("pracb2022と入力してください")
        subprocess.run('FromServer', encoding='utf-8', shell=True)

    def upload():
        print("pracb2022と入力してください")
        subprocess.run('ToServer', encoding='utf-8', shell=True)


# GetSendDB.upload()
# GetSendDB.download()