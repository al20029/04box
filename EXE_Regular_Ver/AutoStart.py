"""
*******************************************************************
***  File Name      : AutoStart.py
***  Version        : V1.1
***  Designer       : 太田峻輔
***  Date           : 2022.6.14
***  Purpose       	: PC起動時から1時間毎にアプリを自動起動する.
***
*******************************************************************/
"""

from UI_main import UIMainProcess
import schedule
import datetime
import time 

def task():
    print(datetime)
    UIMainProcess.Regular()

task()

schedule.every(1).hours.do(task)

while 1:
    schedule.run_pending()
    time.sleep(1)