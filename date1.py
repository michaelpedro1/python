from datetime import date, time, datetime

today=date.today()
print('today is on', today)
now=datetime.now()
print('the time is now', now)
print('dates component')
print('current year is', today.year ,'the current month', today.month)
print('the current day is', today.day)