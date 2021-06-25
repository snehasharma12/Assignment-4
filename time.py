import time
import datetime
time = datetime.datetime.now()
current_time = time.strftime("%H:%M:%S")
date = datetime.date.today()
day = datetime.date.today()
current_day = day.strftime("%A")
print("Time: ", current_time)
print("date: ", date)
print("day: ", current_day)
