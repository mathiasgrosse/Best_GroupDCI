import datetime

current_time = datetime.datetime.now().time()
Display_time = current_time.strftime("%H:%M:%S")
print(Display_time)