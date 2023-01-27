import datetime
import pytz

#surprise feature: get time on the opposit side of the world.

current_time = datetime.datetime.now()

# convert current time to opposite timezone (12 hours difference)
opposite_time = current_time.astimezone(pytz.timezone('Etc/GMT-12'))

print(opposite_time.strftime("%Y-%m-%d , %H:%M:%S"))