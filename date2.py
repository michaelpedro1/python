import datetime
import random
import time

def random_date(start, end):
    date_format="%m/%d/%Y"
    start=time.mktime(time.strptime(start, date_format))
    end=time.mktime(time.strptime(end, date_format))

    random_time=start+random.random()*(end-start)

    return time.strftime(date_format, time.localtime(random_time))

print('random date ', random_date('04/01/2025', '04/25/2025'))    
