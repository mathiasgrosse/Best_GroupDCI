# Import datetime
from datetime import datetime
 
tday = str(datetime.now())
tday = datetime.strptime(tday, "%Y-%m-%d %H:%M:%S.%f")
unix_time = datetime.timestamp(tday)
print(unix_time)