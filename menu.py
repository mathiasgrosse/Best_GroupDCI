import os
import datetime
import random
import time
from datetime import timedelta
import calendar
menu = True
while menu == True:
    print("(1) - #Display Time")
    print("(2) - #Display Time in Unix")
    print("(3) - #Convert to a datetime datatype")
    print("(4) - #Checking if current year is a leap year and how much time until the next leap year left")
    print("(5) - #output the delta in full, only seconds, only day, only years")
    print("(6) - #Output a random joke")
    print("(7) - #Print a calendar")
    print("(8) - #Exit")

    
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
    
    # import datetime (Spencer)    
    elif choice == "3":
        from datetime import datetime

        # date input
        dateinput = input("Enter a Date (DD.MM.YYYY): ")

        # output datetime data type
        print(datetime.strptime(dateinput, "%d.%m.%Y"))
    
    # Kyrylo
    elif choice == "4":
        from datetime import datetime
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
    
    # calculate the time from today until a given date, outputs the delta(Ammara)
    elif choice == "5":
        time_now = datetime.datetime.now()
        past_date1 = time_now - timedelta(days=189)
        print(past_date1)   

        # What day will it be after 180 days
        future_date2 = time_now + timedelta(days=189)
        print(future_date2)

        # What day would it have been 150 days ago
        past_date1 = time_now - timedelta(days=189)
        print(past_date1)  
        
    # Output a random jokes (Darlene)
    elif choice == "6":
        jokes = ["What is Forrest Gump´s e-mail password? 1forrest1" , 
        "Did you hear about the guy who invented the knock knock joke? He won the 'no-bell' price", 
        "What´s red and bad for your teeth? A brick","What kind of tea is hard to swallow? Reality", "What´s the most terrifying word in nuclear physics? Oooops ",
        "Ebay is so useless. I tried to look up lighters and all they had were 13 765 matches"]
        
        print(random.randint(0,(jokes.__len__()-1)))
        print(jokes[random.randint(0,(jokes.__len__()-1))])
    
    # Print a chosen calendar (Yaroslav)
    elif choice == "7":
        year = int(input("Please, type one year (yyyy): "))
        month =  int(input("Please, type one month (mm): "))
        print(f"{calendar.month(year, month)}")
    
    elif choice == "8":
        menu = False