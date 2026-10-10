# Why do i want to build this thing?



# very simple, to track my habits, why do i want to track my habits?
# well looking at something that has a streak feels really motivating
# it's like you know you're trying your best because you see your streak

# this is very simple, what i'll do is first list what it does


# what im thinking is like a github type of block
# each cell is an empty cell the top most header is the month, then below it are
# cells, each cell indicates the day of the month

# design
# im thinking of using a library but i don't kow what thouhg
# i need to extract the current year and month and week using a library

# flow

"""
screen opens

he will see these decision_numbers

add a habit/task
log
see a specific habit streak
see all log

if he chooses a habit
-> prompt what habit
-> add that habit to data structure (later json)


if he chooses log
-> pick what habit (meditating, coding etc)
-> pick date (default is present)
-> then exits that page



if he chooses see a habit streak
-> pick what habit (meditating, coding etc)
-> logs for a specific habit will show up, with a month hearder below it are the weeks
and cells are below the weeks, each cell contains either an empty cell or an X inside it
X marks that the user did that habit for that day "im thinking of putting a color in the cell if it's possible"

if he chooses see all habit streak
-> all streak will be shown in the terminal, with a month hearder below it are the weeks
and cells are below the weeks, each cell contains either an empty cell or an X inside it
X marks that the user did that habit for that day


ALL HABITS WILL BE SHOWN IN the year 2026

there's a lot of features that can be added in this project but right now this is good


"""



""" 
TOOLS: 
rich + datetime/calendar + JSON

"""



""" 
DESIGN/FUNCTIONS:

everyhting runs on habit.py
NEEDS: RICH FOR STYLE

[1] Add a habit
[2] Log a habit
[3] See streak of a specific habit
[4] See all habit streak

EDGECASE: input asks for int, what if string is given?, is the nunmber in the range from 1  to 4

add_habit
    1. asks what habit
    2. stores that habit in dictionary (json for later)
    3. exits automatically

    EDGE CASE: input asks a string -> what if user inputs a number?

log_habit
    1. displayes all the habits with a number beside the habits 
    2. user picks one number
    3. asks to log it with the current date or custom date
        4,1. if custom date user is asked a specific month and day
        4.2 if current then it uses the current date
    5. adds those log data in a dictionary
    6. exits automatically
    EDGE CASE: input asks a number, what if user inputs a string?, is the asked date a valid date? like is it in the 
    range of 1 to 31 or 30 or 29 depending on the month?


- need to think about tyhe spacing, lets just agree to two spacing between each month
- the rows? 5 rows, 7 columns
output_one_habit_streak
    1. displayes all the habits with a number beside the habits 
    2. user picks one number
    3. full year strea for that habit will be shown
    4. prompts press eny key to exit
    5. exits if any keys are pressed

    EDECASE: is the nunmber in the range from 1  to n? depends how many habits are there

output_all_habit_streak
    3. full year streak for all the habits will be shown
    4. prompts press eny key to exit
    5. exits if any keys are pressed
"""

""" 
DATA STRUCTURE

- using a dictionary
{habit : {month:[3, 2, 4] , month: [4, 2]}}

sample
{coding: {3: [3, 4, 1, 2], 8: {}}, meditating: {september: {}}}

outer part is the habit - string
inner part is the month - integer
each month has an integer value, the day - integer

3 = march
8 = october
1 = january

you get the point
"""






""" 
Order to building it:
- setup my functions and flow for add_habit
- understand how rich works -> user console.print()
- understand how to get the current year, month, and day using a library called date/time?
- build the first flow, main and habit
"""

# ! ADD A BACK FEATURE

default_print = print

from rich import print
import time
import sys
from rich.prompt import Prompt
import calendar
import random

# TODO: Document
# TODO: Refactor (DRY)

# TODO: JSON FEATURE


