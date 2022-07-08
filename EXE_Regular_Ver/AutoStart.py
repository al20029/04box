from UI_main import UIMainProcess
import schedule
import datetime
import time 


def task():
    print(datetime)
    UIMainProcess.Regular()

task()

# schedule.every(1).hours.do(task)
schedule.every(60).seconds.do(task)
# schedule.every(10).seconds.do(task)

while 1:
    schedule.run_pending()
    time.sleep(1)