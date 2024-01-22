import datetime
from datetime import date, datetime
today = date.today()
rightnow = datetime.now()

day = today.day
month = today.month
year = today.year

current_time = rightnow.strftime('%H:%M')
current_day = f'{day}/{month}/{year}'
logdate = f'{current_day} {current_time}'