def add_habit(habit_records):
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")
    while True:     
        # ask what habit to add (only string, dont accept empty string)
        try:
            print("[magenta bold]ADD A HABIT TO TRACK IT LATER![/magenta bold]")
            print("To exit the prompt type \"x\" without the double quotes")
            print("\'To add more than one habit separate them by spaces\'\n")

            # ask what habit to add (only string, dont accept empty string)
            habits = str(Prompt.ask("[light_cyan1 bold]Habit(s) [/light_cyan1 bold]")).split()
            if habits == []: 
                raise Exception("Input is empty!") 

            elif habits[0] == "x": # exit if the user inputs 'x'
                delete_lines(11)
                break
            
            else: # add the habit
                for habit in habits:
                    habit_records[habit] = {}
                delete_lines(11)
                break
        except:
            print("Input is [magenta bold]EMPTY![/magenta bold]")
            time.sleep(2)
            delete_lines(6)



def log_habit(habit_records, bright_colors): 
    from datetime import datetime
    
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n\n")

    # prevent the user from inputting anything if the habit_records is empty
    if not habit_records:
        print("There are no habits to log...")
        input("Press \'enter\' to continue..")
        delete_lines(9)

        return


    print("type \'x\' if you want to exit\n")

    # display all the habits
    print("[bold bright_blue]Habit(s):[/bold bright_blue]")
    key_habit_records_list = []
    for i, habit in enumerate(habit_records):
        key_habit_records_list.append(habit)
        bright_color = random.choice(bright_colors)
        print(f"[{bright_color}][{i}] {habit}[/{bright_color}]")

    print()

    # ask what habit to log
    while True:
        try:
            decision_number = str(Prompt.ask(f"[light_cyan1 bold]Pick a habit from [0 - {len(key_habit_records_list) - 1}] [/light_cyan1 bold]"))
            if decision_number == 'x': # exit the function
                delete_lines(13)
                return 
            else:
                decision_number = int(decision_number)

            if decision_number < 0 or decision_number > len(key_habit_records_list) - 1: # number does NOT ranges from 0 to the last habit index
                raise ValueError(f"decision_number is not valid, it should range only from 0 - {len(key_habit_records_list) - 1}")
            else:
                delete_lines(3 + len(key_habit_records_list))
                break
        except:
            print(f"Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to {len(key_habit_records_list) - 1}![/bold red]")
            time.sleep(2)
            delete_lines(2)

    # Adding a date to log the habit
    while True:
        try:
            date_decision = input("Manually input date [y/n]? ")

            if date_decision == 'x': # exit the function
                delete_lines(13)
                return 

            if date_decision == 'y': # manually input the month and day
                while True:
                    try:
                        month = input("Month [1 - 12]: ")

                        if month == 'x': # exit the function
                            delete_lines(13)
                            return 
                        else:
                            month = int(month) 


                        if month < 1 or month > 12:
                            raise ValueError("Invalid month input")
                        else:
                            delete_lines(1)
                            break
                    except:
                        print("Invalid [bold blue]month[/bold blue]!")
                        time.sleep(2)
                        delete_lines(2)

                
                total_days_in_month = calendar.monthrange(2026, month)[1] # get the total days in a month

                while True:
                    try:
                        # input the nth day of the month
                        day = input(f"Day [1 - {total_days_in_month}]: ")

                        if day == 'x': 
                            delete_lines(13)
                            return 
                        else:
                            day = int(day)

                        if day < 1 or day > total_days_in_month:
                            raise ValueError("Invalid day input")
                        else:
                            delete_lines(1)
                            break
                    except:
                        print("Invalid [bold blue]day[/bold blue]!")
                        time.sleep(2)
                        delete_lines(2)
                

                # log it
                habit = key_habit_records_list[decision_number]
                if month in habit_records[habit]: # month is already existing in the dictionary
                    habit_records[habit][month].add(day) # only add the day 
                else:
                    habit_records[habit][month] = {day} # create a month key and add the day inside a dictionary


                delete_lines(12)
                break

                    
            elif date_decision == 'n': # automatic date (current date)
                present_day = datetime.now().day
                present_month = datetime.now().month
                habit = key_habit_records_list[decision_number]

                if present_month in habit_records[habit]: # month is already existing in the dictionary
                    habit_records[habit][present_month].add(present_day) # only add the day 
                else:
                    habit_records[habit][present_month] = {present_day} # create a month key and add the day inside a dictionary

                delete_lines(10)
                break
            else:
                raise ValueError("date decision should be either a y/n")
            

        except:
            print("Input should either be a [bold blue]y[/bold blue] or [bold red]n[/bold red]!")
            time.sleep(2)
            delete_lines(2)
    


