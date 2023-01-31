import os
import datetime

menu = True
while menu == True:
    print("(1) - #Display Time")
    print("(2) - #Display Time in Unix")
    print("(3) - #Convert to a datetime datatype")
    print("(4) - #Checking if current year is a leap year and how much time until the next leap year left")
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
        # import datetime (Spencer)
        from datetime import datetime

        # date input
        dateinput = input("Enter a Date (DD.MM.YYYY): ")

        # output datetime data type
        print(datetime.strptime(dateinput, "%d.%m.%Y"))
    # Kyrylo
    elif choice == "4":
        from datetime import datetime
        import calendar
        year = datetime.now() #int(input("Enter the year: ")) 
        year = int(year.strftime("%Y"))

        play = True
        while play:
    # Checking if current year is a leap year (Kyrylo)
            if calendar.isleap(year):
                print(year,"is a leap year")
                play = False
            else:
                print(year,"is not a leap year")
                play = False
    # Checking how much time until the next leap year left (Kyrylo)
                next_leap_year = year
                while calendar.isleap(next_leap_year) != True:
                    next_leap_year += 1
                    print(next_leap_year - year, "year(s) left until the next leap year")