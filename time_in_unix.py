# Import datetime
import datetime
 
tday = str(datetime.datetime.now())
tday = datetime.datetime.strptime(tday, "%Y-%m-%d %H:%M:%S.%f")
unix_time = datetime.datetime.timestamp(tday)
print(unix_time)