def output_one_habit_streak(habit_records, bright_colors):
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")


    # prevent the user from inputting anything if the habit_records is empty
    if not habit_records:
        print("There are no habits to display...")
        input("Press \'enter\' to continue..")
        delete_lines(9)
    
        return

    # display all the habits
    print("[bold bright_blue]Habit(s):[/bold bright_blue]")
    key_habit_records_list = []
    for i, habit in enumerate(habit_records):
        key_habit_records_list.append(habit)
        bright_color = random.choice(bright_colors)
        print(f"[{bright_color}][{i}] {habit}[/{bright_color}]")

    print()

    # ask what habit to display its streak (2026)
    while True:
        try:
            decision_number = Prompt.ask(f"[light_cyan1 bold]Pick a habit streak to display from [0 - {len(key_habit_records_list) - 1}] [/light_cyan1 bold]")

            if decision_number == "x": # exit the function
                delete_lines(13)
                return 
            else:
                decision_number = int(decision_number)


            if decision_number < 0 or decision_number > len(key_habit_records_list) - 1:
                raise ValueError(f"decision_number is not valid, it should range only from 0 - {len(key_habit_records_list) - 1}")
            else:
                delete_lines(3 + len(key_habit_records_list))
                break
        except:
            print(f"Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to {len(key_habit_records_list) - 1}![/bold red]")
            time.sleep(2)
            delete_lines(2)

    habit_key = key_habit_records_list[decision_number]

    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    days = {1: "Su", 2: "Mo", 3: "Tu", 4: "We", 5: "Th", 6: "Fr", 7: "Sa"}
    
    month = 1 # starting index for the month (January)
    cal = calendar.Calendar(firstweekday=6) # cal object, gives a lot of functions out of the box

    print(f"\n\n[bold hot_pink]{habit_key:^70}[/bold hot_pink]")
    print(f"\n{"2026":^70}\n")

    for i in range(4): # four rows total
                       # row1 = jan, feb, march 
                       # row2 = april, may, june
                       # row3 = july, august, september
                       # row4 = october, november, december

        print(f"{months[month]:^20}{months[month + 1]:^30}{months[month+2]:^20}")
        for i in range(3):
            print(f"{days[1]:^3}{days[2]:^3}{days[3]:^3}{days[4]:^3}{days[5]:^3}{days[6]:^3}{days[7]:^3}", end=f"{"":<4}")

        print()

        # month1, month2 and month3's values is a 2d array, each index is an array containing days in one row
        # [[0, 1, 2, 3], [4, 5, 6, 7]]
        month1 = cal.monthdayscalendar(2026, month) 
        month2 = cal.monthdayscalendar(2026, month + 1) 
        month3 = cal.monthdayscalendar(2026, month + 2) 


            
        for j in range(6):
            for k in range(7): # month1
                try:
                    if month1[j][k] != 0:
                        # highlight the specific date in this month
                        if month in habit_records[habit_key] and month1[j][k] in habit_records[habit_key][month]: 
                            print(f"[black on white]{month1[j][k]:^3}[/black on white]", end="")

                        else:
                            print(f"{month1[j][k]:^3}", end="")
                    else:
                        print(f"{" ":^3}", end="")
                except:
                    print(f"{"":^3}", end="")


            print(end="    ")

            for l in range(7): # month 2
                try:
                    if month2[j][l] != 0:
                        if month + 1 in habit_records[habit_key] and month2[j][l] in habit_records[habit_key][month + 1]:
                            print(f"[black on white]{month2[j][l]:^3}[/black on white]", end="")
                        else:
                            print(f"{month2[j][l]:^3}", end="")
                    else:
                        print(f"{" ":^3}", end="")
                except:
                        print(f"{" ":^3}", end="")

            print(end="    ")

            for m in range(7): # month 3
                try:
                    if month3[j][m] != 0:
                        if month + 2 in habit_records[habit_key] and month3[j][m] in habit_records[habit_key][month + 2]:
                            print(f"[black on white]{month3[j][m]:^3}[/black on white]", end="")
                        else:
                            print(f"{month3[j][m]:^3}", end="")
                    else:
                        print(f"{" ":^3}", end="")
                except Exception:
                        print(f"{" ":^3}", end="")

            print()


        month += 3
        print("\n\n")

    input("Press enter to continue")
    default_print("\033[2J]\033[3J]\033[H")

    return


