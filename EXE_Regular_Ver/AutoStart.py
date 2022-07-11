"""
*******************************************************************
***  File Name      : AutoStart.py
***  Version        : V1.0
***  Designer       : 
***  Date           : 2022.6.14
***  Purpose       	: 
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