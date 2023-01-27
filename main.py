from datetime import datetime
import calendar

year = datetime.now() #int(input("Enter the year: ")) 
year = int(year.strftime("%Y"))

play = True

while play:
    #Checking if current year is a leap year
    if calendar.isleap(year):
        print(year,"is a leap year")
        play = False
    else:
        print(year,"is not a leap year")
        play = False
    #Checking how much time until the next leap year left
        next_leap_year = year
        while calendar.isleap(next_leap_year) != True:
            next_leap_year += 1
        print(next_leap_year - year, "year(s) left until the next leap year")
        
