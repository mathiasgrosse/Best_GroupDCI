import os
import datetime

menu = True
while menu == True:
    print("(1) - #Display Time")
    print("(2) - #task")
    print("(3) - #task")
    print("(4) - #task")
    print("(5) - #task")
    print("(6) - #task")
    print("(7) - #task")
    print("(8) - #task")
    choice = input("ENTER CHOICE: (1-8)")

#############################   
    if choice == "1":
        current_time = datetime.datetime.now().time()
        Display_time = current_time.strftime("%H:%M:%S")
        print(Display_time)
    elif choice == "2":