import os
import datetime

menu = True
while menu == True:
    print("(1) - #Display Time")
    print("(2) - #Display Time in Unix")
    print("(3) - #task")
    print("(4) - #task")
    print("(5) - #task")
    print("(6) - #task")
    print("(7) - #task")
    print("(8) - #task")
    choice = input("ENTER CHOICE(1-8):")

    # Display time (Mathias)   
    if choice == "1":
        current_time = datetime.datetime.now().time()
        Display_time = current_time.strftime("%H:%M:%S")
        print(Display_time)
    # Time in Unix (Giulio)
    elif choice == "2":
        tday = str(datetime.datetime.now())
        tday = datetime.datetime.strptime(tday, "%Y-%m-%d %H:%M:%S.%f")
        unix_time = datetime.datetime.timestamp(tday)
        print(unix_time)
    elif choice == "3":
        # import datetime
        from datetime import datetime

        # date input
        dateinput = input("Enter a Date (DD.MM.YYYY): ")

        # output datetime data type
        print(datetime.strptime(dateinput, "%d.%m.%Y"))