def output_all_habit_streak(habit_records):
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")


    # check if there are habits to log
    if not habit_records:
        print("There are no habits to display...")
        input("Press \'enter\' to continue..")
        delete_lines(9)
    
        return

    print(f"\n{"2026":^70}\n")


    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    days = {1: "Su", 2: "Mo", 3: "Tu", 4: "We", 5: "Th", 6: "Fr", 7: "Sa"}
    month = 1
    cal = calendar.Calendar(firstweekday=6)


    # output all habits
    for habit_key in habit_records:
        print(f"\n\n[bold hot_pink]{habit_key:^70}[/bold hot_pink]")
        for i in range(4):
                # display months 1 to 3, 4 to 6 etc
                print(f"{months[month]:^20}{months[month + 1]:^30}{months[month+2]:^20}")
                # display Su Tu, We to Sa three times
                for i in range(3):
                    print(f"{days[1]:^3}{days[2]:^3}{days[3]:^3}{days[4]:^3}{days[5]:^3}{days[6]:^3}{days[7]:^3}", end=f"{"":<4}")
        
                print()

                # matrix of all the dates for a specific month
                month1 = cal.monthdayscalendar(2026, month)
                month2 = cal.monthdayscalendar(2026, month + 1)
                month3 = cal.monthdayscalendar(2026, month + 2)
        
                for j in range(6):

                    for k in range(7): # month1
                        try:
                            if month1[j][k] != 0:
                                if month in habit_records[habit_key] and month1[j][k] in habit_records[habit_key][month]:
                                    print(f"[black on white]{month1[j][k]:^3}[/black on white]", end="")
        
                                else:
                                    print(f"{month1[j][k]:^3}", end="")
                            else:
                                print(f"{" ":^3}", end="")
                        except:
                            print(f"{"":^3}", end="")
        
        
                    print(end="    ")
        
                    for l in range(7): # month 2
                        try:
                            if month2[j][l] != 0:
                                if month + 1 in habit_records[habit_key] and month2[j][l] in habit_records[habit_key][month + 1]:
                                    print(f"[black on white]{month2[j][l]:^3}[/black on white]", end="")
                                else:
                                    print(f"{month2[j][l]:^3}", end="")
                            else:
                                print(f"{" ":^3}", end="")
                        except:
                                print(f"{" ":^3}", end="")
        
                    print(end="    ")
        
                    for m in range(7): # month 3
                        try:
                            if month3[j][m] != 0:
                                if month + 2 in habit_records[habit_key] and month3[j][m] in habit_records[habit_key][month + 2]:
                                    print(f"[black on white]{month3[j][m]:^3}[/black on white]", end="")
                                else:
                                    print(f"{month3[j][m]:^3}", end="")
                            else:
                                print(f"{" ":^3}", end="")
                        except Exception:
                                print(f"{" ":^3}", end="")
        
                    print()
        
        
                month += 3
                print("\n\n")

        month = 1        
        
    input("Press enter to continue")
    default_print("\033[2J]\033[3J]\033[H")


def delete_lines(n):
    if n < 1: print("n should be greater than 0!")
    else:
        for i in range(n):
            sys.stdout.write("\033[1A") # move cursor up
            sys.stdout.write("\x1b[2K") # delete line

