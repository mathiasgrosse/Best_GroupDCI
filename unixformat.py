# importing datetime module

import datetime
import time
from datetime import timedelta

####  display the current time in UNIX format

# assigned regular string date
date_time = datetime.datetime(2023, 1, 26, 15, 20)
 
 # print regular python date&time
print("date_time =>",date_time)

 
# displaying unix timestamp after conversion
print("unix_timestamp => ",
 (time.mktime(date_time.timetuple())))

#######
#######    calculate the time from today until a given date, outputs the delta
time_now = datetime.datetime.now()
past_date1 = time_now - timedelta(days=189)
print(past_date1)   

# What day will it be after 180 days
future_date2 = time_now + timedelta(days=189)
print(future_date2)

# What day would it have been 150 days ago
past_date1 = time_now - timedelta(days=189)
print(past_date1)



