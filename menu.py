import os
menu = True
while menu == True:
    print("(1) - #task")
    print("(2) - #task")
    print("(3) - #task")
    print("(4) - #task")
    print("(5) - #task")
    print("(6) - #task")
    print("(7) - #task")
    print("(8) - #task")
    choice = input("ENTER CHOICE: ")

#############################   
    if choice == "1":
        print("hi")



############################      is able to display the current time
    elif choice == "2":
        print("there")



###########################        is able to display the current time in UNIX format
    elif choice == "3":
        print("")



###########################         is able to take user input and convert it to a datetime datatype
    elif choice == "4":
        print("")



#############################        is able to calculate the time from today until a given date, outputs the delta
    if choice == "5":
        print()



############################         is able to output the delta in full, only seconds, only day, only years
    elif choice == "6":
        var = input("")
        print("")



###########################           is able to display a chosen months calendar (import calendar)
    elif choice == "7":
        var = input("")
        print("")



###########################          is able to output  if current year is a leapyear
    elif choice == "8":
        


###########################           is able to output how much time until the next leapyear
    elif choice == "9":
        var = input("")
        print("")



###########################            is able to output a random joke (yes.)
    elif choice == "10":
        import random
        jokes = ["What is Forrest Gump´s e-mail password? 1forrest1" , 
        "Did you hear about the guy who invented the knock knock joke? He won the 'no-bell' price", 
        "What´s red and bad for your teeth? A brick","What kind of tea is hard to swallow? Reality", "What´s the most terrifying word in nuclear physics? Oooops ",
        "Ebay is so useless. I tried to look up lighters and all they had were 13 765 matches"]
        
         print(random.randint(0,(jokes.__len__()-1)))
         print(jokes[random.randint(0,(jokes.__len__()-1))])
    
    

        menu = False
        exit("bye")
###########################            one additional surprise feature related to time or date
    else:
        print("")