def delete_habit(habit_records, bright_colors):
    print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
    print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
    print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]\n")

    # check if there are habits to log
    if not habit_records:
        print("There are no habits to delete...")
        input("Press \'enter\' to continue..")
        delete_lines(9)
        return

    print("Delete a habit.\n\n")

    # display the habits
    print("[bold bright_blue]Habit(s):[/bold bright_blue]")
    key_habit_records_list = []
    for i, habit in enumerate(habit_records):
        key_habit_records_list.append(habit)
        bright_color = random.choice(bright_colors)
        print(f"[{bright_color}][{i}] {habit}[/{bright_color}]")
    
    print()

    # ask what habit to delete
    while True:
            try:
                decision_number = str(Prompt.ask(f"[light_cyan1 bold]Pick a habit to [bold red]delete[/bold red] from [0 - {len(key_habit_records_list) - 1}] [/light_cyan1 bold]"))
                if decision_number == 'x': 
                    delete_lines(13)
                    return 
                else:
                    decision_number = int(decision_number)
    
                if decision_number < 0 or decision_number > len(key_habit_records_list) - 1:
                    raise ValueError(f"decision_number is not valid, it should range only from 0 - {len(key_habit_records_list) - 1}")
                else:
                    delete_lines(3 + len(key_habit_records_list))
                    break
            except:
                print(f"Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to {len(key_habit_records_list) - 1}![/bold red]")
                time.sleep(2)
                delete_lines(2)


    # delete habit
    del habit_records[key_habit_records_list[decision_number]]

    delete_lines(9)
    
# data
def main_flow():

    bright_colors = [
    "red1",
    "green1",
    "yellow1",
    "blue1",
    "magenta1",
    "cyan1",
    "orange1",
    "deep_pink1",
    "hot_pink",
    "chartreuse1",
    "spring_green1",
    "dodger_blue1",
    "purple",
    "gold1",
    "orchid1",
    "turquoise2",
    "sea_green1",
    "salmon1",
    "violet",
    "medium_orchid1",
    ]
    habit_records = {"meditating": {9: {4, 5, 6, 29, 28, 27, 26, 25, 23, 22, 21, 19, 12, 11, 10, 9, 6}}}


    while True:

        delete_lines(1)
        # display decision_numbers
        print("[bold red]█   █  ███  ████  ███ █████ ███  ███   ███[/bold red]")  
        print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
        print("[bold red]█████ █████ ████   █    █    █  █     █████[/bold red]") 
        print("[bold red]█   █ █   █ █   █  █    █    █  █     █   █[/bold red]") 
        print("[bold red]█   █ █   █ ████  ███   █   ███  ███  █   █[/bold red]") 

        print("\n\n[bold green][0][/bold green] [bold bright_white]Add a habit[/bold bright_white]")
        print("[bold yellow][1][/bold yellow] [bold bright_white]Log a habit[/bold bright_white]")
        print("[bold cyan][2][/bold cyan] [bold bright_white]See streak of a specific habit[/bold bright_white]")
        print("[bold magenta][3][/bold magenta] [bold bright_white]See all habit streak[/bold bright_white]")
        print("[bold yellow][4][/bold yellow] [bold bright_white]Delete a habit[/bold bright_white]\n")

        while True:
            try:
                decision_number = int(Prompt.ask("[light_cyan1 bold]What do you want to do? [0 - 4] [/light_cyan1 bold]"))
                if decision_number < 0 or decision_number > 4: # not a valid decision_number
                    raise ValueError("decision_number is not valid, it should range only from 1 - 4")
                else:
                    delete_lines(14)
                    break
            except:
                print("Input should be an [bold red]integer[/bold red] and [bold red]ranges from 0 to 4![/bold red]")
                time.sleep(2)
                delete_lines(2)

        if decision_number == 0:
            add_habit(habit_records)
        elif decision_number == 1:
            log_habit(habit_records, bright_colors)
        elif decision_number == 2:
            output_one_habit_streak(habit_records, bright_colors)
        elif decision_number == 3:
            output_all_habit_streak(habit_records)   
        elif  decision_number == 4:
            delete_habit(habit_records, bright_colors)


        # check if input is correct -> if it is asks again

        # check what decision_number used 
            # add_habit decision_number -> passes dictionary date

main_flow()




# ! https://claude.ai/share/fbd82ae4-354c-4636-b4bc-e0b53b720fbd





