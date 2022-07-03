"""
*******************************************************************
***  File Name      : ServerSocket.py
***  Version        : V1.0
***  Designer       : 荒川 塁唯
***  Date           : 2022.7.3
***  Purpose       	: Socket通信を行う際の, サーバー側の流れを定義する.
***
*******************************************************************/
"""

import socket

ip_address = '160.16.141.77'
port = 50422
buffer_size = 4092

# Socketの作成
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IP Adress とPort番号をソケット割り当てる
    s.bind((ip_address, port))
    # Socketの待機状態
    s.listen(5)
    # while Trueでクライアントからの要求を待つ
    while True:
        # 要求があれば接続の確立とアドレス、アドレスを代入
        conn, addr = s.accept()
        # データを受信する
        data = conn.recv(buffer_size)
        print('data-> {}, addr->{}'.format(data, addr))
        # データを送信する
        conn.sendall(b'I received the data correctly.')