from UI_main import UIMainProcess
import schedule
import datetime
import time 

UIMainProcess.Regular()
def task():
    print(datetime)
    UIMainProcess.Regular()

schedule.every(1).hours.do(task)
# schedule.every(10).seconds.do(task)

while 1:
    schedule.run_pending()
    time.sleep(1)