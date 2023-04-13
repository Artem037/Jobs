import sys
import datetime
import schedule


def job():
    if dp:
        time1, time2 = dp.split('-')
        if not (datetime.datetime.now().hour in range(int(time1), int(time2) + 1)):
            for i in range(datetime.datetime.now().hour % 12):
                print(msg)
    else:
        for i in range(datetime.datetime.now().hour % 12):
            print(msg)


msg = 'Ку'
dp = ''
for arg in sys.argv[1:]:
    arg1, val = arg.split('=')
    if arg1 == 'msg':
        msg = val
    elif arg1 == 'dp':
        dp = val

schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()
