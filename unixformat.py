# importing datetime module
import datetime
import time
 
# assigned regular string date
date_time = datetime.datetime(2023, 1, 26, 15, 20)
 
 # print regular python date&time
print("date_time =>",date_time)

 
# displaying unix timestamp after conversion
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))

from datetime import timedelta
import datetime
import time
from datetime import datetime
past_date1 = time - timedelta(days=189)
print(past_date1)    


