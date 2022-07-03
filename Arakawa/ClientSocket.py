"""
*******************************************************************
***  File Name      : ClientSocket.py
***  Version        : V1.0
***  Designer       : 荒川 塁唯
***  Date           : 2022.7.3
***  Purpose       	: Socket通信を行う際の, クライアント側の流れを定義する.
***
*******************************************************************/
"""

import socket

ip_address = '160.16.141.77'
port = 50422
buffer_size = 4092

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバーに接続を要求する
    s.connect((ip_address, port))
    # データを送信する
    s.sendall(b'I sent a message.')
    # サーバーからのデータを受信
    data = s.recv(buffer_size)

    print(data.decode())